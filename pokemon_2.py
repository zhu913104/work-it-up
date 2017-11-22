# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 07:24:46 2017

@author: jason
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


pokemondata=pd.read_csv('pokemon.csv', sep=',',header=None)


pop = np.array([pokemondata.values[1:39,2],pokemondata.values[1:39,14]])




plt.scatter(pop[0,:],pop[1,:],s=10,c='r')
plt.show()