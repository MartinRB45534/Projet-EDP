# LGEP - departement MOCOSEM
# santandrea@lgep.supelec.fr

# Petit exemple de programmation de la methode des elements finis en Python
# Elements finis triangulaire du premier ordre
# Probleme de magnetostatique avec une formulation en potentiel vecteur magnetique A (Inconnue scalaire : composante en z de A) (Champ magnétique dans le plan xy)
# Fil de cuivre infiniment long parcouru par une densité de courant uniforme et constante dans le temps J0
# fichier de maillage necessaire fil.msh

# utilisation du module sparse de Scipy pour gerer les matrices creuses

from numpy import *
import pylab
import string, math
import time

from scipy import *
import scipy

from matplotlib import mlab
import matplotlib

from scipy.sparse import *
from scipy.sparse.linalg import cg

# Fonction de lecture du maillage

def  readmsh(filename) :

  f=open(filename,'r')

  line=f.readline()
  data = line.split()
  nbnoeud=int(data[0])
  nbelt=int(data[1])
  x=zeros(nbnoeud,double)
  y=zeros(nbnoeud,double)
  ref=zeros(nbnoeud,int)
  triangle=zeros((nbelt,3),int)
  NumDom=zeros(nbelt,int)
  print(nbnoeud)
  print(nbelt)
  for i in range(nbnoeud) :
    line=f.readline()
    data = line.split()
    x[i]=double(data[0])
    y[i]=double(data[1])
    ref[i]=int(data[2])

  for i in range(nbelt) :
    line=f.readline()
    data = line.split()
    triangle[i,0]=int(data[0])
    triangle[i,1]=int(data[1])
    triangle[i,2]=int(data[2])
    NumDom[i]=int(data[3])

  f.close() 
  return x,y,ref,triangle,NumDom,nbnoeud,nbelt

# Debut programme principal

# lecture du maillage

x,y,ref,triangle,NumDom,nbnoeud,nbelt = readmsh("fil.msh")

# Donnees physiques du problemes
J=array([1.e7, 0.])
mu0=4e-7*math.pi
mu=array([mu0, mu0])


t1 = time.clock()
# Solution d'un probleme de magnetostatique

MatMef = lil_matrix((nbnoeud,nbnoeud))
SdMembre = zeros(nbnoeud,double)
Az = zeros(nbnoeud,double)

xe=zeros((3,1),double)
ye=zeros((3,1),double)
InvJac=zeros((2,2),double)
MatElmt=zeros((3,3),double)
SdElmt=zeros(3,double)


# Gradient sur l'element de reference
Grad = matrix([[-1.,1.,0.],[-1.,0.,1.]])

# Boucle sur les elements

for ielt in range(nbelt) :

  # Donnees elementaires
  NumNoeuds = triangle[ielt][0:3]
  NumNoeuds=NumNoeuds-1
  idom = NumDom[ielt]-1

  for inoeud in range(3) :
    xe[inoeud]=x[NumNoeuds[inoeud]]
    ye[inoeud]=y[NumNoeuds[inoeud]]

  # Determinant et l'inverse de la matrice Jacobienne 
  DetJac = (xe[1]-xe[0])*(ye[2]-ye[0])-(xe[2]-xe[0])*(ye[1]-ye[0])
  InvJac = matrix([ [double(ye[2]-ye[0]) , double(-ye[1]+ye[0])] , [double(-xe[2]+xe[0]) , double(xe[1]-xe[0]) ] ])/DetJac

  #Calcul de la matrice elementaire de rigidite (integration analytique)
  MatElmt = (Grad.transpose()*(InvJac.transpose()*InvJac)*Grad)*double(DetJac/2./mu[idom])      
  SdElmt = ones(3,double)*J[idom]*DetJac/6.

  # Assemblage
  for inoeud in range(3) :
    SdMembre[NumNoeuds[inoeud]] =  SdMembre[NumNoeuds[inoeud]]+SdElmt[inoeud]
    for jnoeud in range(3) :
    	MatMef[NumNoeuds[inoeud],NumNoeuds[jnoeud]] =  MatMef[NumNoeuds[inoeud],NumNoeuds[jnoeud]]+MatElmt[inoeud,jnoeud]
  
# fin de boucle sur les elts

# Prise en compte des Conditions aux limites dirichlet homogene  

for inoeud in range(nbnoeud) :
    if (abs(ref[inoeud])==2) :
      MatMef[inoeud,inoeud]=MatMef[inoeud,inoeud]+1.e7
      SdMembre[inoeud]=0

tol = 1e-10

# inversion 
Az0 = zeros((nbnoeud),complex)
MatMefCsr = MatMef.tocsr()  
Sol=cg(MatMefCsr,SdMembre,Az0,1e-6,nbnoeud)
Az=real(Sol[0]) # recupere le tuple

print('Time for solving the system using CSR matrix: %8.2f sec' % (time.clock() - t1, ))

def rotationnel(x,y,Sol) :

  xg=zeros(nbelt,double)
  yg=zeros(nbelt,double)
  zg=zeros(nbelt,double)
  Bx=zeros(nbelt,double)
  By=zeros(nbelt,double)
  Bz=zeros(nbelt,double)

  for ielt in range(nbelt) :

    # Recuperation des donnees elementaires

    NumNoeuds = triangle[ielt][0:3]
    NumNoeuds=NumNoeuds-1
    idom = NumDom[ielt]-1
    xg[ielt]=0.
    yg[ielt]=0.
    for inoeud in range(3) :
      xe[inoeud]=x[NumNoeuds[inoeud]]
      ye[inoeud]=y[NumNoeuds[inoeud]]
      xg[ielt]=xg[ielt]+xe[inoeud]/3.
      yg[ielt]=yg[ielt]+ye[inoeud]/3.

    # Determinant et l'inverse de la matrice Jacobienne 
    DetJac = (xe[1]-xe[0])*(ye[2]-ye[0])-(xe[2]-xe[0])*(ye[1]-ye[0])
    InvJac = matrix([ [double(ye[2]-ye[0]) , double(-ye[1]+ye[0])] , [double(-xe[2]+xe[0]) , double(xe[1]-xe[0]) ] ])/DetJac

    # Calcul du rotationnel

    for inoeud in range(3) :
      for j in range(2) :
        
        Bx[ielt]= Bx[ielt]+(InvJac[1,j]*Grad[j,inoeud]*Sol[NumNoeuds[inoeud]])
        By[ielt]= By[ielt]-(InvJac[0,j]*Grad[j,inoeud]*Sol[NumNoeuds[inoeud]]) 
  
  return xg,yg,Bx,By

# Visualisation des lignes de champ magnétique (interpolation sur une grille uniforme)

def isovaleurs(x,y,Az) :

  xMin = x.min()
  xMax = x.max() 
  yMin = y.min()
  yMax = y.max()
    
  #Calcul du pas
    
  xPas = abs(xMax-xMin)/60;
  yPas = abs(yMax-yMin)/60;

  xi,yi = meshgrid(arange(xMin,xMax,xPas,'d'),arange(yMin,yMax,yPas,'d'))
  Azi = mlab.griddata(x,y,Az,xi,yi) 

  return xi,yi,Azi


# visu rotationel
xg,yg,Bx,By=rotationnel(x,y,Az)   
matplotlib.pyplot.quiver(xg,yg,Bx,By)

xi,yi,Azi=isovaleurs(x,y,Az)
matplotlib.pyplot.contour(xi,yi,Azi,30)

#pylab.imshow(Azi) #use matplotlib(pylab) to display
pylab.show()






  
