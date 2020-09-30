#!/usr/bin/env python3

import os
import datetime
import sys
import json
from datetime import datetime
import pandas as pd


expiry_value = int()
limit = expiry_value
snap_list = []
start_time_list = []
snapshot_age_list = []
tag_dict = {}

snapshot_report_file = sys.argv[1]

######## Calculate difference of days between snapshot_creation_date and current_date
def days_old(date):
    date_obj = date.replace(tzinfo=None)
    diff = datetime.now() - date_obj
    return diff.days

f = open( snapshot_report_file, 'r' )

snapshot_details = json.loads(f.read())

#print(snapshot_details[0]['timeCreated'])

for snapshot in snapshot_details:
    timeCreated_str = snapshot['timeCreated']
    timeCreated = datetime.strptime(timeCreated_str[:-6].replace("T", " "), '%Y-%m-%d %H:%M:%S.%f')
    snapshot_age = days_old(timeCreated)
    snapshot_name = snapshot['name']
    location = snapshot['location']
    expiry_value = snapshot['tags']['Expiry']
    resource_group = snapshot['resourceGroup']
    tag_dict = snapshot['tags']


    if snapshot_age > limit:
        snap_list.append(snapshot_name)   
        start_time = str(timeCreated)
        start_time_list.append(start_time)
        snapshot_age_list.append(snapshot_age)

        # Generate the Report name for deleted snapshots and push the column names and details of the deleted snapshots
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
        filename = '/home/ansible/AzureDeletedSnapshotReport'+ date_time +'.csv'
        print (filename)
        dict = {'SnapshotNames':snap_list, 'StartTime':start_time_list, 'Age':snapshot_age_list, 'Tags':tag_dict}
        print(dict)
        df = pd.DataFrame(dict)
        df.to_csv(filename, index=False)