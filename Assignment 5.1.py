#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np


# In[8]:


df = pd.read_csv(r"C:\Users\Envy 360\Desktop\learn-data-analysis-w-python-master\learn-data-analysis-w-python-master\datasets\gradedata.csv")


# In[9]:


df.head()


# In[10]:


df.tail()


# In[11]:


df.take(np.random.permutation(len(df))[:500])


# In[ ]:




