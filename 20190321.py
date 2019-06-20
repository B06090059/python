#!/usr/bin/env python
# coding: utf-8

# In[7]:


x,y,z = 3,4,5
x +=1
y*=2
z **=3
print(x,y,z)


# In[8]:


import math
d=math.sqrt(((3+4+5)/2)*(((3+4+5)/2)-3)*(((3+4+5)/2)-4)*(((3+4+5)/2)-5))
print(d)


# In[9]:


import math
a,b,c=3,4,5
s=(a+b+c)/2
d=math.sqrt(s*(s-a)*(s-b)*(s-c))


# In[10]:


x=254
print(type(x))
id(x)


# In[11]:


x='write'
print(type(x))
id(x)


# In[12]:


import math
print((4.5*4.5*math.pi*4.5)/3)


# In[13]:


x=16
y=3
print(x/y)
print(x//y)
print(x%y)


# In[14]:


x=10
print(20==20)
y=20
print(x==y)
x=y
print(x)


# In[15]:


x=3.141592627
print(x-3.14)


# In[16]:


y=2010
print(y%4==0 and y%100!=0 or y%400==0)
y=2012
print(y%4==0 and y%100!=0 or y%400==0)
y=2000
print(y%4==0 and y%100!=0 or y%400==0)


# In[17]:


x=12
y=float(x)+0.5
print(y)
print(int('123'))
print(float('123'))
print(int(123.333))
x=10*3.25
y=200*200
s='the value of x is'+str(x)+'and y is '+str(y)
s1='the value of x is'+repr(x)+'and y is '+repr(y)
print(s)
print(s1)


# In[21]:


import math
print(math.pi)
print(math.pow(2,3))
print(8.3*10.58*math.sin(37.0/180*math.pi)/2)
print(math.sqrt(25))


# In[19]:


import math
r=input("請輸入數字")
a=float(r)*float(r)*math.pi
print("園面積",a)


# In[ ]:




