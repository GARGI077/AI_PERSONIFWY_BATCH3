# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 20:38:42 2022

@author: GARGI SINGH
"""

import numpy as np

#1-D Array

arr=np.array([1,2,3,4,5,6,7,8])
print ("1-D Array :: ",arr)
print (type(arr))

#2-D Array

a=np.array([[1,2,3],[4,5,6]])
print("2-D Array \n ",a)

#3-d Array

array=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print("3-D Array \n",array)


#minimum dimensions

ar=np.array([1,2,3,4],ndmin=2)
print(ar)