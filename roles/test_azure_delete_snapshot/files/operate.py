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
snap_age_list = []
snap_location_list = []
snap_sku_tier_list = []
snap_rg_list = []
snap_id_list = []
tag_dict = {}

snapshot_report_file = sys.argv[1]

######## Calculate difference of days between snapshot_creation_date and current_date
def days_old(date):
    date_obj = date.replace(tzinfo=None)
    diff = datetime.now() - date_obj
    return diff.days

f = open( snapshot_report_file, 'r' )

snapshot_details = json.loads(f.read())


for snapshot in snapshot_details:
    timeCreated_str = snapshot['timeCreated']
    timeCreated = datetime.strptime(timeCreated_str[:-6].replace("T", " "), '%Y-%m-%d %H:%M:%S.%f')
    snapshot_name = snapshot['name']
    location = snapshot['location']
    sku_tier = snapshot['sku']['tier']
    expiry_value = snapshot['tags']['Expiry']
    resource_group = snapshot['resourceGroup']
    snapshot_id = snapshot['id']
    tag_dict = snapshot['tags']['Expiry']
    snapshot_age = days_old(timeCreated)
    if snapshot_age > limit:
        print(snapshot_name)
        snap_list.append(snapshot_name)   
        start_time = str(timeCreated)
        start_time_list.append(start_time)
        snap_age_list.append(snapshot_age)
        snap_location_list.append(location) 
        snap_sku_tier_list.append(sku_tier)
        snap_rg_list.append(resource_group)
        snap_id_list.append(snapshot_id)
        dict = {'SnapshotNames':snap_list, 'StartTime':start_time_list, 'SnapshotAge':snap_age_list, 'Expiry_Limit_in_Days':tag_dict, 'Resource_Group':snap_rg_list, 'Location':snap_location_list, 'SKU_TIER':snap_sku_tier_list, 'Snapshot_id':snaps_id_list}
        # Generate the Report name for deleted snapshots and push the column names and details of the deleted snapshots
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = '/home/ansible/AzureDeletedSnapshotReport'+ date_time +'.csv'
        #report_dict = {'SnapshotNames':snap_list, 'StartTime':start_time_list, 'SnapshotAge':snapshot_age_list, 'Expiry_Limit_in_Days':tag_dict}
        #print (filename)
        df = pd.DataFrame(dict)
        df.to_csv(filename, index=False) 
        
print(snap_list)