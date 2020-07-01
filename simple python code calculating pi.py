#!/usr/bin/env python
# coding: utf-8

# In[14]:


months = ['jan','feb','mar','apr']
sun    = [22.8 , 33.8 , 34 , 23]
for i , t in sorted(zip(sun,months), reverse = True):
    print('{}:{:5.1f} hrs'.format(i,t))


# In[24]:


# ------ fizz buzz fizzbuzz game 

fb=[]
for i in range(31):
    if i==0:
        fb.append(0)
    elif i%3 and i%5 ==0:
        fb.append('fizzbuzz')
    elif i%3 == 0 :
        fb.append('fizz')
    elif i%5 == 0:
        fb.append('buzz')
    else:
        fb.append(i)
print(fb)










# In[96]:


import math as mt
import numpy as np

def seq(n):
    pii=0
    for i in range(n):
        pii += mt.sqrt(12) * pow(-1,i) / ((2*i + 1)*pow(3,i))
    return pii
print ('the value of pi is : ',seq(3),'the error is : ',abs(seq(3)-mt.pi))







# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[69]:





# In[74]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




