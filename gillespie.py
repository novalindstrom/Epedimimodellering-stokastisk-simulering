
#==================================
# Gillespies algoritm
# Numeriska metoder och Simulering
#==================================
import numpy as np
import random
import SIR_modell as sir
import matplotlib.pyplot as plt


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

# Kör 10 oberoende simuleringar och plotta dem i samma diagram
antal_forsok = 10
for i in range(antal_forsok):
    tvec, Xarr = SSA(sir.propensitetsfunktioner_SEIR, sir.stockiomatris_SEIR, sir.Y0, sir.tspan, sir.c)
    
    # Plotta bytesdjur (Y1) med heldragen linje och rovdjur (Y2) med streckad linje
    # Plotta Mottagliga (S) och Smittade (I)
    if i == 0:
        plt.plot(tvec, Xarr[:, 0], 'b-', label='Mottagliga (S)', alpha=0.5)
        plt.plot(tvec, Xarr[:, 1], 'r-', label='Smittade (I)', alpha=0.5)
        plt.plot(tvec, Xarr[:, 2], 'g-', label='Resistenta (R)', alpha=0.5) # Lägg till R också om du vill se alla tre!

    else:
        plt.plot(tvec, Xarr[:, 0], 'b-', alpha=0.3)
        plt.plot(tvec, Xarr[:, 1], 'r--', alpha=0.3)
        plt.plot(tvec, Xarr[:, 2], 'g-', alpha=0.3)

plt.xlabel('Tid (t)')
plt.ylabel('Antal individer')
plt.title('Stokastisk simulering av SIR')
plt.legend()
plt.grid(True)
plt.show()