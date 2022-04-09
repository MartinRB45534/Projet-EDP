import numpy as np
import scipy as sp
from scipy import integrate
from Projet_2D.phi import cree_phis

def matrice_f(x,y,triangles,f,):
    M_f = np.zeros(len(x))
    for tri in triangles:
        phis = cree_phis(np.array([x[tri[0]-1],y[tri[0]-1]]),np.array([x[tri[1]-1],y[tri[1]-1]]),np.array([x[tri[2]-1],y[tri[2]-1]]))
        for i in range(3):
            def a_integrer(y,x):
                return f(x,y)*phis[i](x,y)
            contribution = integrate.dblquad(a_integrer,min(x[tri[0]-1],x[tri[1]-1],x[tri[2]-1]),max(x[tri[0]-1],x[tri[1]-1],x[tri[2]-1]),min(y[tri[0]-1],y[tri[1]-1],y[tri[2]-1]),max(y[tri[0]-1],y[tri[1]-1],y[tri[2]-1]))
            print(tri,contribution)
            M_f[tri[i]-1] = contribution[0]
    return M_f
        