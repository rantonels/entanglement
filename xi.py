import matplotlib.pyplot as plt
import numpy as np

fig = plt.gcf()
fig.set_size_inches((2.2,4))

R = 3

lam = np.linspace(-np.pi/2,np.pi/2,500)
rho = 2 * np.arctanh(np.tan(lam/2))
tau = np.linspace(-R,R,500)

L,T = np.meshgrid(lam,tau)

xi2 =  np.cosh(rho)*np.cos(T)

F = 0.3

val_one = np.exp(np.linspace(-F,F,11))


vals = np.concatenate( (-val_one[::-1],val_one)        )

print vals

plt.contour(lam,tau,xi2,vals,colors="black",linewidths=1)
plt.axvline(x=-np.pi/2,c="black")
plt.axvline(x=np.pi/2,c="black")
plt.axes().set_aspect('equal', 'datalim')
plt.axis("off")
#plt.show()
fig.savefig("penrosie.png",bbox_inches="tight")
fig.savefig("penrosie.pgf",bbox_inches="tight")
