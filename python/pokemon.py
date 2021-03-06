# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 08:35:55 2017

@author: jason
"""
import csv
import numpy as np
import matplotlib.pyplot as plt

pokemondata = open("pokemon.csv",'r')

def get_cp(species):
    pop = np.vstack([np.vstack([np.array([row['cp'] if row["species"] == species else None,row["cp_new"] if row["species"] == species else None])])for row in csv.DictReader(pokemondata) ])
    return pop

cp = get_cp("Pidgey")

print(cp)

plt.scatter(cp[:,0],cp[:,1],s=10,c='r')


plt.show()
