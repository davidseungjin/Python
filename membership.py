# use the "in" operator

fc_roster = ['David', 'Aaron', 'Davis', 'Steve', 'Sae']

name = input('Enter name to check: ')

if name in fc_roster:
	print('Founr', name, 'on the roster.')
else:
	print('Could not find', name, 'on the roster.')


#use the "not in" operator

name2 = input('Enter name to check: ')

if name2 not in fc_roster:
	print('Could not find', name, 'on the roster.')
else:
	print('Found', name2, 'on the roster.')

# in operator can be used to find substring.

substring = 'Get index.html HTTP/1.1'

req = input('Enter substring you want to check ')

if req in substring:
	print(req,'is in the string', substring)
else:
	print(req,'is not found in the string', substring)

my_dict = {'A':1, 'B':2, 'C':3}

selection = input('Choose one letter')

if selection in my_dict:
	print('Found', selection, 'in the dictionary', my_dict)
else:
	print(selection, "is not found")

