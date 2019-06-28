nose = 'O'
user_value = '-'

while user_value != 'q':
	print(' %s %s ' %(user_value, user_value))
	print('  %s  ' % nose)
	print(user_value * 5)
	print('\n')

	user_input = input("Enter a character ('q' for quit): ")
	user_value = user_input[0]

print('Gootbye.\n')

