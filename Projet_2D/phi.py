import numpy as np

def cree_phis(P1,P2,P3):
    """Génère les trois fonctions phi qui sont non-nulles sur le triangle"""
    A=np.array([[1,1,1],[P1[0],P2[0],P3[0]],[P1[1],P2[1],P3[1]]])
    invA = np.linalg.inv(A)
    phis=[]
    for i in range(3):
        def phi(x,y):
            f"""
            La fonction phi{i+1}, fonction affine sur le triangle, qui vaut 1 sur le sommet P{i+1} et 0 sur les deux autres.
            """
            l=np.dot(invA,np.array([1,x,y]))
            return l[i] #Vu qu'on n'intègre que sur le triangle, probablement mieux et sans impact
        phis.append(phi)
    return phis