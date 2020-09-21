#!/usr/bin/env python3

import os
import sys
from datetime import datetime
import pandas as pd

start_date = sys.argv[1]

print (start_date)

######## Function for days_old

def days_old(date):
    date_obj = datetime.datetime(date)
    diff = datetime.now() - date_obj
    return diff.days


days = days_old(start_date)
