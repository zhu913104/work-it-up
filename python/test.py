import time
t = time.time()
for x in range(1000000):
    print(x)
print(time.time()-t)