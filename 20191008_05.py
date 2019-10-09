import sys

file = open(sys.argv[1])
for line in file:
	for word in line.split():
		print(word)
