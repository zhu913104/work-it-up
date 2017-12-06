
"""
Created on Wed Nov 22 07:24:46 2017

@author: jason
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




pokemondata=pd.read_csv('pokemon.csv', sep=',',header=None)

cp = pokemondata.values[1:39,2]
cp_new = pokemondata.values[1:39,14]

cp = np.array([cp],dtype = np.float16).reshape([cp.shape[0]])
cp_new = np.array([cp_new],dtype = np.float16).reshape([cp_new.shape[0]])

from sympy import *
def linear_regression(X, Y):
    w, b = symbols('w  b')
    print(w)
    residual = 0
    #residualSum 求殘差
    for i in range(len(X)):
        residual += (Y[i] - (w * X[i] + b)) ** 2
    #展開觀看方程式內容
    print ('expand',expand(residual))
    #對a微分

    f1 = diff(residual, w)
    #對b微分

    f2 = diff(residual, b)
    print ('w',f1)
    print ('b',f2)
    #求聯立方程式的解

    res = solve([f1, f2], [w, b])
    print(res)
    return res[w], res[b]

print(cp,cp_new)
w, b = linear_regression(cp, cp_new)
X = np.linspace(0,400)
f = lambda x: x*w+b
Y = f(X) 

plt.scatter(cp,cp_new,s=10,c='r')
plt.plot(X, Y, 'b') # render blue line
plt.show()