#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[5]:


data=pd.read_csv("/home/placement/Desktop/raj.csv")


# In[6]:


data.head(10)


# In[7]:


data.describe()


# In[9]:


data.isna().sum()


# In[10]:


data.shape


# In[11]:


data.info()


# In[12]:


data2=data.groupby(['year']).count()


# In[13]:


data2


# In[14]:


data2.to_csv('raj1.csv')


# In[ ]:





# In[ ]:




