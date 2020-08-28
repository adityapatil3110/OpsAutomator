#!/usr/bin/python3
# -*- coding: utf-8 -*-
############################################################################################################################################################
#### Fetching and Deleting the Older Snapshots
############################################################################################################################################################
#!/usr/bin/python3
import os
import sys
import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd
from datetime import datetime

age_limit = None
snap_list = []
ownerid_list = []
start_time_list = []
day_old_list = []

######## Function for days_old

def days_old(date):
    date_obj = date.replace(tzinfo=None)
    diff = datetime.now() - date_obj
    return diff.days


ec2_client = boto3.client('ec2')

snapshot_response = ec2_client.describe_snapshots(OwnerIds=['self'],
            Filters=[
                {'Name': 'tag:Expiry', 'Values': ['*']}
                  ]
              )
#print (snapshot_response)

for snapshot in snapshot_response['Snapshots']:
    create_date = snapshot['StartTime']
    snapshot_id = snapshot['SnapshotId']
    owner_id = snapshot['OwnerId']
    day_old = days_old(create_date)
    
    for tag in snapshot_response['Snapshots[].[Tags]']:
        if tag['Key'] == 'Expiry':
            age_limit = tag.get('Value')
            print (age_limit)
    
    
    
    if day_old > age_limit:
        snap_list.append(snapshot_id)
        start_time = str(create_date)
        ownerid_list.append(owner_id)
        start_time_list.append(start_time)
        day_old_list.append(day_old)
        
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
        filename = '/home/ansible/DeletedSnapshotReport'+ date_time +'.csv'
        print (filename)
        dict = {'OwnerId': owner_id, 'SnapshotIDs':snap_list, 'StartTime':start_time, 'Age':day_old}
        df = pd.DataFrame(dict)
        df.to_csv(filename, index=False)
        
        SENDER = sys.argv[1]
        RECIPIENT = sys.argv[2]
        AWS_REGION = sys.argv[3]
        SUBJECT = "Reporting Untagged Snapshots"
        ATTACHMENT = filename
        BODY_TEXT = "Hello,\r\nThis mail is for the reporting of Non-Compliant Snapshots which do not have required tags."
        
        BODY_HTML = """\
        <html>
        <head></head>
        <body>
        <h4>Hello,</h4>
        <p>Please refer to the attached excel sheet for the Non-Compliant Snapshot Report.</p>
        <h4>Regards,</h4>
        <h5>Aditya Patil</h5>
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
        try:
            ec2.delete_snapshot(SnapshotId=snapshot_id, DRYRun=True)
        except:
            print ("can't delete " + snapshot_id)


############################################################################################################################################################
# Sending Report of the deleted Snapshots
############################################################################################################################################################
