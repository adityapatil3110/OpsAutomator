#!/usr/bin/python

import os
import sys
import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
 
SENDER = sys.argv[1]
RECIPIENT = sys.argv[2]
AWS_REGION = sys.argv[3]
SUBJECT = "Reporting Untagged Snapshots"
ATTACHMENT = "report.csv"
BODY_TEXT = "Hello,\r\nPlease see the attached file for a list of customers to contact."
 
BODY_HTML = """\
<html>
<head></head>
<body>
<h4>Hello Admin,</h4>
<p>Please refer to the attached excel sheet for the report.</p>
<h4>Regards,</h4>
<h5>Kunal</h5>
</body>
</html>
"""
 
CHARSET = "utf-8"
 
client = boto3.client('ses',region_name=AWS_REGION)
 
msg = MIMEMultipart('mixed')
msg['Subject'] = SUBJECT 
msg['From'] = SENDER 
msg['To'] = RECIPIENT
 
msg_body = MIMEMultipart('alternative')
 
textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)
 
msg_body.attach(textpart)
msg_body.attach(htmlpart)
 
att = MIMEApplication(open(ATTACHMENT, 'rb').read())
 
att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))
 
msg.attach(msg_body)
 
msg.attach(att)
try:
    response = client.send_raw_email(
        Source=SENDER,
        Destinations=[
            RECIPIENT
        ],
        RawMessage={
            'Data':msg.as_string(),
        },
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])