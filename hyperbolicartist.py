import sympy
from sympy import Point,Segment
from numpy import pi,arctan2

class PoincareDisk:
    def __init__(self,radius=1.0):
        self.radius = radius

    def segmentToArcCentre(self,p1,p2):

        p2norm = float(p2.distance(Point(0,0)))**2
        p3 = Point((self.radius**2) * float(p2.x) /p2norm, (self.radius**2)* float(p2.y) / p2norm)

        s12 = Segment(p1,p2)
        s23 = Segment(p2,p3)

        try:
            pb12 = s12.perpendicular_bisector()
            pb23 = s23.perpendicular_bisector()
        except AttributeError:
            print "EROR",s12,s23
            return Point(0,0)

        center = pb12.intersection(pb23)[0]

        return center


import cairo

class Drawing:
    def __init__(self,size):
        self.size = size
        self.surf = cairo.SVGSurface("test.svg",size,size)
        self.ctx = cairo.Context(self.surf)

        self.ctx.scale(size/2.,size/2.)

        self.ctx.translate(1,1)

        self.ctx.set_source_rgb(1,1,1)
        self.ctx.rectangle(-1,-1,2,2)
        self.ctx.fill()

        self.ctx.set_source_rgb(0,0,0)


    def drawBoundary(self,disk):
        self.ctx.arc(0,0,disk.radius,0,2*pi)
        self.ctx.set_line_width(0.005)
        self.ctx.stroke()
    
    def drawPoint(self,p):
        self.ctx.arc(p.x,p.y,0.01,0,2*pi)
        self.ctx.fill()

    def set_color(self,r,g,b):
        self.ctx.set_source_rgb(r,g,b)

    def drawArc(self,p1,p2,C):
        r = p1.distance(C)
        pover = C + Point(1,0)
        segup = Segment(C,pover)
        #angle1 = float(Segment(p1,C).angle_between(segup))
        #angle2 = float(Segment(p2,C).angle_between(segup))


        angle1 = arctan2(float((p1-C).y),float((p1-C).x))
        angle2 = arctan2(float((p2-C).y),float((p2-C).x))
        anglea = min(angle1,angle2)
        angleb = max(angle1,angle2)

        self.ctx.arc(C.x,C.y,r,anglea,angleb)
        self.ctx.stroke()


    def drawCircle(self,radius):
        self.ctx.arc(0,0,radius,0,2*pi)
        self.ctx.stroke()

    def close(self):
        self.surf.finish()


#diskOut = PoincareDisk(1)
#
#
#dr = Drawing(500)
#dr.drawBoundary(diskOut)
#C = Point(-.9,0)
#D = Point(0,.9)
#dr.drawPoint(C)
#dr.drawPoint(D)
#
#O = diskOut.segmentToArcCentre(C,D)
#dr.drawPoint(O)
#print O
#
#dr.drawPoint(Point(0,0))
#
#dr.drawArc(C,D,O)
#
#dr.close()
