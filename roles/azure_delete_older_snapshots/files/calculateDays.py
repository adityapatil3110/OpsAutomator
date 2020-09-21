#!/usr/bin/env python3

import os
import datetime
import sys
from datetime import datetime
import pandas as pd

snapshot_date_raw_str = sys.argv[1]
snapshot_date_raw_str = snapshot_date_raw_str[:-6]
snapshot_date_raw_str = snapshot_date_raw_str.replace("T", " ")
snapshot_date = datetime.strptime(snapshot_date_raw_str, '%Y-%m-%d %H:%M:%S.%f')

#print(snapshot_date)


######## Function for days_old
def days_old(date):
    date_obj = date.replace(tzinfo=None)
    diff = datetime.now() - date_obj
    return diff.days


snapshot_age = int (days_old(snapshot_date))
print(snapshot_age)