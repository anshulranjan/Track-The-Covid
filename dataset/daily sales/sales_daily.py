# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:44:06 2020

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

#city1
n = 4
data = [[] for x in range(n)]
z1 = cities.get_group(1)
z2 = z1.groupby('Dates')
print(z2.groups)
dict1 = z2.indices
def getList(dict): 
    return dict.keys() 
list_date = list(getList(dict1))
count = 0 
for i in range(0,len(list_date)):
    z3 = z2.get_group(list_date[count])
    b = z3['Package_id']==1
    c = z3['Package_id']==2
    d = z3['Package_id']==3
    e = b.value_counts().index.tolist()
    f = b.value_counts().tolist()
    g = c.value_counts().index.tolist()
    h = c.value_counts().tolist()
    i = d.value_counts().index.tolist()
    j = d.value_counts().tolist()
    k = e.index(True)
    l = g.index(True)
    m = i.index(True)
    data[0].append(list_date[count])
    data[1].append(f[k])
    data[2].append(h[l])
    data[3].append(j[m])
    count = count+1

df = DataFrame(data).transpose()
df.columns =['Date','Item_1','Item_2','Item_3']
df.to_csv('city1sales.csv', index=False)


#city2
n = 4
data = [[] for x in range(n)]
z1 = cities.get_group(2)
z2 = z1.groupby('Dates')
print(z2.groups)
dict1 = z2.indices
def getList(dict): 
    return dict.keys() 
list_date = list(getList(dict1))
count = 0 
for i in range(0,len(list_date)):
    z3 = z2.get_group(list_date[count])
    b = z3['Package_id']==1
    c = z3['Package_id']==2
    d = z3['Package_id']==3
    e = b.value_counts().index.tolist()
    f = b.value_counts().tolist()
    g = c.value_counts().index.tolist()
    h = c.value_counts().tolist()
    i = d.value_counts().index.tolist()
    j = d.value_counts().tolist()
    k = e.index(True)
    l = g.index(True)
    m = i.index(True)
    data[0].append(list_date[count])
    data[1].append(f[k])
    data[2].append(h[l])
    data[3].append(j[m])
    count = count+1

df = DataFrame(data).transpose()
df.columns =['Date','Item_1','Item_2','Item_3']
df.to_csv('city2sales.csv', index=False)


#city3
n = 4
data = [[] for x in range(n)]
z1 = cities.get_group(3)
z2 = z1.groupby('Dates')
print(z2.groups)
dict1 = z2.indices
def getList(dict): 
    return dict.keys() 
list_date = list(getList(dict1))
count = 0 
for i in range(0,len(list_date)):
    z3 = z2.get_group(list_date[count])
    b = z3['Package_id']==1
    c = z3['Package_id']==2
    d = z3['Package_id']==3
    e = b.value_counts().index.tolist()
    f = b.value_counts().tolist()
    g = c.value_counts().index.tolist()
    h = c.value_counts().tolist()
    i = d.value_counts().index.tolist()
    j = d.value_counts().tolist()
    k = e.index(True)
    l = g.index(True)
    m = i.index(True)
    data[0].append(list_date[count])
    data[1].append(f[k])
    data[2].append(h[l])
    data[3].append(j[m])
    count = count+1

df = DataFrame(data).transpose()
df.columns =['Date','Item_1','Item_2','Item_3']
df.to_csv('city3sales.csv', index=False)