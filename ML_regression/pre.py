import numpy as np
import csv

text = open("data/ans.csv","r")
ans=csv.reader(text)

ansdata=[]
for i,data in enumerate(ans):
    if i!=0:
        ansdata.append(float(data[1]))
text.close()
ansdata=np.array(ansdata)


text = open("data/prediction.csv","r")
ans=csv.reader(text)

predata=[]
for i,data in enumerate(ans):
    if i!=0:
        predata.append(float(data[1]))
text.close()
predata=np.array(predata)
pre = np.load('pre.npy')
pre=np.hstack((pre,np.sqrt(np.mean((ansdata-predata)**2))))
print(np.sqrt(np.mean((ansdata-predata)**2)))

np.save("pre.npy",pre)