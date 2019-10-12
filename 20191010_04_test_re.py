import re

f = open('20191011_test.txt', 'r')
line = f.readline()
result = []

while  line:
	line = line.lower()
	line = re.sub(r'[,?!@{}():;/.=\n]', "", line)
	result = result + re.split(r'\s+', line, flags = re.I)
	print(result)
	line = f.readline()


print(line)
