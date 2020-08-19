#!/usr/bin/python3

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
ATTACHMENT = sys.argv[4]
BODY_TEXT = "Hello,\r\nThis mail is for the reporting of Non-Compliant Snapshots which do not have required tags."
 
BODY_HTML = """\
<html>
<head></head>
<body>
<h4>Hello Admin,</h4>
<p>Please refer to the attached excel sheet for the Non-Compliant Snapshot Report.</p>
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