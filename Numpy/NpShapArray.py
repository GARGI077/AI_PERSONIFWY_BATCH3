# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 00:12:17 2022

@author: GARGI SINGH
"""

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

newarr = arr.reshape(-1)

print(newarr)