def factorial1(x):
	if ((x == 1) or (x == 0)):
		return 1
	else:
		return x * factorial1(x-1)

def factorial2(a, x):
	if x == 0:
		return 1
	else:
		return factorial2(a, x-1) + a/factorial1(x)

#input

#x = int(input('Enter the number x   '))
#a = float(input('Enter the number a   '))
a = 2.5
x = 0

b = ((a**x/factorial1(x))/factorial2(a,x))


while(b >= 0.02):
	print(f'when x is {x}', end=' ')
	print(f'B is {b}')
	b = ((a**x/factorial1(x))/factorial2(a,x))
	x += 1


print(a**x)
print(factorial1(x))
print(factorial2(a,x))


print('finally')
print(f'x is {x}')
print(f'B is {b}')
print("in unit of % ", b*100, "%")

