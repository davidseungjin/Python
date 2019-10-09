import sys

f = open(sys.argv[1], 'r')
line = f.readline()

while line:
	line = line.replace("\n", "")
	result = line.split(";")
	line = f.readline()

	print(result)
