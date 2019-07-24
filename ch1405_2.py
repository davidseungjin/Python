"""
Determine the greatest common divisor of two numbers
"""

def gcd(n1, n2):
	if n1 % n2 == 0:		#n2 is a common factor
		return n2
	else:
		return gcd(n2, n1%n2)

print('This program outputs the greatest '
		  'common divisor of two numbers.\n')

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if (num1 < 1) or (num2 < 1):
	print('Note: Neither value can be below 1.')
else:
	my_gcd = gcd(num1, num2)
	print('Greatest common divisor =', my_gcd)

