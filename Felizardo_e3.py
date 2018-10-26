# import Felizardo_e3
# import sys

# print("Enter a comma separated list of numbers:", sys.argv[0])
# print("Sum of squares:", sys.argv[1])

# print = float("100")

add = [ x**2 for x in range(100)]
print(add) 


data = input ("Please type a message: ")
print(add) 
print("You said '{}'".format(data))

message = input ("Please type a " + 
"comma separated list of values: ")

values = message.split(",")
print("The first two elements " + 
"of your list are: {} and {}".format(values[0], values[1]))