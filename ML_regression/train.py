import csv
import numpy as np


traindata = open("data/train.csv",'r')

traindata = csv.reader(traindata, delimiter=',')


data = []
for _ in range(18):
    data.append([])


for i,rows in enumerate(traindata):
    if i!=0:
        for j in range(3,27):
            if rows[j]=="NR":
                data[i%18-1].append(float(0))
            else:
                data[i%18-1].append(float(rows[j]))

x=[]
y=[]



for i in range(12):
    for j in range(471):
        x.append([])
        for t in range(18):
            for s in range(9):
                x[471*i+j].append(data[t][480*i+j+s])
        y.append(data[9][480 * i + j + 9])

x=np.array(x)
y=np.array(y)
print(x.T.shape,x.shape)
x=np.concatenate((np.ones((x.shape[0],1)),x),axis=1)
w = np.zeros((x.shape[1]))
lr=10
s_gra=0
repeat=10000
cost_=np.load("cost_others.npy")
cost_train=0
h = x.dot(w)
print(y.shape,h.shape)
for _ in range(repeat):
    h=x.dot(w)
    loss = h-y
    cost = np.sum(loss**2) / len(x)
    cost_a  = np.sqrt(cost)
    gra = x.T.dot(loss)
    s_gra +=gra**2
    w = w - (lr/np.sqrt(s_gra))*gra
    print("interation:{},cost:{}".format(_,cost_a))
    cost_train=cost_a

cost_=np.hstack( (cost_,cost_train))
# save model
np.save('model.npy',w)
np.save('cost_others.npy',cost_)