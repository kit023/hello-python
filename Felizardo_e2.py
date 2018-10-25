import sys


print = sys.argv[1]

print = float(print)

if x >=220:
print (x, "Super Typhoon")
elif x >=118:
print (x, "Typhoon")
elif x >=89:
print (x, "Severe Tropical Storm")
elif x >=62:
print (x, "Tropical Storm")
elif x <=61:
print (x, "Tropical Depression")
