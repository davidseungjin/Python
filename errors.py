#print('Enter something to make error. should be string')
#x = int(input())
#print(x)

#print(y)

#z = x + 'string'

current_salary = int(input('Enter current salary:'))
raise_percentage = 5 # this is wrong information.
#right_percentage = 5% <== % seems not to be allowed.
right_percentage = 0.05

new_salary = current_salary + (current_salary * raise_percentage)
new_salary2 = current_salary + (current_salary * right_percentage)

print('New salary:', new_salary)
print('New salary2:', new_salary2)
print('New salary with int value is:', int(new_salary2))


#Syntax Error The program contains invalid code that cannot be understood
#Indentation error: the lines of the program are not properly indented
#Value error: An invalid value is used - can occur if giving letters to int()
#Name error: the program tries to use a variable that does not exist
#Type error: An operation uses incorrect types - can occur if adding an integer to a string.

