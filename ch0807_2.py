num1 = [5, 10, 15]
num2 = [10, 15]

num3 = [5, 10, 15]
num4 = num2[:]


for val in num1:
	if val in num2:
		num1.remove(val)

print(num1)

for val in num3[:]:
	if val in num4:
		num3.remove(val)

print(num3)

