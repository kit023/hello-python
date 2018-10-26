# FUNCTIONS

# def square(x):
#     return x*x 

# for y in range(10):
#     print("{}**2 =={}"
#          .format(y, square(y)))    

import math
def area_circle (radius):
    return math.pi * radius **2

data = input("Enter the radius of"+
       "a circle:")

radius =float(data)       

print("Area of the circle: {}".format(data))       
