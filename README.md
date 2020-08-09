# MLabsDataPlot

MLabDataPlot is a small Python utility i wrote to parse the csv files created by the MotionLabs Logger at the company I worked at before the COVID-19.
Since they had no intrest in supporting the development of this tool, I'm going to opensource it and hopefully create a PHP or react.js version of this tool later on.
The MotionLabs Power Logger is a 3-Phase inline power monitor that logs the power usage for event power, like tradeshows, theater, corperate AV.

Right now this will take the CSV file, cleans up the data while parsing the file and graphs the data for 120 V, 220 V and the Current.
The CSV files are very large in size and contain logs of power usage throughout the day, aprox every 11-12 sec.
There are 45 columns of data, I only used 10 for this tool;  This is enough to see how each phase is being used and if the Dimmer Tech didn't balance their loads.
The graphs can visually display voltage drops and spikes, and how much current has been used throughout the day.

I have included a php CSV generator for this tool and I have replaced all the previous logs with the random generated ones.  the random data might look odd at the moment, but it is basically the same format as the CSV files that were generated from the hardware.

## Prerequisites

```
pip3 install plotly
```

### Generate the Offline Plotly HTML file with test script

```
python3 ./parseFile.py <CSV file>.csv
```

### Use this in your own script.

```
#!/usr/bin/python3
import listParse, MLabsData
import os.path as path
import sys

listParse.file = './test.csv'

listParse.delimiter = ';'

listParse.quotechar = '"'

listParse.fields = 45

listParse.readfile()

listParse.writefile()

MLabsData.title = path.basename(listParse.file)

MLabsData.MakeGraph(listParse.list)
```