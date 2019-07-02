7.7 LAB: Name format
Many documents use a specific format for a person's name. Write a program whose input is: firstName middleName lastName, and whose output is: lastName, firstName middleInitial.

Ex: If the input is:

Pat Silly Doe
the output is:

Doe, Pat S.
If the input has the form firstName lastName, the output is lastName, firstName.

Ex: If the input is:

Julia Clark
the output is:

Clark, Julia





''' Type your code here. '''
user_input=input()
list_input=user_input.split()
show_result = ''
if len(list_input) == 2:
    show_result = list_input[-1] + ', ' + list_input[0]
else:
    show_result = list_input[-1] + ', ' + list_input[0] + ' ' + list_input[1][0].capitalize() + '.'
print(show_result)
