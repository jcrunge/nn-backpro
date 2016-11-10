import numpy as np

def sigmoid(y):
    return (1.0)/(1.0+np.exp(-y))

X=[1,0,1]
I=X
O=[1,0,1]
teta=[-0.4,0.2,0.1]
w=[[0.2,-0.3],[0.4,0.1],[-0.5,0.2],[-0.3,-0.2]]
smi4=0.0
smi5=0.0
smi6=0.0
"""sumamult=(w[0]*O[0])+(w[2]*O[1])+(w[4]*O[2])+teta[0]"""
for x in range(3):
    smi4+= (w[x][0]*O[x])
    resul_smi4= smi4 + teta[0]
    """O[x]=sigmoid(I[x])"""
    smi5+= (w[x][1]*O[x])
    resul_smi5= smi5 + teta[1]

I.append(resul_smi4)
I.append(resul_smi5)

for x in range(3,5):
    O.append(sigmoid(I[x]))

resul_smi6=w[3][0]*O[3]+w[3][1]*O[4]+teta[2]

I.append(resul_smi6)

O.append(sigmoid(I[5]))

print(I)
print(O)

