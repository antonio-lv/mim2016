#Solución del problema de control óptimo de una masa puntual
#Creado por Antonio Lamas Villar

#Importamos las librerías
import numpy as np
from numpy import linalg as alg
from numpy import matrix as mat
import matplotlib.pyplot as plt

n=10                     #Número de valores
m=1                      #Masa del objeto
A_v=np.zeros((n,n))      #Matriz de velocidades
A_p=np.zeros((n,n))      #Matriz de posiciones

#Definición de vectores de posiciones
p=np.array([0,0,0,0,0,0,0,0,0,1])[np.newaxis]
v=np.array([0,0,0,0,0,0,0,0,0,0])[np.newaxis]
#Transposición para hacerlo tipo matriz
p_c=p.T
v_c=v.T

#Relleno de los valores de la matriz según la ecuación
for i in range(0,10):
    for j in range(0,10):
        if(i-j)>=0:
            A_v[i,j]=1
            A_p[i,j]=(i-j)+0.5
        else:
            A_v[i,j]=0
            A_p[i,j]=0

#Creación y transposición del vector objetivo a lograr
y_obj_=np.array([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])[np.newaxis]
y_obj=y_obj_.T

#Creación de la matriz A global
A=np.concatenate((A_p,A_v),axis=0)
np.vstack((A_p,A_v))
#Creación de la pseudo-inversa
I=alg.pinv(A)
#Cálculo del vector de fuerzas
F=mat.dot(I,y_obj)

t=np.array([0,1,2,3,4,5,6,7,8,9,10])
p_graf=A_p*F
v_graf=A_v*F

p_graf=p_graf[np.newaxis]
p_graf=p_graf.T

plt.plot(t,p_graf)
#plt.plot(t,v_graf)

