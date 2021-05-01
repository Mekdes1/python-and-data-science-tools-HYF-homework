#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

#Task 1: Clean the data (that is, follow these steps:
#1) load the data
#2) identify nonsensical values
#3) remove/change any nonsensical values

df = pd.read_csv('responses.csv', delimiter = ",") 


# In[13]:


df # read data

#dentify nonsensical values and change the values
df2=df.drop(['minSekRaw'], axis = 1)
df2['min'] = pd.to_numeric(df2['min'], errors = 'coerce') # change min from string to numeric
df2.loc[df2['sec'] > 60,'sec'] = np.nan
df2.loc[~df2['exp'].isin(['Yes','No']),'exp'] = np.nan  # change to nan if value is not correct
df2.loc[~df2['cor'].isin(['Yes','No']),'cor'] = np.nan
df2['time'] = df2['min']*60 + df2.sec # make a time variable


#summerize 

df2.shape # size of data (number of (rows,columns) - recall, Python is zero-indexed)
df2.describe(include='all')  
df2.describe() # numerical overview of each variable, by default only numeric types

#plot data
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
# numeric data
df2.plot(x = 'Unnamed: 0', y = 'diff', kind = 'scatter') # scatter plot 
df2.plot(x = 'hour', y = 'sec', kind = 'scatter')
df2.plot(y = 'min', kind = 'density') # density plot
df2['type'].value_counts().plot(kind='bar')


#calculate mean time
GreekTime = df2[df2['type'] == 'Greek'].time.mean()
LatinTime = df2[df2['type'] == 'Latin'].time.mean()
print('GreekTime', GreekTime)
print('LatinTime',LatinTime)
if GreekTime > LatinTime:
   print('The players were faster solving the Latin words')
print('The Players were faster solving the Geek words')


# In[ ]:




