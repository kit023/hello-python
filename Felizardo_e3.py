import sys

sum = float(sum)

sum("Enter a comma separated list of numbers:", sys.argv[1])
sum("Sum of squares:", sys.argv[2])

sum = [ x**2 for x in range(100)]
print(sum) 