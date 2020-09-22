#!/usr/bin/env python3

import os
import datetime
import sys
import json
from datetime import datetime
import pandas as pd

snapshot_response = sys.argv[1]
snapshot_response = json.dumps(snapshot_response)
snapshot_response = json.loads(snapshot_response)
print (snapshot_response[0]['name'])

#for snapshot in snapshot_response:
  #  snapshot_name = snapshot[0]['diskSizeBytes']
 #   print(snapshot_name)