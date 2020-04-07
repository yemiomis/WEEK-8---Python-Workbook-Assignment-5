#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd


# In[16]:


names = ['Bob','Jessica','Mary','John','Mel']


# In[17]:


grades = [76,95,77,78,99]


# In[18]:


bsdegrees = [1,1,0,0,1]


# In[19]:


msdegrees = [2,1,0,0,0]


# In[20]:


phddegrees = [0,1,0,0,0]


# In[22]:


GradeList = zip(names,grades,bsdegrees,msdegrees, phddegrees)


# In[23]:


df = pd.DataFrame(data=GradeList,columns=['Names','Grades', 'bsdegrees','msdegrees','phddegrees'])


# In[24]:


df


# In[28]:


df['Grades'].count()


# In[29]:


df['Grades'].mean()


# In[30]:


df['Grades'].std()


# In[31]:


df['Grades'].min()


# In[32]:


df['Grades'].max()


# In[33]:


df['Grades'].quantile(.25)


# In[34]:


df['Grades'].quantile(.5)


# In[35]:


df['Grades'].quantile(.75)


# In[ ]:




