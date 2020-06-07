#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy import cluster


# In[2]:


help(cluster)


# In[4]:


help()


# In[5]:


import scipy
scipy.info(cluster)


# In[6]:


scipy.source(cluster)


# In[8]:


## Exponential function
##special
from scipy import special
a=special.exp10(3)
print(a)


# In[10]:


b=special.exp2(3)
print(b)


# In[12]:


##trignometry function


# In[13]:


c=special.sindg(90)
print(c)


# In[14]:


d=special.cosdg(90)
print(d)


# # #integration function
#    
# 

# In[16]:


# genral inegration
from scipy import integrate
help(integrate.quad)


# In[18]:


i=scipy.integrate.quad(lambda x:special.exp10(x),0,1)
print(i)


# In[21]:


#double
e=lambda x,y: x*y**2
f=lambda x: 1
g=lambda x:-1
integrate.dblquad(e,0,2,f,g)


# # fourier transformation
# 

# In[26]:


from scipy.fftpack import fft,ifft
import numpy as np
x=np.array([1,2,3,4])
y=ifft(x)
print(y)


# # linear algebra

# In[27]:


#inverse of a matrix


# In[30]:


from scipy import linalg

a=np.array([[1,2],[3,4]])
b=linalg.inv(a)
print(b)


# # interpolation function

# In[33]:


import matplotlib.pyplot as plt
from scipy import interpolate
x=np.arange(5, 20)
y=np.exp(x/3.0)
f=interpolate.interp1d(x, y)
x1=np.arange(6, 12)
y1=f(x1)
plt.plot(x, y, 'o', x1, y1, '--')
plt.show()


# In[ ]:




