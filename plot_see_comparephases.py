import entanglement as ee
import numpy as np

bp = ee.convertBubbleParameters(1.0,0.5)

theta_A = np.linspace(0.4,1.0,200)

parallelism_theta_A = np.arccos(bp.tm)
theta_A_cropped = np.linspace(theta_A[0], parallelism_theta_A,100)

vacuum_phase = ee.gamma_vacuum(theta_A_cropped)

upper_theta_B = ee.extremalB(theta_A,bp,False)
lower_theta_B = ee.extremalB(theta_A,bp,True)

upper_injection_phase = ee.gamma_raw(theta_A,upper_theta_B,bp)
lower_injection_phase = ee.gamma_raw(theta_A,lower_theta_B,bp)



print "calc done... plotting."

import matplotlib as mpl
mpl.use("pgf")

import matplotlib.pyplot as plt


fig = plt.gcf()

fig.set_size_inches(6,4)

plt.rc('text', usetex=True)
plt.rc('pgf', preamble=r'\usepackage{amsmath}')
plt.rc('font', family='serif')

plt.plot(theta_A_cropped,vacuum_phase,label="vacuum",color="blue")
plt.plot(theta_A,upper_injection_phase,label="injection",color="crimson")
#plt.plot(theta_A,lower_injection_phase,label="lower injection",color="gold")

#plt.plot([parallelism_theta_A,parallelism_theta_A],[0,-3],color="black")
plt.axvline(x=parallelism_theta_A,color="black",linestyle="--")

plt.xlabel(r"$\theta_A$")
plt.ylabel(r"$L_\text{min} = 4G_3 S_\text{ent}$")

arrowpr = dict(arrowstyle="->", shrinkA = 0.2, shrinkB=0.2 )

plt.annotate(r"$\theta_A^\text{crit}$",
        xy=(0.66,-0.99),
        xytext=(.66,-1.2), 
        arrowprops=arrowpr,
        ha="center",va="center")

endpt = (parallelism_theta_A,vacuum_phase[-1])

plt.annotate(r"$\theta_A^\text{par}$",
        xy=endpt,xytext=(endpt[0]+0.03,endpt[1]-0.7), 
        ha="center",va="center")


plt.legend(loc='upper left')

#plt.show()

fig.savefig("plot_phases.png",dpi=300)
fig.savefig("plot_phases.pgf",bbox_inches="tight")

