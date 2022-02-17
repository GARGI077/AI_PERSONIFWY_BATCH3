# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 00:14:27 2022

@author: GARGI SINGH
"""

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)


a = np.array([[1, 2, 3], [4, 5, 6]])

for x in a:
  for y in x:
    print(y)