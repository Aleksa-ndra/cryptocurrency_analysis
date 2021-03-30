#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import requests


# In[4]:


req = requests.get("https://bitbay.net/API/Public/BTCPLN/orderbook.json")
req.status_code


# In[6]:


print(req.url)


# In[7]:


req.text


# In[ ]:

print('New row to train GIT.')


