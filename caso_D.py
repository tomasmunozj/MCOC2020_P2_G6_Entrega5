from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from math import *

def caso_D():
    
    # Unidades base
    m = 1.
    kg = 1.
    s = 1. 
    
    #Unidades derivadas
    N = kg*m/s**2
    cm = 0.01*m
    mm = 0.001*m
    KN = 1000*N
    Pa = N / m**2
    KPa = 1000*Pa
    MPa = 1000*KPa
    GPa = 1000*MPa
    KGF = 9.8067*N
    
    #Parametros
    L = 5.0 * m
    B = 2.0 * m
    H = 5 * m
    q = 400 * kg / m**2

    #Inicializar modelo
    ret = Reticulado()
    
    #Nodos
    
    for a in range(45):

        ret.agregar_nodo( 10 + a * L    , 2   ,  100         ) 
        
    for a in range(45):

        ret.agregar_nodo( 10 + a * L    , 0   ,  100         )  
        
    for a in range(44):
        ret.agregar_nodo( 10 + (L/2) + a * L    , 1   ,  100  + H  )
    
    
#   Barras

    props = [10*cm, 45*mm, 200*GPa, 7600*kg/m**3, 420*MPa]
    props2 = [20*cm, 90*mm, 200*GPa, 7600*kg/m**3, 420*MPa]
    props3 = [9.5*cm, 45*mm, 200*GPa, 7600*kg/m**3, 420*MPa]
    props4 = [9*cm, 40*mm, 200*GPa, 7600*kg/m**3, 420*MPa]
    
    for a in range(44): #Barras abajo en y = 2
        
        ret.agregar_barra(Barra(a, a+1, *props))
   
    for a in range(45,89): #Barras abajo en y = 0
    
        ret.agregar_barra(Barra(a, a+1, *props))
    
    for a in range(90,133): #Barras superiores
        
        ret.agregar_barra(Barra(a, a+1, *props2))
    
    
#    Barras Diagonales
    for a in range(44):
        
        ret.agregar_barra(Barra(a, a + 90, *props))
        
    for a in range (45,89):
        
        ret.agregar_barra(Barra(a, a + 45, *props))
    
    for a in range(44):
        
        ret.agregar_barra(Barra(a+1, a + 90, *props))
    
    for a in range (46,90):
        
        ret.agregar_barra(Barra(a, a + 44, *props))    
    
    for a in range(45):
        
        ret.agregar_barra(Barra(a+1, a + 46, *props))
        
    ret.agregar_barra(Barra(0, 45, *props))  
    
    ret.agregar_barra(Barra(0, 45, *props))


    
    #Barras Diagonales de abajo
    for a in range(44):
        
        ret.agregar_barra(Barra(a, a + 46, *props3))
        
    for a in range(44):
        
        ret.agregar_barra(Barra(a + 1, a + 45, *props3))



    
    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
    
    ret.agregar_restriccion(45, 0, 0)
    ret.agregar_restriccion(45, 1, 0)
    ret.agregar_restriccion(45, 2, 0)
    
    
    ret.agregar_restriccion(43, 1, 0)
    ret.agregar_restriccion(43, 2, 0)
    ret.agregar_restriccion(88, 1, 0)
    ret.agregar_restriccion(88, 2, 0)
    

	
	
    return ret

