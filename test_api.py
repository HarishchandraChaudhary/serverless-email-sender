import requests
import json

def test_send_email():
    """Test the send email API endpoint."""
    
    # API endpoint (adjust URL based on your deployment)
    url = "http://localhost:3000/dev/send-email"
    
    # Test data
    test_data = {
        "receiver_email": "recipient@example.com",
        "subject": "Test Email from Python Serverless API",
        "body_text": "This is a test email sent from the Python serverless API.\n\nBest regards,\nYour API"
    }
    
    # Headers
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        # Send POST request
        response = requests.post(url, json=test_data, headers=headers)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except json.JSONDecodeError:
        print(f"Invalid JSON response: {response.text}")


def test_validation_errors():
    """Test API validation."""
    
    url = "http://localhost:3000/dev/send-email"
    
    # Test with missing fields
    test_data = {
        "receiver_email": "invalid-email",
        "subject": "",
        # missing body_text
    }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=test_data, headers=headers)
        print(f"Validation Test - Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
    except Exception as e:
        print(f"Validation test failed: {e}")


if __name__ == "__main__":
    print("Testing successful email send:")
    test_send_email()
    
    print("\n" + "="*50 + "\n")
    
    print("Testing validation errors:")
    test_validation_errors()
