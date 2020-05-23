# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:54:08 2020

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
n = 2
data = [[] for x in range(n)]
z1 = cities.get_group(1)
count = 0 
for i in range(0,20):
    count = count+1
    z2 = z1[z1['Zones_id']==count]
    a = len(z2.index)
    data[0].append(count)
    data[1].append(a)

df = DataFrame(data).transpose()
df.columns =['Zone_id','Total Users']
df.to_csv('zonesvsusers1.csv', index=False)

#city2
n = 2
data = [[] for x in range(n)]
z1 = cities.get_group(2)
count = 0 
for i in range(0,20):
    count = count+1
    z2 = z1[z1['Zones_id']==count]
    a = len(z2.index)
    data[0].append(count)
    data[1].append(a)

df = DataFrame(data).transpose()
df.columns =['Zone_id','Total Users']
df.to_csv('zonesvsusers2.csv', index=False)


#city3
#city1
n = 2
data = [[] for x in range(n)]
z1 = cities.get_group(3)
count = 0 
for i in range(0,20):
    count = count+1
    z2 = z1[z1['Zones_id']==count]
    a = len(z2.index)
    data[0].append(count)
    data[1].append(a)

df = DataFrame(data).transpose()
df.columns =['Zone_id','Total Users']
df.to_csv('zonesvsusers3.csv', index=False)


 