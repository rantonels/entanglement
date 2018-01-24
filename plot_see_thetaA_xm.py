import entanglement as ee
import numpy as np
import matplotlib.pyplot as plt

#thetaA = np.linspace(0,np.pi,num=40,endpoint=True)
plt.figure(figsize=(4.0, 6.3))

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

xms = np.linspace(0,1.5,num=30)

ax = plt.gca()

ax.set_xlabel(r'$x_-$')
ax.set_ylabel(r'$S_{EE}$')

delta = .075
for thetaA in np.flip(np.linspace(np.pi/8,np.pi/2,8,endpoint=True),0):
    print thetaA

    
    gammas = [ ee.gamma(np.array([thetaA]),xm,0.5) for xm in xms ]

    plt.plot(xms,gammas,color="k")
    i = 10
    ax.annotate(r'$%.2f \pi$'%(thetaA/np.pi), xy=(-0.1,gammas[0]-0.05+delta ))
    delta = 0
            
        

ax.set_xlim((-.15,xms[-1]))
plt.savefig('sEE_thetaA_xm.pgf',bbox_inches='tight')
plt.savefig('sEE_thetaA_xm.pdf',bbox_inches='tight')
