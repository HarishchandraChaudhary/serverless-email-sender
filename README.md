Serverless Email Sender
This is a simple serverless REST API built with the Serverless Framework and Python that sends an email using SMTP. It's designed to be deployed to AWS Lambda and API Gateway.

🚀 Getting Started
Prerequisites
You need to have the following installed on your machine:

Node.js & npm: The Serverless Framework is a Node.js application.

Python 3.9: The runtime for the AWS Lambda function.

Installation
Clone the repository and navigate to the project directory:

Bash

git clone https://github.com/HarishchandraChaudhary/serverless-email-sender.git
cd serverless-email-sender
Install the Serverless Framework and plugins:

Bash

npm install -g serverless
npm install serverless-offline serverless-python-requirements
Install Python dependencies:
The serverless-python-requirements plugin will handle this automatically during deployment, but for local testing, you can install them manually if needed (though the only dependency is the standard library smtplib).

⚙️ Configuration
Before you can run the API, you must configure your email credentials as environment variables. Do not hardcode these in your files.

Update the serverless.yml file with your email address and an application-specific password.

YAML

# serverless.yml
...
provider:
  name: aws
  runtime: python3.9
  environment:
    EMAIL_ADDRESS: your-email@example.com
    EMAIL_PASSWORD: your-email-app-password
...
Note: The EMAIL_PASSWORD should be an app password, not your regular email password. You can generate one from your email provider's security settings (e.g., Google Account > Security > App passwords).

💻 Local Development
Run the API locally using the serverless-offline plugin.

Bash

sls offline start
This will start a local server, and your API will be available at http://localhost:3000/.

📬 API Endpoint
The API exposes a single endpoint for sending emails.

Method	Path	Description
POST	/email/send	Sends an email with the provided details.

Export to Sheets
Request Body
The API expects a JSON body with the following fields:

Field	Type	Description	Required
receiver_email	string	The email address of the recipient.	Yes
subject	string	The subject line of the email.	Yes
body_text	string	The plain text content of the email.	Yes

Export to Sheets
Example Usage (curl)
Bash

curl -X POST \
  http://localhost:3000/email/send \
  -H 'Content-Type: application/json' \
  -d '{
    "receiver_email": "test@example.com",
    "subject": "Hello from my Serverless API",
    "body_text": "This is a test email sent from a local serverless function."
  }'
🚀 Deployment
To deploy this function to your AWS account, run the following command:

Bash

sls deploy
This will package your service, create the necessary AWS resources, and deploy your Lambda function and API Gateway endpoint.

