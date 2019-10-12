import sys
import re
from collections import Counter

f = open(sys.argv[1], 'r')
line = f.readline()
mylist = []
mylist2 = []

while line:
	line = line.lower()
	line = line.replace("\n", "")
	line = re.sub(r"[,@{}():;/.=]","",line)
	result = re.split(r"\s+", line, flags = re.I)
	for i in result:
		mylist.append(i)
	line = f.readline()

	print('result in while loop is', result)
print('result outside of while loop is ', result)
print('mylist[0] is', mylist[0])
print('mylist is', mylist)

print('count test', mylist.count("david"))

"""
for i in mylist:
	if i not in mylist2:
		mylist2.append(i)
		print(f'{i} in mylist count is {mylist.count(i)}')
"""

for i, val in enumerate(mylist):
	if i not in enumerate(mylist2):
		val = mylist.count(i)
		mylist2.append((i, val))


print('mylist2 is ', mylist2)
print(Counter(mylist))			#collection library

f.close()
