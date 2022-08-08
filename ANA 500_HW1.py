#!/usr/bin/env python
# coding: utf-8

# In[164]:



import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import sympy as sp
import sys


# In[166]:


# gives current path directory
from pathlib import Path
print(Path.cwd());


# In[167]:


# read text file into pandas DataFrame
df = pd.read_csv("C:\\Users\\dpapa_fxbb8d0\\hessi.solar.flare.2002to2016.csv");
print(df);


# In[125]:


df.head();


# In[104]:


df.tail();


# In[129]:


df.shape


# In[168]:


df.columns


# In[122]:


df.dtypes;


# In[117]:


df.info;


# In[169]:


df


# In[170]:


# CLEAN & PREPARE DATA

# Are there any missing values from the 18 variables:
df.isnull().values.any()



# In[171]:


# find total number of missing values we have:
df.isnull().sum()


# In[172]:


# Making a list of other missing value types
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("hessi.solar.flare.2002to2016.csv", na_values = missing_values)

df.isnull().sum()


# In[173]:


# Drop all rows with 'NaN' entries:
df.dropna(inplace=True)
print(df)


# In[208]:


# check if rows with "NaN" are dropped:
df


# In[220]:


# Now, let's check if we have negative values in variables for out time and energy values
(df<0).values.any()


# In[ ]:




