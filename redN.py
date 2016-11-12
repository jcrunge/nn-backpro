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
erroroculto=[]
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

err6=(O[5])*(1-O[5])*(X[2]-O[5])

l = input("inserta el label: ")

for x in range(3,5):
    erroroculto.append(O[x]*(1-O[x])*w[3][x-3]*err6)

deltaw=[] 
deltawp=[]
for x in range(0,3):
    deltaw.append(l*(erroroculto[0])*(O[x]))

for x in range(0,3):
    """deltawp.append(w[3][0]+deltaw[x])"""
    deltaw.append(l*(erroroculto[1])*(O[x]))	

print(deltaw)
print("error en la capa oculta", erroroculto)

print(I)
print(O)

