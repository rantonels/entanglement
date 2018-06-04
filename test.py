import entanglement as ee
import numpy as np

import matplotlib.pyplot as plt

plt.figure(figsize=(6.3,4.0))

for xm in list(np.linspace(0.5,2.001,9)):
    print xm
    #xm = 1.5
    l = 0.5


    bp = ee.convertBubbleParameters(xm,l)
    HALF = 2* ( - bp.xm + l*bp.xp)


    tA = np.linspace(0,np.pi,300)


#    tA = np.array([np.pi/4])

    gamma = ee.gamma(tA,xm,l)
#    gammatest = ee.gamma_fast(tA,xm,l)

#    theta_A = np.arccos(np.tanh(xm))+0.3

#    B = np.linspace(0.0000001,np.pi/4,200)
#    thest,numthest = ee.minimizationtest(theta_A,B, bp,l)

#    plt.plot(B,thest)
#    plt.plot(B,numthest)

    croft = ee.crofton(tA,xm,l,fast=False) * np.sin(tA)**2

    croft[ np.diff(croft) < - 0.2 ] = np.nan

    #tB = np.linspace(0,np.pi,100)
    #
    #gammaD = ee.gamma_overall(tA,tB,xm,l)


    #mB,mA = np.meshgrid(tB,tA)

#    plt.plot(tA,gamma)
#    plt.plot(tA,gammatest)

    plt.plot(tA,croft)
    #plt.plot(tA,np.repeat(HALF,tA.shape))

    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    #
    #ax.plot_wireframe(mA,mB,gammaD)

ax = plt.gca()
ax.set_xlabel(r"$\theta_A$")
ax.set_ylabel(r"$\Omega$")
ax.set_ylim([-5,5])
plt.show()
plt.savefig('croftcrater.pgf', bbox_inches='tight')
plt.savefig('croftcrater.pdf', bbox_inches='tight')
