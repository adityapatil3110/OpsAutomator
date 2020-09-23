#!/usr/bin/env python3

import os
import datetime
import sys
import json
from datetime import datetime
import pandas as pd

#quotes = '"""'
json_str_data = sys.argv[1]
for json_data in json_str_data:
  json_data = json_str_data.replace("\'", "\"")
#json_data = json.dumps(json_data)
  print(json_data)
#for snapshot in json_data:
 snapshot_response = json.loads(json_data)
#snapshot_response = json.dumps(snapshot_response)
#snapshot_response = json.loads(snapshot_response)
 print(snapshot_response[0]["name"])

#for snapshot in snapshot_response:
  #  snapshot_name = snapshot[0]['diskSizeBytes']
 #   print(snapshot_name)