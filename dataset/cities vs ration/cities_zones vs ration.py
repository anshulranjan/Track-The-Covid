# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:57:55 2020

@author: anshu
"""

import pandas as pd
import numpy as np
from pandas import DataFrame

dataset = pd.read_csv("dataset.csv")


cities = dataset.groupby('City_Id')
print(cities.groups)

for city, group in cities:
    print(cities)
    print(group)


#city1
n = 3
data = [[] for x in range(n)]
count = 0 
z1 = cities.get_group(1)
for i in range(0,20):
    count = count+1
    z2 = z1[z1['Zones_id']==count]
    b = z2['Ration Opt']==1
    c = b.value_counts().index.tolist()
    d = b.value_counts().tolist()
    e = c.index(True)
    f = c.index(False)
    data[0].append(count)
    data[1].append(d[e])
    data[2].append(d[f])
df = DataFrame(data).transpose()
df.columns =['Zone_id','Ration_Yes','Ration_No']
df.to_csv('city1.csv', index=False)


#city2
n = 3
data = [[] for x in range(n)]
count = 0 
z1 = cities.get_group(2)
for i in range(0,20):
    count = count+1
    z2 = z1[z1['Zones_id']==count]
    b = z2['Ration Opt']==1
    c = b.value_counts().index.tolist()
    d = b.value_counts().tolist()
    e = c.index(True)
    f = c.index(False)
    data[0].append(count)
    data[1].append(d[e])
    data[2].append(d[f])
df = DataFrame(data).transpose()
df.columns =['Zone_id','Ration_Yes','Ration_No']
df.to_csv('city2.csv', index=False)


#city3
n = 3
data = [[] for x in range(n)]
count = 0 
z1 = cities.get_group(3)
for i in range(0,20):
    count = count+1
    z2 = z1[z1['Zones_id']==count]
    b = z2['Ration Opt']==1
    c = b.value_counts().index.tolist()
    d = b.value_counts().tolist()
    e = c.index(True)
    f = c.index(False)
    data[0].append(count)
    data[1].append(d[e])
    data[2].append(d[f])
df = DataFrame(data).transpose()
df.columns =['Zone_id','Ration_Yes','Ration_No']
df.to_csv('city3.csv', index=False)
