#!/usr/bin/python

# @package: listParse
# @author:  Abu Khadeejah Karl Holz <binholz|[A]|hotmail|d|com>

import csv
import os

titles = []

#file to parse
file = ''

# main list variable
list = []

# show text list while debuging, can be used to make a new file
DEBUG = False

# default delimiter is ','. some files use ; or .
delimiter = ","

# default quote charater is ' .  somefiles use "
quotechar = "'"

# fields is for the number of fields to expect, and to ignore any data row that dosen't conform
# the number of fields your file has, this is a hardset number.
# this parser won't match rows that don't exactly contain this set number
fields = 5
 
# txt is for the newly parsed csv 
txt = ''

# this is for reading a CSV file, not all are the same format

def readfile():
    if (os.path.isfile(file)):
        newcsv = []
        with open(file) as csvfile:
            # remove any spaces and the delimiter from the end of the line
            for d in csvfile:
                newcsv.append(d.rstrip().rstrip(delimiter))
            # parse the new updated CSV data
            reader = csv.reader(newcsv, delimiter=delimiter, quotechar=quotechar)
            n=0
            for row in reader:
                if len(row) == fields:
                    list.append([])
                    for x in row:
                        if (n == 0):
                            titles.append(x.strip())
                        list[n].append(x.strip())
                    if (DEBUG):
                        # test parse of CSV file
                        txt = ', '.join(list[n])
                        #print(txt.rstrip().rstrip(','))
                    n=n+1

def writefile():
    if len(list) == 0:
        print("ERROR:    You need to read a CSV file first")
    else:
        # write file
        n = 0
        for l in list:
            fix = []
            if n == 0:
                n = 1
            else: 
                for f in l:
                    fix.append(f.strip("V").strip("A").strip().strip())
                
            txt = ','.join(fix)
            #print(txt.rstrip().rstrip(','))
         