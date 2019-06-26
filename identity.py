x = 500 + 500
y = 500 + 500 
z = x

print('id(x) is ', id(x))
print('id(y) is ', id(y))
print('id(z) is ', id(z))

if z is x:
	print('z and x are bound to the same object.')
if z is not y:
	print('z and y are not the same object.')

