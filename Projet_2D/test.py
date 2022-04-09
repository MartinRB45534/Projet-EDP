from Projet_2D.gmsh_loader import readmsh
from Projet_2D.matrice_rigidite import matrice_rigidite
from Projet_2D.matrice_f import matrice_f

from matplotlib import mlab
import matplotlib.pyplot as plt
import numpy as np
import pickle as pkl
import os

def f(x,y):
    return 1

x,y,z,ref,triangle,NumDom,nbnoeud,nbelt = readmsh("Projet_2D/cylinder.msh")

fig = plt.figure()
ax = plt.subplot()
ax.plot(x, y, 'b.')
# print(triangle)
# print(NumDom)
for tri in triangle:
    x_ = [x[tri[i]-1] for i in [0,1,2,0]]
    y_ = [y[tri[i]-1] for i in [0,1,2,0]]
    ax.plot(x_,y_)
rig = matrice_rigidite(x,y,triangle)
print(rig)
mat_f = matrice_f(x,y,triangle,f)
print(mat_f)
pkl.dump(mat_f,open(os.path.abspath(".")+"/matrice_cylinder_f_1_verif.p",'wb'))
ax.axis('scaled')
plt.show()