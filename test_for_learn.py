# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:55:16 2020
@author: Jiaming Wang
"""

# =============================================================================
# a=np.array([[1,2],
#             [3,4],
#             [5,6]])
# b=np.array([[1, 2, 3],
#             [4, 5, 6]])
# 
# c=np.ones((3,4),dtype=np.float64)
# d=np.ones((5,6),dtype=np.float64)
# h = sp.linalg.norm(b)
# =============================================================================

# =============================================================================
# Hami = np.empty([2**5,2**5])
# A = np.empty([1,2**5],dtype=np.int64)
# a=0
# i=0
# while a<2**5:
#     while i<5:
#         j=(i+1)%N
#         if(A[i]==A[j]):
#             Hami[a,a]  = Hami[a,a] + 1/4
# =============================================================================
import numpy.matlib
import numpy as np
c = np.eye(2)
d = np.eye(2)
e = np.eye(2)
a = np.array([[3,1],[0,2]])
b = np.array([[1,-1],[0,1]])
c = np.dot(a, b)#
d = np.linalg.inv(b)
e = np.dot(d,c)
print(e)


#print(np.dot(a,b))

