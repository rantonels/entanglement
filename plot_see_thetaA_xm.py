import entanglement as ee
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl



#thetaA = np.linspace(0,np.pi,num=40,endpoint=True)
plt.figure(figsize=(3.0, 4.5))

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.rc("pgf", preamble=[r"\usepackage{amsmath}",
        r"\usepackage{amssymb}",
        r"\usepackage{physics}"])
xms = np.linspace(0,1.5,num=30)

ax = plt.gca()

ax.set_xlabel(r'$R/L_-$')
ax.set_ylabel(r'$S_\text{ent}$')

delta = .075
for thetaA in np.flip(np.linspace(np.pi/8,np.pi/2,6,endpoint=True),0):
    print thetaA

    
    gammas = [ min( ee.gamma(np.array([thetaA]),xm,0.5) , ee.gamma_vacuum(thetaA)) for xm in xms ]

    plt.plot(xms,gammas)
    i = 10
    ax.annotate(r'$%.2f \pi$'%(thetaA/np.pi), xy=(-0.1,gammas[0]-0.05+delta ))
    delta = 0
            
        

ax.set_xlim((-.15,xms[-1]))
plt.savefig('sEE_thetaA_xm.pgf',bbox_inches='tight')
plt.savefig('sEE_thetaA_xm.pdf',bbox_inches='tight')

plt.show()
