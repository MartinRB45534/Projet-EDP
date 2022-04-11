from numpy import *

from scipy import *

def matrices_elementaires_masse(P1,P2,P3):
    M_masse = array([[1/12,1/24,1/24],[1/24,1/12,1/24],[1/24,1/24,1/12]])
    Aire2 = abs((P2[0]-P1[0])*(P3[1]-P1[1])-(P3[0]-P1[0])*(P2[1]-P1[1]))
    M_masse*=Aire2
    return M_masse

def matrices_elementaires(P1,P2,P3):
    C=array([[dot(P3-P1,P3-P1),-dot(P2-P1,P3-P1)],[-dot(P2-P1,P3-P1),dot(P2-P1,P2-P1)]])
    S1=array([[1,-1,0],[-1,1,0],[0,0,0]])/2
    S2=array([[2,-1,-1],[-1,0,1],[-1,1,0]])/2
    S3=array([[1,0,-1],[0,0,0],[-1,0,1]])/2
    Aire2 = abs((P2[0]-P1[0])*(P3[1]-P1[1])-(P3[0]-P1[0])*(P2[1]-P1[1]))
    M_rig = (C[0,0]*S1+C[0,1]*S2+C[1,1]*S3)/Aire2
    return M_rig