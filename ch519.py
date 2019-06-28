
num1 = int(input())
denominator = 11
remainder = num1 % denominator

if (num1 < 20) or (num1 > 98):
	print('Input must be 20-98')
else:
	for i in range(remainder + 1):
		print(num1)
		num1 -= 1

