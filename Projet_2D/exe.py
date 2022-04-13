#import imp
from Projet_2D.gmsh_loader import readmsh
from Projet_2D.matrice_rigidite import matrice_rigidite
from Projet_2D.matrice_f import matrice_f
from Projet_2D.dirichlet import dirichlet

import matplotlib.pyplot as plt
import numpy as np

# def f(x,y):
#     return 1

x,y,z,ref,triangle,NumDom,nbnoeud,nbelt = readmsh("Projet_2D/geomCarre.msh")

fig = plt.figure()
ax = plt.subplot()
ax.plot(x, y, 'b.')
# print(triangle)
# print(NumDom)
for tri in triangle:
    x_ = [x[tri[i]-1] for i in [0,1,2,0]]
    y_ = [y[tri[i]-1] for i in [0,1,2,0]]
    ax.plot(x_,y_)
ax.axis('scaled')
print("Fermer la figure du maillage pour voir la suite.")
plt.show()
rig = matrice_rigidite(x,y,triangle)
plt.figure()
plt.pcolor(rig)
plt.gca().invert_yaxis()
plt.colorbar()
plt.title('Matrice de Rigidité ')
print("Fermer la figure de la matrice de rigidité pour voir la suite.")
plt.show()

# inv_rig = np.linalg.inv(rig)
# print(inv_rig)

# print("Conditionnement :")
# print(np.linalg.cond(rig))
def f(x,y):
    return -2*np.power(np.pi,2)*np.sin(np.pi*x/2)*np.sin(np.pi*y/2)/4
def solution_analytique(x,y):
    return np.sin(np.pi*x/2)*np.sin(np.pi*y/2)
mat_f = matrice_f(x,y,triangle,f)
# print(mat_f)
# U=np.linalg.solve(rig,mat_f)
# print(U)

x_,y_,rig_,mat_f_=dirichlet(x,y,rig,mat_f)
U_=np.linalg.solve(rig_,-mat_f_)
#print(U_)

X = np.linspace(0,2,101)
Y = np.linspace(0,2,101)
X_,Y_=np.meshgrid(X,Y)
sol = solution_analytique(X_,Y_)
fig = plt.figure()

ax = plt.axes(projection ='3d')
ax.plot_surface(X_,Y_,sol,alpha=0.5)
ax.scatter(x_ ,y_, U_,marker='o',color='r')
ax.set_title('Solution analytique et solution du problème')
plt.show()