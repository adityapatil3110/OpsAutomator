#!/usr/bin/python3

import pandas as pd
import sys

raw_file = sys.argv[1]

header = ['OwnerID', 'SnapshotID', 'StartTime']


df = pd.read_csv(raw_file, header=None)

df.to_csv(raw_file, header=header, index=False)