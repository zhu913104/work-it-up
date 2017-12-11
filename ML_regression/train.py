import csv
import numpy as np


data = open("data/train.csv",'r')

data = csv.reader(data)


x = []
for _ in range(18):
    x.append([])
for i,rows in enumerate(data):
    if i!=0:
        for j in range(3,27):
            if rows[j]=="NR":
                x[i%18-1].append(0)
            else:
                x[i%18-1].append(rows[j])
x= np.array(x)
