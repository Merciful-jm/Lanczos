# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:55:16 2020
@author: Jiaming Wang
"""
import numpy as np
import scipy as sp


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
# =============================================================================
# L=8
# J=1.0
# shape = (L, L)
# spins = np.full(shape,1)
# S= -np.sum(    J * spins * np.roll(spins, 1, axis=0) +    J * spins * np.roll(spins, -1, axis=0) +    J * spins * np.roll(spins, 1, axis=1) +    J * spins * np.roll(spins, -1, axis=1)  )/2
# =============================================================================
