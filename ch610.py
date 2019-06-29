employee_name = 'N/A'

def get_name():

	name = input('Enter employee name:')
	employee_name = name

get_name()
print('Employee name:', employee_name)

employee_name2 = 'N/A'

def get_name2():

	global employee_name2
# if global statement is used in a function, I can modify global variable in a function
	name = input('Enter employee name2:')
	employee_name2 = name

get_name2()
print('Employee name2:', employee_name2)

