import json
import os
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def create_response(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,POST'
        },
        'body': json.dumps(body, indent=2)
    }

def send_email(event, context):
    try:
        # Parse request
        body = json.loads(event.get('body', '{}'))
        
        # Basic validation
        if not body.get('receiver_email') or not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', body['receiver_email']):
            return create_response(400, {'success': False, 'message': 'Valid receiver_email required'})
        
        if not body.get('subject', '').strip():
            return create_response(400, {'success': False, 'message': 'Subject required'})
            
        if not body.get('body_text', '').strip():
            return create_response(400, {'success': False, 'message': 'Body text required'})
        
        # Get email credentials
        email_user = os.getenv('EMAIL_USER')
        email_pass = os.getenv('EMAIL_PASS')
        
        if not email_user or not email_pass:
            return create_response(500, {'success': False, 'message': 'Email credentials not set'})
        
        # Create and send email
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = body['receiver_email']
        msg['Subject'] = body['subject']
        msg.attach(MIMEText(body['body_text'], 'plain'))
        
        # Send via Gmail SMTP
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_user, email_pass)
            server.send_message(msg)
        
        return create_response(200, {
            'success': True,
            'message': 'Email sent successfully via SMTP'
        })
        
    except smtplib.SMTPAuthenticationError:
        return create_response(401, {'success': False, 'message': 'Email authentication failed'})
    except json.JSONDecodeError:
        return create_response(400, {'success': False, 'message': 'Invalid JSON'})
    except Exception as e:
        return create_response(500, {'success': False, 'message': f'Error: {str(e)}'})
