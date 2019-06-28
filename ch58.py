num_rows = int(input())
num_cols = int(input())

"""
i = 1
for i in range(1, num_rows+1):
	j = 'a'
#	print(type(j))
#	print(ord(j))
	for j in range(1, num_cols+1):
		print('%s%s' % (i, j), end=' ')
		print(type(j))
	#	j = chr(ord(j)+1)
"""

i = 1
for i in range(1, num_rows+1):
	ch = 'A'
	j = 0
	print()
	while j < num_cols:
		print('%s%s' % (i, ch), end=' ')
		ch = chr(ord(ch)+1)
		j += 1
print()
