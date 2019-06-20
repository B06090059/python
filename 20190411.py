#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PYTHON物件
#list,tuple,dict,sets
list:[1,2,3]
tuple:(1,2,3)#不能改變其值
dict:{1:'apple',2:'banana',3:'orange'}
sets:{apple,banana,orange}


# In[4]:


#list串列
my_list0=[1,2,3]
print(my_list0)
my_list1=['python','js','sql']
print(my_list1[0])
my_list1.append('java')
print(my_list1)


# In[6]:


my_list1.insert(0,'c#')
print(my_list1)


# In[7]:


list2=['c#','pythin','js','sql','java']
#list長度
print(len(list2))
print(len(list2[1]))


# In[12]:


list3=['c#','python','js','sql','java']
list3.remove("js")
print(list3)
del list3[0]
print(list3)
del list3[-1]#最後一個
print(list3)


# In[13]:


print('java'in['python','js','c#'])


# In[14]:


a=[1,2]
print(a*5)


# In[16]:


a=[1,2,3,4,5,6,7,8,9]
b=a[0:3]#0到2
print(b)
c=a[0:9:2]#0-8間隔2
print(c)
del a[7:9]
print(a)
print(max(a))
print(min(a))
print(a.index(5))#索引值
print(a.count(1))#1出現幾次


# In[18]:


print(a)
a.reverse()
print(a)
a.sort
print(a)


# In[21]:


a=[123,'abc',[111,222],[333]]
print(a[0])
print(a[2][1])


# In[23]:


a=[111,222]+[333,444]+[555,666]
print(a)


# In[25]:


shoplist=['milk','egg','coffee','water']
for item in shoplist:
    print(item)


# In[26]:


alist=['python','js','c#']
atuple=('python','js','c#')
btuple=tuple(alist)
print(type(alist))
print(type(atuple))
print(btuple)


# In[27]:


ctuple=111,222,333
print(ctuple)
print(type(ctuple))


# In[29]:


alist=['python','js','c#']
adict={0:'python',1:'js',2:'c#'}
print(alist[0])
print(adict[0])
dict={'1st':'python','2nd':'js','3rd':'c#'}
print(dict['1st'])
       


# In[ ]:




