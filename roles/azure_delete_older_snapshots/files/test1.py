#!/usr/bin/env python3

import os
import datetime
import sys
import json
from datetime import datetime
import pandas as pd

#quotes = '"""'
json_str_data = sys.argv[1]
json_str_data = json_str_data.replace('{\n  ', '{\n  "')
json_str_data = json_str_data.replace(':', '": "')
json_str_data = json_str_data.replace(',\n', '",\n"')
json_str_data = json_str_data.replace('": " {', '": {')
json_str_data = json_str_data.replace('"\n}",', '},')
json_str_data = json_str_data.replace('\n}",', '"\n},')
json_str_data = json_str_data.replace('" null"', 'null')
json_str_data = json_str_data.replace('" null\n    }",', 'null\n      },')




f = open( '/home/ansible/Azure_Old_Snapshot_List.json', 'w' )
f.write(json_str_data)


f = open( '/home/ansible/Azure_Old_Snapshot_List.json', 'r' )

snapshot_details = json.loads(f.read())

for snapshot in snapshot_details:
    print(snapshot)
    
    
f.close()