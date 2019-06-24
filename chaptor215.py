import math

a = float(input('what is the input value 1?'))
b = float(input('what is the input value 2?'))
c = float(input('what is the input value 3?'))

x = math.sqrt(a)
y = abs(b-c)
z = math.factorial(math.ceil(c))

print('%0.2f %0.2f %0.2f' % (x,y,z))

