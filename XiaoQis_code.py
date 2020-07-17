# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 15:07:20 2020
@author: Jiaming Wang
"""
import numpy as np
import scipy as sp
np.set_printoptions(threshold=np.inf)
from scipy import sparse
from scipy.linalg import eigh_tridiagonal as tqli
from scipy.linalg import norm
import time
from scipy.sparse.linalg import eigsh

def generate_map():
    matrix_basis=[]
    basis_matrix={}
    k1=-1
    for j in range(2<<(n-1)):
        S=sum((j>>k)&1 for k in range(n))
        if S==n//2:
            k1+=1
            matrix_basis.append(j)
            basis_matrix[j]=k1
    return matrix_basis,basis_matrix

def generate_hm():
    hm=sparse.lil_matrix((matrix_dim,matrix_dim))
    for j in range(matrix_dim):
        j1=matrix_basis[j]
        hm[j,j]=sum((float((j1>>k)&1)-1/2)*(float((j1>>((k+1)%n))&1)-1/2) for k in range(n))
        for k in range(n):
            if ((j1>>k)&1)+((j1>>((k+1)%n))&1)==1:
                j2=basis_matrix[j1^(1<<k)^(1<<((k+1)%n))]
                hm[j,j2]=1/2
    return hm

def hm_j2():
    hm_j2=sparse.lil_matrix((matrix_dim,matrix_dim))
    for j in range(matrix_dim):
        j1=matrix_basis[j]
        hm_j2[j,j]=sum((float((j1>>k)&1)-1/2)*(float((j1>>((k+2)%n))&1)-1/2) for k in range(n))  
        for k in range(n):
            if ((j1>>k)&1)+((j1>>((k+2)%n))&1)==1:
                j2=basis_matrix[j1^(1<<k)^(1<<((k+2)%n))]
                hm_j2[j,j2]=1/2
    return hm_j2

#return s^2 matrix
def total_spin_square():
    total_spin_square=sparse.lil_matrix((matrix_dim,matrix_dim))
    for j in range(matrix_dim):
        j1=matrix_basis[j]
        for k in range(n):
            for l in range(n):
                total_spin_square[j,j] = total_spin_square[j,j] + (float((j1>>k)&1)-1/2)*(float((j1>>l)&1)-1/2)
                if k==l :
                    total_spin_square[j,j] = total_spin_square[j,j] + 1/2
        for k in range(n):
            for l in range(n):
                if ((j1>>k)&1)+((j1>>l)&1)==1:
                    j2=basis_matrix[j1^(1<<k)^(1<<l)]
                    total_spin_square[j,j2]=total_spin_square[j,j2] + 1/2
    return total_spin_square

#cor_i,cor_j <= n
def correlation_function(cor_i,cor_j):
    cor_fun=sparse.lil_matrix((matrix_dim,matrix_dim))
    for j in range(matrix_dim):
        j1=matrix_basis[j]
        cor_fun[j,j]=(float((j1>>((cor_i)%n))&1)-1/2)*(float((j1>>((cor_j)%n))&1)-1/2)
        if ((j1>>((cor_i)%n))&1)+((j1>>((cor_j)%n))&1)==1:
            j2=basis_matrix[j1^(1<<((cor_i)%n))^(1<<((cor_j)%n))]
            cor_fun[j,j2]=1/2
    return cor_fun

if __name__ == '__main__':
    t1=time.time()
    cor_20=[]
    r_20=[]
    n=20
    for r in range(1,int(n/2+1)):
        r_20.append(r)
        print('lanzcos J1_J2 r:',r)
        matrix_basis,basis_matrix=generate_map()
        matrix_dim=np.size(matrix_basis)
        J2=0.1
        hm_j1_j2=generate_hm() + J2*hm_j2()
        correlation_matrix=correlation_function(0,r)
        eig_j1j2, vec_j1j2 = eigsh(hm_j1_j2, k=1, which='SA')
        cor_20.append(vec_j1j2[:,0]@correlation_matrix@vec_j1j2 * ((-1)**r) *r)
    t2=time.time()
    print("Time Spent=",t2-t1,"s")
