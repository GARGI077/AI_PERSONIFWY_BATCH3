# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 15:08:18 2022

@author: GARGI SINGH
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

hsplitArray=np.hsplit(arr,3)
print(hsplitArray)

