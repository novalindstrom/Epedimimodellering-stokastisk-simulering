
#---testar
#Se till att både de deterministiska modellerna (0DE)
# och de motsvarande stokastiska modellerna (reaktionsformulering, 
# inklusive reaktioner, stökiometrimatris och propensitetsvektor)
# finns tydligt beskrivna för varje modell (SIR, SEIR etc) ni implementerar.
# Det gäller även er egen modell om ni satsar på 5-poängsprojektet. 

import numpy as np
import random

# ----------- Startvärden --------------
tspan = [0, 120]
b = 0.3 #beta är 0.3
N = 1000 #startpersoner är 1000 varav 5 smittade (inte med)
g = 1/7 #gamma är 1/7
alfa = 0.5 # Inkubationstid - TODO - ju mindre dagar desto fler blir smittade
my = 0.3 #dödlighet TODO: kolla att alla dessa variabler är rätt enhet (är det per dag eller % osv)
v = 1/7
c = np.array([b/N, g, alfa, my, v]) #vår propentitestfunktions array


Y0 = np.array([995, 0, 5, 0, 0, 0]) #5 är smittade i start 0 resistenta, resten mottaglig


# ----------- SIR MODELLEN ---------------
#denna kan behöva byta plats på rader och kolumner
#just nu är rader = SIR, klm = reaktioner
def stockiomatris():
    #test att vända på matrisen
    B = np.array([

        [-1, 1, 0],
        [ 0, -1 , 1]
    ])
    return B

#Y är en array som innehåller [s(t), I(t), R(t)] Returvärdet är bara propfunktionerna i sin grundform
def propensitetsfunktioner(Y, c):
    #tar ut variabler från en array och sätter värden så s(t) = y[0] osv
    S1 = Y[0] #antal mottagliga just nu
    I1 = Y[1] #antal smittade just nu
    R1 = Y[2] #denna blir alltså inte använd, kan det vara felet?
    c1, c2 = c[0], c[1] #reaktionshastigheterna
    
    #faktiska derivator från uppgiften, paranteser för tydlighetens skull
    a1 = (c1 * I1 * S1) 
    #a2 =  (c1 * I1 * S1) - (c2 * I1)
    a3 = c2 * I1
    
    #bygger en array med alla dessa värden som retuneras
    A = np.array([a1, a3])
    #print(A)
    return A

#----------------- SIER MODELL ------------------------

def stockiomatris_SEIR():
    #test att vända på matrisen
    B = np.array([

        [-1, 1, 1, 0],
        [ 0, 0, -1 , 1],
        [0, -1, 1,0]
    ])
    return B

def propensitetsfunktioner_SEIR(Y, c):
    #tar ut variabler från en array och sätter värden så s(t) = y[0] osv
    S1 = Y[0] #antal mottagliga just nu
    E1 = Y[1]
    I1 = Y[2] #antal smittade just nu
    R1 = Y[3]
    
    c1, c2, c3 = c[0], c[1], c[2] #reaktionshastigheterna
    
    #faktiska derivator från uppgiften, paranteser för tydlighetens skull
    a1 = (c1 * I1 * S1) 
    #a2 =  (c1 * I1 * S1) - (c2 * I1)
    a2 = c2 * I1
    a3 = c3 * E1
    
    #bygger en array med alla dessa värden som retuneras
    A = np.array([a1, a2, a3])
    #print(A)
    return A



#----------------- SIERD MODELL ------------------------

def stockiomatris_SEIRD():
    #test att vända på matrisen
    B = np.array([

        [-1, 1, 1, 0, 0],
        [ 0, 0, -1 , 1, 0],
        [0, -1, 1,0, 0],
        [0, 0, -1, 0, 1]
    ])
    return B

def propensitetsfunktioner_SEIRD(Y, c):
    #tar ut variabler från en array och sätter värden så s(t) = y[0] osv
    S1 = Y[0] #antal mottagliga just nu
    E1 = Y[1]
    I1 = Y[2] #antal smittade just nu
    R1 = Y[3]
    D1 = Y[4]
    
    c1, c2, c3, c4 = c[0], c[1], c[2], c[3] #reaktionshastigheterna
    
    #faktiska derivator från uppgiften, paranteser för tydlighetens skull
    a1 = (c1 * I1 * S1) 
    a2 = c2 * I1
    a3 = c3 * E1
    a4 = c4 * I1
    
    #bygger en array med alla dessa värden som retuneras
    A = np.array([a1, a2, a3, a4])
    #print(A)
    return A



#----------------- SIERDV MODELL + va------------------------

def stockiomatris_SEIRDV():
    #test att vända på matrisen
    B = np.array([

        [-1, 1, 1, 0, 0, 0],
        [ 0, 0, -1 , 1, 0, 0],
        [0, -1, 1,0, 0, 0],
        [0, 0, -1, 0, 1, 0],
        [-1, 0, 0, 0, 0, 1]
    ])
    return B

def propensitetsfunktioner_SEIRDV(Y, c):
    #tar ut variabler från en array och sätter värden så s(t) = y[0] osv
    S1 = Y[0] #antal mottagliga just nu
    E1 = Y[1]
    I1 = Y[2] #antal smittade just nu
    R1 = Y[3]
    D1 = Y[4]
    V1 = Y[5]
    
    c1, c2, c3, c4, c5  = c[0], c[1], c[2], c[3], c[4] #reaktionshastigheterna
    
    #faktiska derivator från uppgiften, paranteser för tydlighetens skull
    a1 = (c1 * I1 * S1) 
    #a2 =  (c1 * I1 * S1) - (c2 * I1)
    a2 = c2 * I1
    a3 = c3 * E1
    a4 = c4 * I1
    a5 = v
    
    #bygger en array med alla dessa värden som retuneras
    A = np.array([a1, a2, a3, a4, a5])
    #print(A)
    return A
