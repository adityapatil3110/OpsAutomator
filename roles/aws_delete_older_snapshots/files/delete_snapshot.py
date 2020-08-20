#!/usr/bin/python3
# -*- coding: utf-8 -*-
import boto3
import sys
from datetime import datetime
from datetime import timezone

age = 2


######## Function for days_old

def days_old(date):
    date_obj = date.replace(tzinfo=None)
    diff = datetime.now() - date_obj
    return diff.days


ec2_client = boto3.client('ec2')

snapshot_response = ec2_client.describe_snapshots(OwnerIds=['self'])

for snapshot in snapshot_response['Snapshots']:
    create_date = snapshot['StartTime']
    snapshot_id = snapshot['SnapshotId']
    day_old = days_old(create_date)
    if day_old > age:
        print ('deleting -> ' + snapshot_id + ' as image is ' \
            + str(day_old) + ' days old.')
    #if day_old > age:
        #try:

            #print ('deleting -> ' + snapshot_id + ' as image is ' \
              #+ str(day_old) + ' days old.')

            # delete the snapshot

            #ec2.delete_snapshot(SnapshotId=snapshot_id)
        #except:
            #print "can't delete " + snapshot_id