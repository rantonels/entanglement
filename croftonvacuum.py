import entanglement as ee
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm

mpl.use("pgf")

plt.rc('text', usetex=True)
plt.rc('pgf', preamble=r'\usepackage{amsmath}')
plt.rc('font', family='serif')

fig = plt.gcf()
fig.set_size_inches(4.5,3.0)

xms = np.linspace(0.5,2.001,9)
tA = np.linspace(0,np.pi,300)

l = 0.5

plt.plot(tA,np.full_like(tA,l),ls='--',c="black")

for it in range(len(xms)):
    xm = xms[it]
    print xm
    bp = ee.convertBubbleParameters(xm,l)
#    gamma = ee.gamma(tA,xm,l)
    croft = ee.crofton(tA,xm,l,fast=False) * np.sin(tA)**2
    
    plt.plot(tA,croft, c=cm.viridis(it/float(len(xms))) )

    


ax = plt.gca()
ax.set_xlabel(r"$\theta_A$")
ax.set_ylabel(r"$\Omega$")
ax.set_ylim([0.25,1.04])
fig.savefig('croftvac.pgf', bbox_inches='tight')
fig.savefig('croftvac.png', dpi=300)
