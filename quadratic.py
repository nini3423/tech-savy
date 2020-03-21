import math

def quadratic(a, b, c):
    d = (b**2) - (4*a*c)
    if d >= 0:
        return (-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a)
    else: 
        print('No Real Solution.')
        return None

    a = float(input("a="))
    b = float(input("b="))
    c = float(input("c="))
    print('Results are:', quadratic (a, b, c))

print(quadratic(1, 2, 1))