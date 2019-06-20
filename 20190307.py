#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=3
b=5
a+b


# In[2]:


import requests
c = requests.get('https://www.must.edu.tw/')
print(c.text)


# In[4]:


from skimage import io,data
img=data.astronaut()
dst=io.imshow(img)
io.show()


# In[ ]:





# In[ ]:




