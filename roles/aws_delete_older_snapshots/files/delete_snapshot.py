#!/usr/bin/python3
# -*- coding: utf-8 -*-
############################################################################################################################################################
#### Fetching and Deleting the Older Snapshots
############################################################################################################################################################
import boto3
import sys
from datetime import datetime
from datetime import timezone

age = 2
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

snapshot_response = ec2_client.describe_snapshots(OwnerIds=['self'])


for snapshot in snapshot_response['Snapshots']:
    create_date = snapshot['StartTime']
    snapshot_id = snapshot['SnapshotId']
    owner_id = snapshot['OwnerId']
    day_old = days_old(create_date)
    snap_list.append(snapshot_id)
    start_time = str(create_date)
    ownerid_list.append(owner_id)
    start_time_list.append(start_time)
    day_old_list.append(day_old)
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
now = datetime.now()
date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
filename = '/home/ansible/DeletedSnapshotReport'+ date_time +'.csv'
dict = {'OwnerId': owner_id, 'SnapshotIDs':snap_list, 'StartTime':start_time, 'Age':day_old}
df = pd.DataFrame(dict)
df.to_csv(filename, index=False)

############################################################################################################################################################
# Sending Report of the deleted Snapshots
############################################################################################################################################################