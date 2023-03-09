#!/usr/bin/env python
# coding: utf-8

# In[2]:


jovian.commit()


# In[1]:


import torch


# In[2]:


t1 = torch.tensor(4.)#tensor creation for single number (4. ) is shorthand for 
#(4.0)


# In[3]:


t1.dtype


# In[4]:


#veector 
t2=torch.tensor([1.,2,3,4])
t2


# In[5]:


#matrix
t3=torch.tensor([[5.,6],[6,7],[3,5],[12,3]])
t3


# In[6]:


t3.dtype


# In[7]:


#3 dimension array 
t4=torch.tensor([[[22,3,4,],[23,4,5],[4,55,6]],])
t4
# diffrence from list is that they must have a common length where as list can have any length irrespective of the previous row


# In[8]:


t1.shape


# In[10]:


print(t2)
t2.shape


# In[ ]:




