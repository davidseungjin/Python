import sys
import re

f = open(sys.argv[1], 'r')

line = f.readline()
token_list = []

while line:
	line = line.replace("\n", "")
	line = re.split(r'\b[ \t]', line.lower())
	token_list.append(line)
	line = f.readline()
print(line)
print('token_list is', token_list)


f.close()

