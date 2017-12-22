import numpy  as np
import matplotlib.pyplot as plt


pre = np.load('pre.npy')
cost_=np.load("cost_others.npy")

modle_name=["PM2.5 in 6hr","PM2.5 in 7hr","PM2.5 in 8hr","PM2.5 in 9hr","All material in 9hr"]

xs=[i for i,_ in enumerate(modle_name)]

plt.xticks([i for i,_ in enumerate(modle_name)],modle_name)
plt.plot(xs,pre,label="test")
plt.plot(xs,cost_,label="train")
plt.ylabel("LOSS VALUE", fontsize=16)
plt.xlabel("COMPLEX OF MODEL", fontsize=16)
plt.legend(loc=9, borderaxespad=0.)
plt.show()



