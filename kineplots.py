import entanglement as ee
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import lines

def arccot(x):
    return np.arctan(1/x)

f, axes = plt.subplots(2,2,sharex='col',sharey='row',figsize=(6,4))

for k in [0,1,2,3]:

    xm = 0.5
    l = 0.5

    D = 1e-4



    beta = [0.0,0.8,0.999,0.999][k]
    gamma = 1/np.sqrt(1-beta*beta)


    H=2.0626

    if k==3:
        H = arccot(np.tan(H)*np.log(gamma))
        H += np.pi * (H < 0)


    print H


    phiflat = np.linspace(0,2*np.pi,100)

    tA,phi = np.meshgrid(np.linspace(D,np.pi-D,100),np.linspace(0,2*np.pi,100))


    ntA = arccot(gamma * ( beta /np.sin(tA) * np.cos(phi) + 1./np.tan(tA))  )

    Hwarp = arccot(gamma*(-beta/np.sin(H) * np.cos(phiflat) + 1./np.tan(H)))
    Hwarp2 = arccot(gamma*(-beta/np.sin(H) * np.cos(phiflat) - 1./np.tan(H)))

    ntA += np.pi * (ntA < 0)
    Hwarp += np.pi * (Hwarp < 0)
    Hwarp2 += np.pi * (Hwarp2 < 0)

    phiwarp_sin = np.sin(Hwarp)/np.sin(H) * np.sin(phiflat)
    phiwarp_cos = gamma * (np.cos(phiflat) / np.sin(H) - beta / np.tan(H)) * np.sin(Hwarp)

    phiwarp = np.arctan2(phiwarp_sin,phiwarp_cos)
    phiwarp += 2*np.pi *(phiwarp < 0)

    phiwarp_sin = np.sin(Hwarp2)/np.sin(H) * np.sin(phiflat)
    phiwarp_cos = gamma * (np.cos(phiflat) / np.sin(H) + beta / np.tan(H)) * np.sin(Hwarp2)

    phiwarp2 = np.arctan2(phiwarp_sin,phiwarp_cos)
    phiwarp2 += 2*np.pi *(phiwarp2 < 0)



    # nphi is not important


#    Omega = ee.crofton(ntA,xm,l,fast=False) * np.sin(ntA)**2
#    masked_Omega = np.ma.array(Omega,mask=np.isnan(Omega))


#    plt.subplot(2,2,1+k)
    ax = axes[k//2][k%2]



    #plt.contourf(phi,tA,masked_Omega,levels=np.linspace(0,0.5,15))

    ax.plot(phiwarp,Hwarp,c='blue')
    ax.plot(phiwarp2,Hwarp2,c='blue')

    # light cone
    ax.plot([np.pi,0],[0,np.pi],ls='--',color='red')
    ax.plot([np.pi,2*np.pi],[0,np.pi],ls='--',color='red')


    ax.set_xlim(0,2*np.pi)
    ax.set_ylim(0,np.pi)

    ax.set_aspect("equal")

    ax.set_xticks( (0,np.pi,2*np.pi))
    ax.set_xticklabels((r"$0$",r"$\pi$",r"$2\pi$"))
    ax.set_yticks( (0,np.pi/2,np.pi))
    ax.set_yticklabels( (r"$0$",r"$\pi/2$",r"$\pi$"))

    ax.set_xlabel(r'$\phi$')
    ax.set_ylabel(r'$\theta_A$')

    #ax =  plt.gca()

    for arrx in [0,2*np.pi]:

            arry = 0.45*np.pi
            arrd = 0.1

            arrT = 2*np.pi

            arx = arrx + np.array([-arrd,0,arrd])
            ary = np.array([arry-arrd,arry,arry-arrd])

            line = lines.Line2D(arx,ary, lw=.5, color='k')
            line.set_clip_on(False)

            ax.add_line(line)

for ax in axes.flat:
    ax.label_outer()

f.savefig("kinematic.png")
f.savefig("kinematic.pgf")

plt.show()
