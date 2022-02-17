# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 00:02:42 2022

@author: GARGI SINGH
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)