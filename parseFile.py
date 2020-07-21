#!/usr/bin/python
import listParse, MLabsData
import os.path as path
import sys

argn = len(sys.argv)
# should be made more dynamic, maybe as a cmd line argument
if (argn == 2):
    if (path.isfile(sys.argv[1])):
        listParse.file = sys.argv[1]
    else:
        print("ERROR: "+sys.argv[1]+" is not a file")
        exit()
else:
    listParse.file = './test.csv'
# the defaults for this file format
#listParse.DEBUG = True



listParse.delimiter = ';'

listParse.quotechar = '"'

listParse.fields = 45

listParse.readfile()

listParse.writefile()

MLabsData.title = path.basename(listParse.file)

MLabsData.MakeGraph(listParse.list)
exit()

