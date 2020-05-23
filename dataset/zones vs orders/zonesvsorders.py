# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:08:55 2020

@author: anshu
"""


import pandas as pd
import numpy as np
from pandas import DataFrame

df = pd.read_csv("dataset.csv")
df1 = pd.read_csv("sales.csv")
dataset = pd.merge(df, df1, on="Customer_id")
cities = dataset.groupby('City_Id')
print(cities.groups)

for city, group in cities:
    print(cities)
    print(group)


n = 2
data = [[] for x in range(n)]
z1 = cities.get_group(1)
count = 0 
for i in range(0,20):
    count = count+1
    z3 = z1[z1['Zones_id']==count]
    a = len(z3.index)
    data[0].append(count)
    data[1].append(a)

df = DataFrame(data).transpose()
df.columns =['Zone_id','Average_Calorie']
df.to_csv('zonesorders1.csv', index=False)


#city2
n = 2
data = [[] for x in range(n)]
z1 = cities.get_group(2)
count = 0 
for i in range(0,20):
    count = count+1
    z3 = z1[z1['Zones_id']==count]
    a = len(z3.index)
    data[0].append(count)
    data[1].append(a)

df = DataFrame(data).transpose()
df.columns =['Zone_id','Total Orders']
df.to_csv('zonesorders2.csv', index=False)

#city3
n = 2
data = [[] for x in range(n)]
z1 = cities.get_group(3)
count = 0 
for i in range(0,20):
    count = count+1
    z3 = z1[z1['Zones_id']==count]
    a = len(z3.index)
    data[0].append(count)
    data[1].append(a)

df = DataFrame(data).transpose()
df.columns =['Zone_id','Total Orders']
df.to_csv('zonesorders3.csv', index=False)