#!/usr/bin/env python3

import os
import datetime
import sys
import json
from datetime import datetime
import pandas as pd

#quotes = '"""'
json_str_data = sys.argv[1]

f = open( '/home/ansible/Azure_Old_Snapshot_List.json', 'w' )
f.write(json_str_data)
f.close()