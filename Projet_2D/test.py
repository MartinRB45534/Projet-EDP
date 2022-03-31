from Projet_2D.gmsh_loader import readmsh

from matplotlib import mlab
import matplotlib.pyplot as plt

x,y,z,ref,triangle,NumDom,nbnoeud,nbelt = readmsh("Projet_2D/cylinder.msh")

fig = plt.figure()
ax = plt.subplot()
ax.plot(x, y, 'b.')
plt.show()