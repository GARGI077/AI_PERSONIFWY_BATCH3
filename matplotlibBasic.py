# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 01:17:19 2022

@author: GARGI SINGH
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#plotting values
a=[7,9,5,4,2]
plt.plot(a)
plt.show()

x=[2,5,7,6]
y=[12,34,44,78]
#plt.plot(x, y)
plt.scatter(x, y)
plt.show()

n=50
l=np.random.rand(n)
m=np.random.rand(n)
color=np.random.randn(n)
area=np.pi*(15*np.random.rand(n))**2

plt.scatter(x, y, c=color, s=area,alpha=0.5)
plt.show()