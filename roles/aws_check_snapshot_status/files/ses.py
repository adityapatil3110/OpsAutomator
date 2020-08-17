import boto3
from botocore.exceptions import ClientError


#DEFINE ARGUMENTS  

# 1) Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
#SENDER =  "sender_identity"
#"patiladi3110@gmail.com" 
sender = sys.argv[1]

# 2) Replace recipient@example.com with a "To" address. If your account 
# is still in the sandbox, this address must be verified.
#RECIPIENT = "reciever_identity"
#"gcptesting4534@gmail.com" #
reciever = sys.argv[2]

# Specify a configuration set. If you do not want to use a configuration
# set, comment the following variable, and the 
# ConfigurationSetName=CONFIGURATION_SET argument below.
#CONFIGURATION_SET = "ConfigSet"

# 3) If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
#AWS_REGION =  "region" 
#"us-east-2" #
region = sys.argv[3]

# The subject line for the email.
SUBJECT = "Warning for Untagged Snapshots"

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("List of Untagged Snapshots for the Account\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
            )
            
# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Untagged Snapshot Details</h1>
  <p>Here are the details of Untagged Snapshots: 
</body>
</html>
            """            

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=region)

# Try to send the email.
try:
    #Provide the contents of the email.
    response = client.send_email(
        Destination={
            'ToAddresses': [
                reciever,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=sender,
        # If you are not using a configuration set, comment or delete the
        # following line
        #ConfigurationSetName=CONFIGURATION_SET,
    )
# Display an error if something goes wrong.	
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])