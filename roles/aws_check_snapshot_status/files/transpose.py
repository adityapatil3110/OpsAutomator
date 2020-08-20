#!/usr/bin/python3

import sys
import pandas as pd


raw_file= sys.argv[1]

df = pd.read_csv(raw_file)

df = df.transpose()

df = df.to_csv(raw_file, index=False, header=False)