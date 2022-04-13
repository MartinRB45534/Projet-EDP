import numpy as np
from operator import itemgetter

def cree_bords_triangles(P1,P2,P3):
    """
    Renvoie les deux fonctions qui indiquent le haut et le bas du triangle
    """
    xs = sorted([P1,P2,P3],key=itemgetter(0)) #De gauche à droite
    ys = sorted([P1,P2,P3],key=itemgetter(1)) #De bas en haut

    if ys[0][0]==ys[2][0]: #Le point le plus haut et le point le plus bas sont au-dessus l'un de l'autre
        #On a donc juste besoin de tracer les droites entre ces points et celui du milieu
        def bord_bas(x):
            """Renvoie la coordonnée y du bas du triangle pour un x donné"""
            return ys[0][1]+(ys[1][1]-ys[0][1])*(x-ys[0][0])/(ys[1][0]-ys[0][0]) # S'il y a une division par 0 ici, c'est que le triangle est dégénéré, on a fait une grosse erreur avant !
        def bord_haut(x):
            """Renvoie la coordonnée y du haut du triangle pour un x donné"""
            return ys[2][1]+(ys[1][1]-ys[2][1])*(x-ys[2][0])/(ys[1][0]-ys[2][0]) # S'il y a une division par 0 ici, c'est que le triangle est dégénéré, on a fait une grosse erreur avant !

    elif ys[0][0]==ys[1][0]: #Le point du milieu et le point le plus bas sont au-dessus l'un de l'autre
        #On a donc juste besoin de tracer les droites entre ces points et celui du haut
        def bord_bas(x):
            """Renvoie la coordonnée y du bas du triangle pour un x donné"""
            return ys[0][1]+(ys[2][1]-ys[0][1])*(x-ys[0][0])/(ys[2][0]-ys[0][0]) # S'il y a une division par 0 ici, c'est que le triangle est dégénéré, on a fait une grosse erreur avant !
        def bord_haut(x):
            """Renvoie la coordonnée y du haut du triangle pour un x donné"""
            return ys[1][1]+(ys[2][1]-ys[1][1])*(x-ys[1][0])/(ys[2][0]-ys[1][0]) # S'il y a une division par 0 ici, c'est que le triangle est dégénéré, on a fait une grosse erreur avant !

    elif ys[1][0]==ys[2][0]: #Le point le plus haut et le point du milieu sont au-dessus l'un de l'autre
        #On a donc juste besoin de tracer les droites entre ces points et celui du bas
        def bord_bas(x):
            """Renvoie la coordonnée y du bas du triangle pour un x donné"""
            return ys[1][1]+(ys[0][1]-ys[1][1])*(x-ys[1][0])/(ys[0][0]-ys[1][0]) # S'il y a une division par 0 ici, c'est que le triangle est dégénéré, on a fait une grosse erreur avant !
        def bord_haut(x):
            """Renvoie la coordonnée y du haut du triangle pour un x donné"""
            return ys[2][1]+(ys[0][1]-ys[2][1])*(x-ys[2][0])/(ys[0][0]-ys[2][0]) # S'il y a une division par 0 ici, c'est que le triangle est dégénéré, on a fait une grosse erreur avant !

    elif xs[1][1]==ys[0][1]: #Le milieu horizontal est en bas
        #Sur le bord bad, on a deux droites, mais sur le bord haut c'est facile
        def bord_bas(x):
            """Renvoie la coordonnée y du bas du triangle pour un x donné"""
            if x<xs[1][0]:
                return xs[0][1]+(xs[1][1]-xs[0][1])*(x-xs[0][0])/(xs[1][0]-xs[0][0]) #On n'a normalement pas de points au-dessus l'un de l'autre
            else:
                return xs[2][1]+(xs[1][1]-xs[2][1])*(x-xs[2][0])/(xs[1][0]-xs[2][0]) #On n'a normalement pas de points au-dessus l'un de l'autre
        def bord_haut(x):
            """Renvoie la coordonnée y du haut du triangle pour un x donné"""
            return xs[0][1]+(xs[2][1]-xs[0][1])*(x-xs[0][0])/(xs[2][0]-xs[0][0])

    elif xs[1][1]==ys[2][1]: #Le milieu horizontal est en haut
        #Sur le bord haut, on a deux droites, mais sur le bord bas c'est facile
        def bord_bas(x):
            """Renvoie la coordonnée y du bas du triangle pour un x donné"""
            return xs[0][1]+(xs[2][1]-xs[0][1])*(x-xs[0][0])/(xs[2][0]-xs[0][0])
        def bord_haut(x):
            """Renvoie la coordonnée y du haut du triangle pour un x donné"""
            if x<xs[1][0]:
                return xs[0][1]+(xs[1][1]-xs[0][1])*(x-xs[0][0])/(xs[1][0]-xs[0][0]) #On n'a normalement pas de points au-dessus l'un de l'autre
            else:
                return xs[2][1]+(xs[1][1]-xs[2][1])*(x-xs[2][0])/(xs[1][0]-xs[2][0]) #On n'a normalement pas de points au-dessus l'un de l'autre

    return [bord_bas,bord_haut]