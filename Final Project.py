#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


business=pd.read_csv('/Users/akhilnallacheruvu/Downloads/Business_Licenses-2.csv')


# In[10]:


business_loc=business[['DOING BUSINESS AS NAME','LATITUDE', 'LONGITUDE']]
business_loc=business_loc.dropna(axis=0)
for i in range(0, 1085397):
    if(float(business_loc.loc[i].at['ZIP CODE'])<600007 or float(business_loc.loc[i].at['ZIP CODE'])>60827):
        business_loc.drop(i)
business_loc.to_csv('/Users/akhilnallacheruvu/Desktop/Business_Lats.csv')


# In[11]:


business_loc=pd.read_csv('/Users/akhilnallacheruvu/Desktop/Business_Lats.csv')


# In[12]:


business_loc=business_loc[['DOING BUSINESS AS NAME','LATITUDE', 'LONGITUDE']]
business_loc.to_csv('/Users/akhilnallacheruvu/Desktop/Business_Lats.csv')


# In[13]:


food=pd.read_csv('/Users/akhilnallacheruvu/Downloads/Food_Inspections.csv')


# In[14]:


food_loc=food[['DBA Name','Latitude','Longitude']]
food_loc=food_loc.dropna(axis=0)
for i in range(0, 244555):
    if(float(food_loc.loc[i].at['ZIP CODE'])<600007 or float(food_loc.loc[i].at['ZIP CODE'])>60827):
        food_loc.drop(i)
food_loc.to_csv('/Users/akhilnallacheruvu/Desktop/Food_Lats.csv')

