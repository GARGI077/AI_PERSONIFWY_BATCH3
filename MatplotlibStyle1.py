# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 01:56:52 2022

@author: GARGI SINGH
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#MatplotLib Style1
n=50
x=np.array([1,2,4,5])
y=np.array([23,12,45,32])
plt.plot(x,y,color='red',marker='*')
plt.plot(x,y)
plt.show()
