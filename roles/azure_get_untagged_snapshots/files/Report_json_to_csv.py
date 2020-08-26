#!/usr/bin/python3

import json
import csv
import sys
import os

#raw_file = sys.argv[1]
#actual_file = sys.argv[2]

header = ['Name', 'ResourceGroup', 'StartTime', 'SKU Tier', 'SnapshotID']

#if you are not using utf-8 files, remove the next line
#sys.setdefaultencoding("UTF-8") #set the encode to utf8
#check if you pass the input file and output file

if sys.argv[1] is not None and sys.argv[2] is not None:
    raw_file = sys.argv[1]
    actual_file = sys.argv[2]
    
    inputFile = open(raw_file) #open json file
    outputFile = open(actual_file, 'w') #load csv file
    
    data = json.load(inputFile) #load json content
    print (data)
    inputFile.close() #close the input file
    
    output = csv.writer(outputFile) #create a csv.write
    output.writerow(header)  # header row
    #output.writerow(data[0].keys())  # header row
    for row in data:
        print (data)
        output.writerow(data) #values row