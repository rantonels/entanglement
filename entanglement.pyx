import numpy as np
from scipy.optimize import minimize


class BubbleParameters:
    def __init__(self):
        pass
    pass

def convertBubbleParameters(xm,l):
    '''Returns bubble parameters as a function of xm and l'''

    bp = BubbleParameters()
    bp.xm = xm
    bp.sm = np.sinh(xm)
    bp.cm = np.cosh(xm)
    bp.tm = np.tanh(xm)

    bp.sp = bp.sm/l
    bp.cp = np.sqrt(1+bp.sp**2)
    bp.tp = bp.sp/bp.cp
    bp.xp = np.arcsinh(bp.sp)

    bp.l = l

    return bp


def gamma_overall(theta_A,theta_B, xm, l):
    '''Computes the finite part of the length of the polygonal chain ABB'A', divided by L_-. (The divergent part is 2*L_-*Lambda.

    This calculation is only sensible if theta_A satisfies the parallelism bound.

    args:
        theta_A: half-aperture angle / angular position of A
            can be numpy array
        theta_B: angular position of B
            can be numpy array
        xm: geodesic radius of bubble in H2_- in units of L_-
        l: ratio of L_+ / L_-
        
    Returns:
        array with size tensor of sizes of theta_A, theta_B
        '''

    tB,tA = np.meshgrid(theta_B,theta_A) #order is VERY IMPORTANT! meshgrid is PERVERSE!!

    bp = convertBubbleParameters(xm,l)

    return gamma_raw(tA,tB,bp)

def gamma_raw(tA,tB,bp):
    '''don't touch this'''

    gamma_m = 2 * np.log(bp.cm - bp.sm * np.cos(tA-tB))
    


    gamma_p = bp.l*np.arccosh(bp.cp**2 - bp.sp**2 * np.cos(2*tB))


    return gamma_m + gamma_p

def gamma_vacuum(theta_A):
    '''Finite part of length of hyperbolic line of half-aperture theta_A, divided by L'''
    return 2*np.log(np.sin(theta_A))

def gamma(theta_A,xm,l,nB=200):

    # reflect values
    tA = np.where(theta_A < np.pi/2, theta_A, np.pi-theta_A)

    bp = convertBubbleParameters(xm,l)

    # parallelism bound
    # WHY + 0.01? Misteeeeeeeeeero
    bound = np.cos(tA) <= bp.tm# + 1.0/tA.shape[0]
 ,   

    gamma_vac = gamma_vacuum(tA)

    theta_B = np.linspace(0,np.pi/2,nB)
#    print theta_B.shape
#    print tA.shape

    gamma_ov = gamma_overall(tA,theta_B,xm,l)
#    gamma_tominim = lambda theta_B : gamma_overall(theta_A, theta_B, xm, l)

    #gamma_min = np.amin(gamma_ov, axis = -1)
    #theta_B_bar = np.argmin(gamma_ov, axis = -1)

    gamma_min_2 = np.zeros(tA.shape)
    cdef int i
    cdef float A
    cdef int N = tA.shape[0]
    for i in range(N):
        func = lambda B : gamma_raw(tA[i],B,bp)

        res = minimize(func, tA[i],tol=1e-4)
        

        gamma_min_2[i] = res.fun


#    print gamma_min.shape


    #return np.where(bound, gamma_min_2,gamma_vac)
    return np.minimum(gamma_min_2,gamma_vac)

#def dgammadb(tA, B, xm,l):
    # B is the sine of theta_B



def gamma_fast(theta_A,xm,l):
    # reflect values
    theta_A = np.where(theta_A < np.pi/2, theta_A, np.pi-theta_A)

    bp = convertBubbleParameters(xm,l)
    sp,cp,sm,cm = bp.sp,bp.cp,bp.sm,bp.cm

    # initial value
    cB = np.cos(theta_A)/bp.tm
    cB = np.clip(cB,0,1)
    B = np.sqrt(1-cB*cB)


    #fix thingies
#    B = np.maximum(B,(theta_A - np.arccos(bp.tm))**2)

    print "starting iteration"

    step = 2e-3
    iterations = 500
    cA = np.cos(theta_A)
    sA = np.sin(theta_A)
    cdef int i
    for i in xrange(iterations):
        B = np.clip(B,1e-10,sA)
        cB = np.sqrt(1-B*B)
        Am = cm - sm*(cA*cB +sA*B)

        Ap = cp*cp - sp*sp*(1-2*B*B)


        grad = 2*sm*(cA*B/cB - sA)/Am +  4*l*sp*sp*B/np.sqrt(Ap*Ap - 1)



#        print step,grad, step*grad

      
        B -=  step*grad



    B = np.clip(B,1e-10,1 - 1e-10)
    gamma_gradient = gamma_raw(theta_A,np.arcsin(B),bp)


    # near-diametre approximation fix
    
    cB = cp / ( cm - sm + cp) * cA   # <- thank you sympy!
    cB = np.clip(cB,1e-10,1-1e-10)
    gamma_nd = gamma_raw(theta_A, np.arccos(cB), bp)

    # near-parallelism approximation fix (doesn't work)

    Gamma1osm = (sm * cA + sA - cm)
    Gamma2osm = (-sm*sm * cA + sm * cm - 2*sm*sA + cA)

    B = np.clip( Gamma1osm / Gamma2osm,1e-10,1-1e-10)
    print B

    gamma_np = gamma_raw(theta_A,np.arcsin(B), bp)

    
    # small-decay (already used as initial condition, so shouldn't matter.)

    cB = np.cos(theta_A)/bp.tm
    cB = np.clip(cB,0,1)
    B = np.sqrt(1-cB*cB)
    gamma_sd = gamma_raw(theta_A,np.arcsin(B),bp)


    return  np.minimum(np.minimum(np.minimum(np.minimum(gamma_gradient,gamma_vacuum(theta_A)), gamma_nd),gamma_np),gamma_sd)

def minimizationtest(tA,B,bp,l):
    sp,cp,sm,cm = bp.sp,bp.cp,bp.sm,bp.cm
    print sp,cp
    sA,cA = np.sin(tA), np.cos(tA)
    cB = np.sqrt(1-B*B)
    Am = cm - sm*(cA*cB +sA*B)

    Ap = cp*cp - sp*sp*(1-2*B*B) # = cp^2 - sp^2 * (1 + 2 B cB - 1) =  1  + (1-2BcB) sp^2

    grad = 2*sm*(cA*B/cB - sA)/Am +  4*l*sp*sp*B/np.sqrt(Ap*Ap - 1)

    hstep = 1e-4
    tB = np.arcsin(B)
    tBp = np.arcsin(B+hstep)
    tBm = np.arcsin(B-hstep)
    numgrad = (gamma_raw(tA,tBp,bp) - gamma_raw(tA,tBm,bp))/(2*hstep)

    return (grad,numgrad)

def crofton(theta_A,xm,l,fast=True):
    function = gamma_fast if fast else gamma

    step = 0.00001 
    Sp = function(theta_A + step,xm,l)
    Sm = function(theta_A - step,xm,l)
    Sc = function(theta_A,xm,l)

    croftie = - 0.5* (Sp+Sm-2*Sc)/(step**2)
    return croftie
