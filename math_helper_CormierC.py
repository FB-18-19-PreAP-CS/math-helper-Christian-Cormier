#http://ocw.uci.edu/lectures/math_1a1b_precalculus_circle_equations.html  circle equation
#distance
#midpoint formula
#quadratic formula
#sphere formula

import math

def distance(x,x2,y,y2):
    '''
        returns the unsimplified istance of 2 points in root form
        
        >>> distance(2,4,4,2)
        the distance is root 8
        
        >>> distance(5,3,9,7)
        the distance is root 8
        
        >>> distance(9,3,10,6)
        the distance is root 52
        
        >>> distance(-2,-6,4,9)
        the distance is root 41
        
        >>> distance(10,20,10,30
        the distance is root 500
        
    '''
    
    d = (x2-x)**2+(y2-y)**2
    return(f'root {d}')
    
def quadratic(a,b,c):
    '''
    finds the solutions to a quadratic equation of
    the form ax^2 + bx + c = 0
    
    >>> quadratic(1,2,1)
    1.00,-1.00
    >>> quadratic(3,7,-6)
    .67,-3.00
    >>> quadratic(6,-7,-3)
    1.50,-0.33
    >>> quadratic(1,8,9)
    -1.35,-6.65
    >>> quadratic(-6,-6,9)
    -1.82,0.82
    '''
    
    q1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    q2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

    return(f'{q1:.2f},{q2:.2f}')

    
def midpoint(x1,x2,y1,y2):
    '''
    finds the midpoint of 2 points
    
    >>> midpoint(1,1,2,2)
    (1.0,2.0)
    
    >>> midpoint(4,2,7,2)
    (3.0,4.5)
    
    >>> midpoint(9,6,8,1)
    (7.5,4.5)
    
    >>> midpoint(-4,-7,4,7)
    (-5.5,5.5)
    
    >>> midpoint(9,5,0,2)
    (7.0,1.0)
    '''
    x = (x1 + x2)/2
    y = (y1 + y2) / 2
    ans = float(x)
    ans2 = float(y)
    hi = str(ans)
    hi2 = str(ans2)
    return(f'({x:.1f},{y:.1f})')
    
def circle(r):
    '''
    finds the area of a circle using 3.14 for pi
    
    >>> circle(4)
    the area of the circle is 50.24
    
    >>> circle(2)
    the area of the circle is 12.16
    
    >>> circle(5)
    the area of the circle is 78.5
    
    >>> circle(-3)
    no negative radius allowed
    
    >>> circle(93)
    27157.86
    
    '''
    r2 = r**2 * 3.14
    return(round(r2,2))

def sphere(r):
    '''
    finds the volume of a sphere
    >>> sphere(4)
    267.95
    
    >>> sphere(3)
    113.04
    
    >>> sphere(89)
    2951470.21
    
    >>> sphere(0)
    0.0
    
    >>> sphere(10)
    4186.67
    '''
    r2 = 3.14*r**3
    r3 = (4/3) * r2
    return(round(r3,2))



def run_dist():
    print("You selected distance.")
    x1= int(input("Enter your first x coordinate: "))
    x2= int(input("Enter your second x coordinate: "))
    y1= int(input("Enter your first y coordinate: "))
    y2= int(input("Enter your second y coordinate: "))
    print("The distance is {}".format(distance(x1,x2,y1,y2)))
    
def run_quad():
    print("you selected quadratic")
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = int(input("enter c: "))
    if a == 0:
        print("the denominator cant be 0")
        run_quad()
    else:
        print("the quadratic is {}".format(quadratic(a,b,c)))
    
def run_circ():
    print("You selected area of a circle.")
    r= int(input("Enter the radius: "))
    if r < 0:
        print("no negative radius allowed")
        run_circ()
    elif r >= 0:
        print("The area of the circle is {}".format(circle(r)))
    
    
def run_mid():
    print("You selected midpoint.")
    x1= int(input("Enter your first x coordinate: "))
    x2= int(input("Enter your second x coordinate: "))
    y1= int(input("Enter your first y coordinate: "))
    y2= int(input("Enter your second y coordinate: "))
    print("The midpoint is {}".format(midpoint(x1,x2,y1,y2)))
    
def run_sphere():
    print("You selected volume of a sphere.")
    r= int(input("Enter the radius: "))
    print("The volume of the sphere is {}".format(sphere(r)))
    
    
def main():
    while True:
        inp = input("which formula do you want?- \n(1).distance \n(2).quadratic \n(3).midpoint \n(4).circle \n(5).sphere \n(6).quit \n-- ")
        if inp == "1":
            run_dist()
            while True:
                cont = input("do you want to continue (yes/no): ")
                print()
                if cont.lower() == "yes":
                    main()
                elif cont.lower() == "no":
                    break
                else:
                    print("Invalid input")
                    print()
            break
                
        elif inp == "2":
            run_quad()
            cont = input("do you want to continue (yes/no): ")
            print()
            if cont.lower() == "yes":
                main()
            elif cont.lower() == "no":
                break
            
        elif inp == "3":
            run_mid()
            cont = input("do you want to continue (yes/no): ")
            if cont.lower() == "yes":
                main()
            elif cont.lower() == "no":
                break
            
        elif inp == "4":
            run_circ()
            cont = input("do you want to continue (yes/no): ")
            if cont.lower() == "yes":
                main()
            if cont.lower() == "no":
                break
        elif inp == "5":
            run_sphere()
            cont = input("do you want to continue (yes/no): ")
            if cont.lower() == "yes":
                main()
            if cont.lower() == "no":
                break
            
        elif inp == '6':
            break
            
        else:
            print("thats not an appropriate value")
            main()
            break
        

    
    
    
if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    main()
    


