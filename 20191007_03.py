while True:
	try:
		number = int(input('Enter any number '))
		print(23/number)
		break
	except ValueError:
		print('It is value error. Make sure the number you entered')
	except ZeroDivisionError:
		print('Do not input zero value')
	except:
		print('This shows becuase it means there are some error which was not caught')
	finally:
		print('This shows because it is defined by "finally statement"')
		break

