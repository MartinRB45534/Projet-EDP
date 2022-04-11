import imp
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
from Projet_2D.dirichlet import dirichlet

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
plt.show()
# plt.figure()
# X = np.linspace(min(x), max(x), 101)
# Y = np.linspace(min(y), max(y), 101)
# X, Y = np.meshgrid(X, Y)
# Z = 2*np.cos(10*X)*np.sin(10*Y) + np.sin(10*X*Y)
# plt.pcolor(X, Y, Z)
# plt.show()
inv_rig = np.linalg.inv(rig)
print(inv_rig)

# print(np.dot(inv_rig,rig))

# def f(x,y):
#     return 1

# print("Matrice f")
# print(matrice_f(x,y,triangle,f))


print("Conditionnement :")
print(np.linalg.cond(rig))
def f(x,y):
    return -2*np.power(np.pi,2)*np.sin(np.pi*x/2)*np.sin(np.pi*y/2)/4
def solution_analytique(x,y):
    return np.sin(np.pi*x/2)*np.sin(np.pi*y/2)
mat_f = matrice_f(x,y,triangle,f)
# print(mat_f)
pkl.dump(mat_f,open(os.path.abspath(".")+"/matrice_Carre_f.p",'wb'))
U=np.linalg.solve(rig,mat_f)
print(U)
# fig = plt.figure()
# ax = plt.axes(projection ='3d')
# ax.scatter(x ,y, U, marker='o')
# ax.set_title('Avec la vraie f')
# plt.show()


x_,y_,rig_,mat_f_=dirichlet(x,y,rig,mat_f)
U_=np.linalg.solve(rig_,-mat_f_)
print(U_)
# fig = plt.figure()
# ax = plt.axes(projection ='3d')
# spline = interpolate.bisplrep(x_,y_,U_)
# print(interpolate.bisplev(spline[0],spline[1],spline[2]))

# X_,Y_=np.meshgrid(spline[0],spline[1])
# plt.plot(X_,Y_,spline[2], marker='o')
# plt.show()
X = np.linspace(0,2,101)
Y = np.linspace(0,2,101)
X_,Y_=np.meshgrid(X,Y)
sol = solution_analytique(X_,Y_)

fig = plt.figure()
#plt.hold(True)
ax = plt.axes(projection ='3d')
ax.plot_surface(X_,Y_,sol,alpha=0.5)
ax.scatter(x_ ,y_, U_,marker='o',color='r')
ax.set_title('Avec la vraie f')
plt.show()

# def f(x,y):
#     return 2*cos(10*x)*sin(10*y) + sin(10*x*y)
# mat_f = matrice_f(x,y,triangle,f)
# # print(mat_f)
# pkl.dump(mat_f,open(os.path.abspath(".")+"/matrice_Carre_f.p",'wb'))
# U=np.linalg.solve(rig,-mat_f)
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