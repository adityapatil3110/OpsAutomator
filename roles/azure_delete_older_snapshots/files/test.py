#!/usr/bin/env python3

import os
import datetime
import sys
from datetime import datetime
import pandas as pd

snapshot_response = sys.argv[1]

for snapshot in snapshot_response:
    snapshot_name = snapshot[0]['name']
    print(snapshot_name)