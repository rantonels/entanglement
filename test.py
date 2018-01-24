import entanglement as ee
import numpy as np

import matplotlib.pyplot as plt

for xm in list(np.linspace(0.1,2.001,5)):
    print xm
    #xm = 1.5
    l = 0.5


    bp = ee.convertBubbleParameters(xm,l)
    HALF = 2* ( - bp.xm + l*bp.xp)


    tA = np.linspace(0,np.pi,200)


#    tA = np.array([np.pi/4])

#    gamma = ee.gamma(tA,xm,l,100)
#    gammatest = ee.gamma_fast(tA,xm,l)

#    theta_A = np.arccos(np.tanh(xm))+0.3

#    B = np.linspace(0.0000001,np.pi/4,200)
#    thest,numthest = ee.minimizationtest(theta_A,B, bp,l)

#    plt.plot(B,thest)
#    plt.plot(B,numthest)

    croft = ee.crofton(tA,xm,l) * np.sin(tA)**2

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

plt.show()
