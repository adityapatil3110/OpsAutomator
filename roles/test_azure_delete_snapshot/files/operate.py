#!/usr/bin/env python3

import os
import datetime
import sys
import json
from datetime import datetime
import pandas as pd


expiry_value = int()

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
    
print(snapshot_age)
