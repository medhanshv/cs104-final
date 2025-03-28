'''
    Geometry (Complex and Polar)
    Author: Saksham Rathi
'''
import math
from complex import Complex
from polar import Polar

# import the classes


def modulus(c:Complex):
    '''return modulus of the complex number'''
    return abs(((c.x)**2+(c.y)**2)**0.5)

    

def arg(c:Complex):
    '''return arg (angle) of the complex number'''
    if(c.x != 0):
        if(c.y==0):
            if(c.x>0): return 0
            if(c.x<0): return math.pi
        return math.atan2(c.y,c.x)
    else:
        if c.y>0: return math.pi/2
        elif c.y<0: return -math.pi/2
    

def abscissa(p:Polar):
    '''return abscissa of the polar point'''
    return math.cos(p.t)*(p.r)
    

def ordinate(p:Polar):
    '''return ordinate of the polar point'''
    return math.sin(p.t)*(p.r)
    

def distance(z1:Complex, z2:Complex):
    '''distance between points'''
    return abs(((z1.x-z2.x)**2+(z1.y-z2.y)**2)**0.5)
    

if __name__ == '__main__':

    # you can use this area of code to check all the functions manually
    # one example of using the functions has been shown
    # run this using "python3 main.py"
    a = Complex(1,2)
    b = Complex(2,2)
    z = a + b # uses the overloaded add
    print(z)
    # print(modulus(z)) # you can call after you implement
    x = Polar(2,math.pi/3) # uses the overloaded power
    print(x ** 2)
