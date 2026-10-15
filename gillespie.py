
#==================================
# Gillespies algoritm
# Numeriska metoder och Simulering
#==================================
import numpy as np
import random
#---testar
#Se till att både de deterministiska modellerna (0DE)
# och de motsvarande stokastiska modellerna (reaktionsformulering, 
# inklusive reaktioner, stökiometrimatris och propensitetsvektor)
# finns tydligt beskrivna för varje modell (SIR, SEIR etc) ni implementerar.
# Det gäller även er egen modell om ni satsar på 5-poängsprojektet. 

import numpy as np
import random
import matplotlib.pyplot as plt

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
    return A

#Y är en array som innehåller [s(t), I(t), R(t)]
def propensitetsfunktioner(Y, c):
    #tar ut variabler från en array och sätter värden så s(t) = y[0] osv
    S1 = Y[0]
    I1 = Y[1]
    R1 = Y[2] #denna blir alltså inte använd, kan det vara felet?
    c1, c2 = c[0], c[1]
    #print ("hit går vi") yep
    
    #faktiska derivator från uppgiften, paranteser för tydlighetens skull
    a1 = -(c1 * I1 * S1) 
    a2 =  (c1 * I1 * S1) - (c2 * I1)
    a3 = c2 * I1
    
    #bygger en array med alla dessa värden som retuneras
    A = np.array([a1, a2, a3])
    print(A)
    return A

#----- annan fil egentilfen

def SSA(prop,stoch,X0,tspan,coeff):
    tvec=np.zeros(1)
    tvec[0]=tspan[0]
    Xarr=np.zeros([1,len(X0)])
    Xarr[0,:]=X0
    t=tvec[0]
    X=X0
    sMat=stoch()
    
    while t<tspan[1]:
        re=prop(X,coeff)
        a0=sum(re)
        if a0>1e-10:    
     # Bestäm reaktionstid
            r1=random.random()
            tau=-np.log(r1)/a0
            t+=tau
            tvec=np.append(tvec,t)
# Bestäm vilken reaktion
            r2=random.random()
            cre=np.cumsum(re)
            cre=cre/cre[-1]
            r=0
            while cre[r]<r2:
                r+=1
                X=X+sMat[r,:]
                Xarr=np.vstack([Xarr,X])
        else: # Alla reaktionshastigheter 0
            print('Simuleringen avslutad vid t=', t)
            return tvec, Xarr
    
    return tvec, Xarr

plt.figure(figsize=(10, 6))

# Kör 5 oberoende simuleringar och plotta dem i samma diagram
antal_forsok = 5
for i in range(antal_forsok):
    tvec, Xarr = SSA(propensitetsfunktioner, stockiomatris, Y0, tspan, c)
    
    # Plotta bytesdjur (Y1) med heldragen linje och rovdjur (Y2) med streckad linje
    if i == 0:
        plt.plot(tvec, Xarr[:, 0], 'b-', label='Bytesdjur (Y1)', alpha=0.5)
        plt.plot(tvec, Xarr[:, 1], 'r--', label='Rovdjur (Y2)', alpha=0.5)
    else:
        plt.plot(tvec, Xarr[:, 0], 'b-', alpha=0.3)
        plt.plot(tvec, Xarr[:, 1], 'r--', alpha=0.3)

plt.xlabel('Tid (t)')
plt.ylabel('Antal individer')
plt.title('Stokastisk simulering av Predator-Byte modell (Gillespie)')
plt.legend()
plt.grid(True)
plt.show()