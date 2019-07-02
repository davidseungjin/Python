7.8 LAB: Count characters
Write a program whose input is a string which contains a character and a phrase, and whose output indicates the number of times the character appears in the phrase.

Ex: If the input is:

n Monday
the output is:

1
Ex: If the input is:

z Today is Monday
the output is:

0
Ex: If the input is:

n It's a sunny day
the output is:

2
Case matters.

Ex: If the input is:

n Nobody
the output is:

0
n is different than N.

''' Type your code here. '''
input_string = input()
input_char = input_string[0]
input_string = input_string[2:]
num_char = input_string.count(input_char)
print(num_char)
