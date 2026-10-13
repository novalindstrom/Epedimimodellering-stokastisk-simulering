
#==================================
# Gillespies algoritm
# Numeriska metoder och Simulering
#==================================
import numpy as np
import random

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
