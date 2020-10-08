#!/usr/bin/env python3
import datetime
import sys
import json
from datetime import datetime
import pandas as pd
import base64
import os
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
from sendgrid import SendGridAPIClient

filename = sys.argv[1]
SENDER = sys.argv[2]
RECIPIENT = sys.argv[3]
SENDGRID_API_KEY= sys.argv[4]
name = filename.strip("/home/ansible/")
                        
message = Mail(
        from_email=SENDER,
        to_emails=RECIPIENT,
        subject='Azure untagged snapshot report',
        html_content='<html><head>Hi</head><body><h4>Hello Admin,</h4><p>Please refer to the attached excel sheet for the Azure Untagged Snapshot Report. And do add the tag as Epiry=Number_of_days.</p><h4>Regards,</h4><h5>Aditya</h5></body></html>')
file_path = filename
with open(file_path, 'rb') as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()
attachment = Attachment()
attachment.file_content = FileContent(encoded)
attachment.file_type = FileType('text/csv')
attachment.file_name = FileName(name)
attachment.disposition = Disposition('attachment')
attachment.content_id = ContentId('AZUntagged Snapshots')
message.attachment = attachment
try:
    sendgrid_client = SendGridAPIClient(SENDGRID_API_KEY)
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)