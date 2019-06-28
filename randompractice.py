import random

command_quit = 'a'

while command_quit != 'q':
	a = random.randint(0,5)
	print(a)
	print()
	command_quit = input("Input new command_quit to be:")

