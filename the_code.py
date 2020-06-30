#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
Sun    = [44.7 , 65.4, 101.7, 148.3, 170.90, 171.4, 176.7, 186.1, 133.9, 105.4, 59.6, 45.8]
print('Temprature in the year table')
for i in range(0,12,1) :
    print(months[i],': ', Sun[i] ,' hrs')
plt.bar(months,Sun, label=['months','avrg Sun Temprature'])
plt.xticks(rotation='vertical')
plt.title('Temprature in the year')
plt.show()
plt.plot(months,Sun,marker='.',markersize=20)
plt.xticks(rotation='vertical')
plt.grid()
#plt.legend()
plt.show()
plt.boxplot(Sun)
plt.grid()
plt.show()


# In[ ]:




