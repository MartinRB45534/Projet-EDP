import numpy as np

def dirichlet(x,y,rig,f):
    x_=x
    y_=y
    rig_=rig
    f_=f
    for i in range(len(x)-1,-1,-1):
        if x[i]==min(x) or x[i]==max(x) or y[i]==min(y) or y[i]==max(y):
            x_=np.delete(x_,i,0)
            y_=np.delete(y_,i,0)
            rig_=np.delete(rig_,i,0)
            rig_=np.delete(rig_,i,1)
            f_=np.delete(f_,i,0)

    return x_,y_,rig_,f_