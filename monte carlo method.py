#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
import math as mt
import numpy as np
input_number = input('input number of dots :')
number_of_dots =int(input_number)
x = np.random.uniform(low=-1,high=1,size=[number_of_dots, 1])
y = np.random.uniform(low=-1,high=1,size=[number_of_dots, 1])
circle = pow(x,2)+pow(y,2)<=1
MC_pi = 4*np.sum(circle)/number_of_dots
error = abs(mt.pi - MC_pi)
print('error is : ', error , 'pi by Monte carlo : ', MC_pi , 'for number of dots',number_of_dots , 'pi value', mt.pi )

plt.figure(figsize=(10,10))
x_inside = x[circle] 
y_inside = y[circle]
plt.scatter (x,y,s=1)
plt.title('Monte carlo : finding pi')
plt.scatter(x_inside ,y_inside,s=1,color='#b33653' )
plt.savefig('D:\\1\\MonteCarlo finding pi.png', dpi=500)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




