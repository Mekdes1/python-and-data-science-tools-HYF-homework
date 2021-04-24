#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('train.csv')

# dataset
df.head()


# In[3]:


# summarized data
df.describe()


# In[4]:


# get data type and menorie information
df.info()


# In[5]:


df.shape


# In[9]:


cdf = df[['Survived','Pclass','Age','SibSp']]
cdf.head(5)


# In[10]:


viz = cdf[['Survived','Pclass','Age','SibSp']]
viz.hist()
plt.show()


# In[13]:



plt.scatter(cdf.Survived, cdf.Age,  color='green')
plt.xlabel("Survived")
plt.ylabel("Age")
plt.show()


# In[ ]:




