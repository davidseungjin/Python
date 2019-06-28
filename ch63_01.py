def c_to_f(c):
	return c * 9 / 5 + 32

temp_c = float(input('Enter temperature in Celsius: '))
temp_f = None

temp_f = c_to_f(temp_c)

print()
print('Fahrenheit: ', temp_f)

