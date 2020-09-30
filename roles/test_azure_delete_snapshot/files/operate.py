#!/usr/bin/env python3

import os
import datetime
import sys
import json
from datetime import datetime
import pandas as pd

snapshot_report_file = sys.argv[1]


f = open( snapshot_report_file, 'r' )

snapshot_details = json.loads(f.read())

#print(snapshot_details[0]['timeCreated'])

for snapshot in snapshot_details:
    timeCreated_str = snapshot['timeCreated']
    timeCreated = datetime.strptime(timeCreated_str[:-6].replace("T", " "), '%Y-%m-%d %H:%M:%S.%f')
    snapshot_name = snapshot['name']
    location = snapshot['location']
    expiry_value = snapshot['tags']['Expiry']
    resource_group = snapshot['resourceGroup']
    
print(timeCreated)