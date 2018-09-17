#http://ocw.uci.edu/lectures/math_1a1b_precalculus_circle_equations.html  circle equation
#distance
#midpoint formula
#quadratic formula
#sphere formula

import math

def distance(x,x2,y,y2):
    d = math.sqrt((x2-x)**2+(y2-y)**2)
    return d
    '''
        returns the distance of 2 points
        
        >>> distance(2,4,4,2)
        math.sqrt(8)
        
        >>>distance(5,3,9,7)
        math.sqrt(8)
        
        >>>distance(9,3,10,6)
        math.sqrt(52)
    '''
    
def main():
    pass
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #main()