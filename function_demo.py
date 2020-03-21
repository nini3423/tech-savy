#defining a function
def double (a):
    return 2*a
    #print('The result is, ', 2 * a)
#result = double(10)
#print(result) #f'THe result of the function with argument 10 is {result}. ')


#import myabs
from myabs import my_abs

b = -42
#abs_b = myabs.my_abs(b)
abs_b = my_abs(b)
print(abs_b)