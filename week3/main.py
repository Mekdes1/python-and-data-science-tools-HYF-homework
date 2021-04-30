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


# In[2]:


df['min'] = pd.to_numeric(df['min'], errors = 'coerce') # change min from string to numeric
df.loc[df['sec'] > 60,'sec'] = np.nan
df.loc[~df['exp'].isin(['Yes','No']),'exp'] = np.nan
df.loc[~df['cor'].isin(['Yes','No']),'cor'] = np.nan


#summerize 

df.shape # size of data (number of (rows,columns) - recall, Python is zero-indexed)

df.describe() # numerical overview of each variable, by default only numeric types


# In[182]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
# numeric data
df.plot(x = 'Unnamed: 0', y = 'diff', kind = 'scatter') # scatter plot 
df.plot(x = 'hour', y = 'sec', kind = 'scatter')
df.plot(y = 'min', kind = 'density') # density plot


# In[3]:



# categorical data (a visualization of the frequence table from before)
df['type'].value_counts().plot(kind='bar')


# In[5]:


df.describe(include = 'all')


# In[4]:


col = df.loc[: , "sec":"min"]
df['secMean'] = col.mean(axis=1)
df


# In[ ]:


df.dropna()


# In[22]:





# In[7]:





# In[21]:





# In[18]:





# In[ ]:





# In[ ]:




