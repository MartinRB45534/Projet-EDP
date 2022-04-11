from Projet_2D.gmsh_loader import readmsh
from Projet_2D.matrice_rigidite import matrice_rigidite
from Projet_2D.matrice_f import matrice_f

from matplotlib import mlab
from math import cos, sin
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import pickle as pkl
import os

def f(x,y):
    return 1

x,y,z,ref,triangle,NumDom,nbnoeud,nbelt = readmsh("Projet_2D/test.msh")

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
plt.show()
plt.figure()
X = np.linspace(min(x), max(x), 101)
Y = np.linspace(min(y), max(y), 101)
X, Y = np.meshgrid(X, Y)
Z = 2*np.cos(10*X)*np.sin(10*Y) + np.sin(10*X*Y)
plt.pcolor(X, Y, Z)
plt.show()
inv_rig = np.linalg.inv(rig)
print(inv_rig)

# print(np.dot(inv_rig,rig))

print("Conditionnement :")
print(np.linalg.cond(rig))
def f(x,y):
    return -1
mat_f = matrice_f(x,y,triangle,f)
# print(mat_f)
pkl.dump(mat_f,open(os.path.abspath(".")+"/matrice_Carre_f.p",'wb'))
U=np.linalg.solve(rig,mat_f)
print(U)
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.scatter(x ,y, U, marker='o')
ax.set_title('Avec la vraie f')
plt.show()

# def f(x,y):
#     return 2*cos(10*x)*sin(10*y) + sin(10*x*y)
# mat_f = matrice_f(x,y,triangle,f)
# # print(mat_f)
# pkl.dump(mat_f,open(os.path.abspath(".")+"/matrice_Carre_f.p",'wb'))
# U=np.linalg.solve(rig,mat_f)
# print(U)
# # fig = plt.figure()
# # ax = plt.axes(projection ='3d')
# # ax.plot_surface(x, y, U, cmap ='viridis', edgecolor ='green')
# # ax.set_title('Avec la vraie f')
# plt.show()
# def f(x,y):
#     return 1
# mat_f = matrice_f(x,y,triangle,f)
# # print(mat_f)
# pkl.dump(mat_f,open(os.path.abspath(".")+"/matrice_Carre_f_1_simpl.p",'wb'))
# U=np.linalg.solve(rig,mat_f)
# print(U)
# # fig = plt.figure()
# # ax = plt.axes(projection ='3d')
# # ax.plot_surface(x, y, U, cmap ='viridis', edgecolor ='green')
# # ax.set_title('Avec f=1')
# # plt.show()