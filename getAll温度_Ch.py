import numpy as np
import os 
import matplotlib.pyplot as plt

#cat
t= np.loadtxt('readT.in')
n = np.shape(t)[0]
print n
for i in range(n):
    t[i] = round(t[i],2)

reade=open('reade.in')
e=float(reade.read())
reade.close()
F = "CH3de"+str(e)+".dat"

for i in t:
    os.chdir("t"+str(i)+"e"+str(e))
    os.system('cat ch_3d.dat >> ../'+F)
    os.chdir("..")

#load
C = np.loadtxt(F)
x=C[:,0]
y=C[:,1]
chmax = np.max(y)
y = y/chmax
C[:,1]=y
#plt
fg1=plt.figure()
plt.title('3DCH Index_e='+str(e))
plt.xlabel('T / J')
plt.grid(axis="x")
plt.xticks(C[:,0])
plt.plot(x,y)
plt.scatter(x,y)
plt.savefig('fig3DcHe'+str(e)+'.png',format='png')
plt.show(fg1)

np.savetxt(F,C,fmt='%.5f')
