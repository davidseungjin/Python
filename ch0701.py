
"""
abc = input('Enter string : ')
print('all character is alphabet or number?', abc.isalnum())
print('all character is number?', abc.isdigit())
print('all character is lower character alphabet?', abc.isalnum())
print('all character is upper character alphabet?', abc.isalnum())
print('all character is while space?', abc.isalnum())
print('all character starts with x ?', abc.isalnum())
print('all character ends with x?', abc.isalnum())
"""

num_people = 30
num_books = 15

if num_people == 30:
	if num_people >= 40:
		num_books = num_books * 4
	else:
		num_books = num_books * 2 
else:
	num_books = num_books - 5 
num_books = num_books + 5
print(num_books)

x = 5 * (8 % 3) / 2 + 7 * 2

print(x)

#Given:

hello_world = "Hello, World!"

for ch in hello_world: # print each character from hello_world
	print(ch)

length = 0 # initialize length variable

for ch in hello_world:
	length += 1 # add 1 to the length on each iteration
print()
print()
print()
print('length is ', length)
print()
print(len(hello_world) == length)

#what is printed at the end of this code 


nums = [1, 2, 4, 8, 16, 32]

print(nums[4])
print(nums[-1])

phrase = "I love coffee; we all love coffee.\n"
#what is the result of 

print(phrase.isupper())

