import sys

f = file(sys.argv[1])
line = f.readline()

while line:
	result = line.split(";")
	line = f.readline()

	print result
