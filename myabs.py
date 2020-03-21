def my_abs(number):
    """
    returns the absolute value of any number.

    number" an int.
    """
    #the above is called docstring
    if number < 0:
        return 0 - number
    else:
        return number

def main():
    #wrap test code in this function
    a = -10
    abs_a = my_abs(a)
    print(abs_a)
    
    #print(my_abs (-10))

if __name__ == '__main__':
    # this will only be excuted when running this file
    main ()