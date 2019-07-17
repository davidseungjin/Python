user_input = ''
while user_input != 'q':
	try:
		weight = int(input('Enter weight (in pounds): '))
		if weight < 0:
			raise ValueError('Invalid weight.')

		height = int(input('Enter height (ion inches): '))
		if height <= 0:
			raise ValueError('Invalid height.')

		bmi = (float(weight) / float(height * height)) * 703
		print('BMI: ', bmi)
		print('(CDC: 18.6~24.9 normal)\n')

	except ValueError as excpt:
		print(excpt)
		print('Could not calculate health info. \n')

	user_input = input("Enter any key ('q' to quit): ")


