#create a list to enter marks
l=[]
for i in range(1,11):
    print("enter marks:")
    l.append(i)
import matplotlib
import pyplot as plt
import numpy as np
fig,ax= plt.suplots(figsize=(7,3))
ax.hist(a,bins=l)
plt.show()