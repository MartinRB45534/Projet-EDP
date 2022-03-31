from numpy import *

from scipy import *


# Fonction de lecture du maillage

def  readmsh(filename) :

  f=open(filename,'r')
  i=0
  while f.readline().split()[0] != "$Nodes": #On va jusqu'aux noeuds
    pass
  line=f.readline()
  data = line.split()
  nbnoeud=int(data[0])
  x=zeros(nbnoeud,double)
  y=zeros(nbnoeud,double)
  z=zeros(nbnoeud,double)
  ref=zeros(nbnoeud,int)
  print(nbnoeud)
  for i in range(nbnoeud) :
    line=f.readline()
    data = line.split()
    ref[i]=int(data[0])
    x[i]=double(data[1])
    y[i]=double(data[2])
    z[i]=double(data[3])
  while f.readline().split()[0] != "$Elements": #On va jusqu'aux éléments
    pass
  line=f.readline()
  data = line.split()
  nbelt=int(data[0])
  triangle=zeros((nbelt,4),int)
  NumDom=zeros(nbelt,int)
  print(nbelt)
  for i in range(nbelt) :
    line=f.readline()
    data = line.split()
    NumDom[i]=int(data[0])
    triangle[i,0]=int(data[1])
    triangle[i,1]=int(data[2])
    triangle[i,2]=int(data[3])
    triangle[i,3]=int(data[4])

  f.close() 
  return x,y,z,ref,triangle,NumDom,nbnoeud,nbelt