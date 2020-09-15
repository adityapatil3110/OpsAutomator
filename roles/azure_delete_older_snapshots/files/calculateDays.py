#!/usr/bin/env python3

import os
import sys
from datetime import datetime


start_date = sys.argv[1]



######## Function for days_old

def days_old(date):
    date_obj = date.replace()
    diff = datetime.now() - date_obj
    return diff.days


days = days_old(start_date)
