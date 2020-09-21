#!/usr/bin/env python3

import os
import sys
from datetime import datetime
import pandas as pd

snapshot_date_obj = sys.argv[1]

snapshot_date = datetime.strptime(snapshot_date_obj, '%Y-%m-%d%H:%M:%S.%f%:z')
print (snapshot_date)

######## Function for days_old

def days_old(date):
    date_obj = datetime.datetime(date)
    diff = datetime.now() - date_obj
    return diff.days


days = days_old(snapshot_date)
