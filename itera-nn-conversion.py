X=[]
Y=[]
Z=[]
I=[]
w=[[0.2,-0.3],[0.4,0.1],[-0.5,0.2],[-0.3,-0.2]]
teta=[-0.4,0.2,0.1]
erroroculto=[]
smi4=0.0
smi5=0.0
smi6=0.0
O=[]

l = input("inserta el label: ")

import numpy as np

def sigmoid(y):
    return (1.0)/(1.0+np.exp(-y))


file=open('datos.txt','r')
lineas=file.readlines()
for li in range(len(lineas)):
    x=(lineas[li])
    Y.append(x)
    file.close()

"""for x in range(len(open("datos.txt").readlines())):"""
x1=0
x2=1

for x in range(0,1):
    for y in range(len(Y[x])):
        if(Y[x][y]!="," and Y[x][y]!="\n"):
            O.append(int(Y[x][y]))

while(x2<=41):
    for x in range(x1,x2):
        for y in range(len(Y[x])):
            if(Y[x][y]!="," and Y[x][y]!="\n"):
                X.append(int(Y[x][y]))
                I=X
                
    for x in range(3):
        smi4+= (w[x][0]*O[x])
        resul_smi4= smi4 + teta[0]
        smi5+= (w[x][1]*O[x])
        resul_smi5= smi5 + teta[1]

    I.append(resul_smi4)
    I.append(resul_smi5)
    
    for x in range(3,5):
        O.append(sigmoid(I[x]))

        
    resul_smi6=w[3][0]*O[3]+w[3][1]*O[4]+teta[2]

    I.append(resul_smi6)
    O.append(sigmoid(I[5]))
    #error que deriva del sigmoid
    err6=(O[5])*(1-O[5])*(X[2]-O[5])

    deltaw=[] 
    for x in range(3,5):
        erroroculto.append(O[x]*(1-O[x])*w[3][x-3]*err6)

            
    deltawp=[]
    for x in range(0,3):
        deltaw.append(l*(erroroculto[0])*(O[x]))
        deltawp.append(w[x][0]+deltaw[x])

    for x in range(0,3):
        deltaw.append(l*(erroroculto[1])*(O[x]))
        deltawp.append(w[x][1]+deltaw[x]) 


    deltaw.append(l*(err6)*O[3])
    deltaw.append(l*(err6)*O[4])
    deltawp.append(w[3][0]+deltaw[-2])
    deltawp.append(w[3][1]+deltaw[-2])
    
    dlt_tt=[]
    dlt_tt.append(l*err6)

    z=1
    while z>=0:
        dlt_tt.append(l*erroroculto[z])
        z=z-1

    ttprim=[]

    ttprim.append(teta[2]+dlt_tt[0])
    ttprim.append(teta[1]+dlt_tt[2])
    ttprim.append(teta[0]+dlt_tt[1])
    #siguiente iteracion teta
    teta=ttprim
   
    """print(dlt_tt)"""
    #Para utilizar el O con la siguiente iteracion
    U=[]
    for x in range(3,len(O)):
        U.append(O[x])

    O=U
    #siguiente iteracion de w
    w[0][0]=deltawp[0]
    w[0][1]=deltawp[1]
    w[1][0]=deltawp[2]
    w[1][1]=deltawp[3]
    w[2][0]=deltawp[4]
    w[2][1]=deltawp[5]
    w[3][0]=deltawp[6]
    w[3][1]=deltawp[7]

    X=[]
    x1=x2
    x2+=1

print(O[-1])
print(err6)