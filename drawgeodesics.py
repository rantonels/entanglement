import entanglement as ee
import hyperbolicartist as ha
from numpy import pi,sin,cos,tanh
from sympy import Point
import numpy as np

l = 0.5
xm = 1.0

# crit: theta_A = 0.657
# par: theta_A = 0.705 

col_vac = (0,0,1)
col_inj = [(1,0,0),(1,1,0)]
col_bub = (0,0.7,0)

bp = ee.convertBubbleParameters(xm,l)

diskOut = ha.PoincareDisk(1)

R = tanh(bp.xm/2) / tanh(bp.xp/2)

diskIn = ha.PoincareDisk(R)


dr = ha.Drawing(500)
dr.drawBoundary(diskOut)
#dr.drawBoundary(diskIn)
dr.set_color(*col_bub)
alf = tanh(bp.xm/2.)
dr.drawCircle(alf)

for theta_A in [0.4,0.658,0.660,0.9,1.3]: #np.linspace(0.6,0.71,5):
    print theta_A, "n"

    dr.set_color(0,0,0)

    A = Point(-sin(theta_A),-cos(theta_A))
    Abar = Point(sin(theta_A),-cos(theta_A))
    Abar_corrected = Point(0.9999*Abar.x,0.9999*Abar.y)

    dr.drawPoint(A)
    dr.drawPoint(Abar)


    theta_B = ee.extremalB(theta_A,bp,False)
    length_vacuum = ee.gamma_vacuum(theta_A)
    length_upper = ee.gamma_raw(theta_A,theta_B,bp)

    if (length_upper > length_vacuum):
        dr.set_color(*col_vac)
        dr.drawArc(A,Abar,diskOut.segmentToArcCentre(A,Abar_corrected))
        print "boi"
    else:

	for reverse in [False,True]:

		theta_B = ee.extremalB(theta_A,bp,reverse)

		print theta_A/np.pi, theta_B/np.pi


		B = Point(-alf*sin(theta_B), -alf*cos(theta_B))
		Bbar = Point(-B.x,B.y)
	       
		if False:
		    dr.set_color(1,0,0)
		    dr.drawArc(A,Abar,diskOut.segmentToArcCentre(A,Abar_corrected))

		dr.set_color(*(col_inj[reverse]))

		dr.drawPoint(B)
		dr.drawPoint(Bbar)

		dr.drawArc(A,B,diskOut.segmentToArcCentre(A,B))
		dr.drawArc(B,Bbar,diskIn.segmentToArcCentre(B,Bbar))
		dr.drawArc(Abar,Bbar,diskOut.segmentToArcCentre(Abar,Bbar))

		
dr.close()



