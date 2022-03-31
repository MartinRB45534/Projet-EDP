from Projet_2D.gmsh_loader import readmsh

from matplotlib import mlab
import matplotlib.pyplot as plt

x,y,z,ref,triangle,NumDom,nbnoeud,nbelt = readmsh("Projet_2D/cylinder.msh")

fig = plt.figure()
ax = plt.subplot()
ax.plot(x, y, 'b.')
print(triangle)
for tri in triangle:
    x_ = [x[tri[i]-1] for i in [0,1,2,0]]
    y_ = [y[tri[i]-1] for i in [0,1,2,0]]
    ax.plot(x_,y_)
plt.show()