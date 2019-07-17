import ch1101_1

n = int(input('Enter number: '))
fact = ch1101_1.factorial(n)

for i in range(1, n+1):
	print(i, end= ' ')
	if i != n:
		print('*', end=' ')

print('=', fact)

