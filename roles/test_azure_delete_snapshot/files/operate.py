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

print(snapshot_details)