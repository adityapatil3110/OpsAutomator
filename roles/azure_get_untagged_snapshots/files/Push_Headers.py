#!/usr/bin/python3

import json
import csv
import sys
import os


header = ['Name', 'ResourceGroup', 'StartTime', 'SKU Tier', 'SnapshotID']


if sys.argv[1] is not None and sys.argv[2] is not None:
    raw_file = sys.argv[1]
        
    inputFile = open(raw_file, 'w') #Load CSV File
    #outputFile = open(actual_file, 'w') #load csv file
    
    #data = json.load(inputFile) #load json content
    #print (data)
    #inputFile.close() #close the input file
    
    output = csv.writer(inputFile) #create a csv.write
    output.writerow(header)  # header row