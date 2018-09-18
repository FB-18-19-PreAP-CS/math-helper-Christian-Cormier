#http://ocw.uci.edu/lectures/math_1a1b_precalculus_circle_equations.html  circle equation
#distance
#midpoint formula
#quadratic formula
#sphere formula

import math

def distance(x,x2,y,y2):
    '''
        returns the distance of 2 points
        
        >>> distance(2,4,4,2)
        root 8
        
        >>> distance(5,3,9,7)
        root 8
        
        >>> distance(9,3,10,6)
        root 52
    '''
    
    d = (x2-x)**2+(y2-y)**2
    ans = int(d)
    hi = str(ans)
    print('root ' + hi)
    
def quadratic(a,b,c):
    '''
    gives the the quadratic form of 3 numbers
    
    >>> quadratic(1,2,3)
    
    >>> quadratic(2,4,6)
    
    >>> quadratic(9,5,12)
    
    '''
    
    q1 = (-b + math.sqrt(b)**2 - 4(a)(c)) / 2(a)
    q2 = (-b - math.sqrt(b)**2 - 4(a)(c)) / 2(a)
    print(q1,q2)
def main():
    distance(5,3,9,7)
    distance(9,3,10,6)
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()