# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 00:17:20 2022

@author: GARGI SINGH
"""

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)


a1 = np.array([[1, 2], [3, 4]])

a2 = np.array([[5, 6], [7, 8]])

a= np.concatenate((a1, a2),axis=1)

print(a)
