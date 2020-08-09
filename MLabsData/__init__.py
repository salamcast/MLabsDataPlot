#!/usr/bin/python

# @package: MLabsDataPlot
# @author:  Abu Khadeejah Karl Holz <binholz|[A]|hotmail|d|com>

import plotly.offline as ol
import plotly.graph_objs as go

import datetime

title = 'MLabsDataPlot'

TS = []
# 120 Volts
L1 = []
L2 = []
L3 = []
# 208 Volts
L12 = []
L23 = []
L31 = []

# Amps
I1 = []
I2 = []
I3 = []



def MakeGraph(data):
    r = 0
    for t in data:
        if r == 0:
            r = 1
        else:
            add_time(t[0])
            # 120 V
            add_L1(t[1])
            add_L2(t[2])
            add_L3(t[3])
            # 208v
            add_L12(t[4])
            add_L23(t[5])
            add_L31(t[6])
            # amps
            add_I1(t[7])
            add_I2(t[8])
            add_I3(t[9])

    blue = dict( color = ('rgb(22, 96, 167)'), width = 2,)
    red = dict( color = ('rgb(205, 12, 24)'), width = 2)
    black = dict( color = ('rgb(0, 0, 0)'), width = 2)

    v120 = go.Figure()
    v120.add_trace(go.Scatter(
                               x=TS,
                               y=L1,
                               mode = 'lines+markers',
                               name = 'L1',
                               line = blue
                       ))
    v120.add_trace(go.Scatter(
                               x=TS,
                               y=L2,
                               mode = 'lines+markers',
                               name = 'L2',
                               line = red
                       ))
    v120.add_trace(go.Scatter(
                               x=TS,
                               y=L3,
                               mode = 'lines+markers',
                               name = 'L3',
                               line = black
                       ))
    ol.plot(v120, filename=title+'-120v.html')

    v208 = go.Figure()
    v208.add_trace(go.Scatter(
                               x=TS,
                               y=L12,
                               mode = 'lines',
                               name = 'L12',
                               line = blue
                       ))
    v208.add_trace(go.Scatter(
                               x=TS,
                               y=L23,
                               mode = 'lines',
                               name = 'L23',
                               line = red
                       ))
    v208.add_trace(go.Scatter(
                               x=TS,
                               y=L31,
                               mode = 'lines',
                               name = 'L31',
                               line = black
                       ))
    ol.plot(v208, filename=title+'-208v.html')

    amps = go.Figure()
    amps.add_trace(go.Scatter(
                               x=TS,
                               y=I1,
                               mode = 'lines+markers',
                               name = 'I1',
                               line = blue
                       ))
    amps.add_trace(go.Scatter(
                               x=TS,
                               y=I2,
                               mode = 'lines+markers',
                               name = 'I2',
                               line = red
                       ))
    amps.add_trace(go.Scatter(
                               x=TS,
                               y=I3,
                               mode = 'lines+markers',
                               name = 'I3',
                               line = black
                       ))
    ol.plot(amps, filename=title+'-amps.html')


def add_time(t):
    #12:02:05
    TS.append(t)

def add_L1(v):
    L1.append(v.strip("V").strip())

def add_L2(v):
    L2.append(v.strip("V").strip())

def add_L3(v):
    L3.append(v.strip("V").strip())

def add_L12(v):
    L12.append(v.strip("V").strip())

def add_L23(v):
    L23.append(v.strip("V").strip())

def add_L31(v):
    L31.append(v.strip("V").strip())

def add_I1(a):
    I1.append(a.strip("A").strip())

def add_I2(a):
    I2.append(a.strip("A").strip())

def add_I3(a):
    I3.append(a.strip("A").strip())
