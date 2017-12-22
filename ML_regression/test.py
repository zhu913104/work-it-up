import csv
import numpy as np


testdata = open("data/test.csv",'r')
testdata = csv.reader(testdata, delimiter=',')

x_test=[]
for i,rows in  enumerate(testdata):
    if i%18==0:
        x_test.append([])
    for j in range(2,11):
        if rows[j]!="NR":
            x_test[i//18].append(float(rows[j]))
        else:
            x_test[i//18].append(float(0))
x_test=np.array(x_test)

x_test = np.concatenate((np.ones((x_test.shape[0],1)),x_test),axis=1)

print(x_test.shape)

w = np.load('model.npy')

ans=[]

for i in range(x_test.shape[0]):
    ans.append(["id_"+str(i)])
    a=w.dot(x_test[i])
    ans[i].append(a)

filename = open("data/prediction.csv","w+")
s = csv.writer(filename,delimiter=',',lineterminator='\n')
s.writerow(["id","value"])
for i in range(len(ans)):
    s.writerow(ans[i])
filename.close()