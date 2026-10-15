
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
c = np.array([b/N, g]) #vår propentitestfunktions array

Y0 = np.array([995, 5, 0]) #5 är smittade i start 0 resistenta, resten mottaglig


# ----------- Funktioner ---------------
#denna kan behöva byta plats på rader och kolumner
#just nu är rader = SIR, klm = reaktioner
def stockiomatris():
    A = np.array([
        [-1,  0],  #antalet mottagliga för sjukdomen
        [1,  -1],  #antalet smittade
        [0,  1],  #antalet resistenta
    ])
    
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

