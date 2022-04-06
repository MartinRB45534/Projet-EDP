from Projet_2D.matrices_elementaires import matrices_elementaires
import numpy as np
from scipy import sparse

def matrice_rigidite(x,y,triangles):
    M_rig = np.zeros((len(x),len(x)))
    for tri in triangles:
        M_rig_loc = matrices_elementaires(np.array([x[tri[0]-1],y[tri[0]-1]]),np.array([x[tri[1]-1],y[tri[1]-1]]),np.array([x[tri[2]-1],y[tri[2]-1]]))
        for i in range(3):
            for j in range(3):
                M_rig[tri[i]-1,tri[j]-1] += M_rig_loc[i,j]

    return M_rig