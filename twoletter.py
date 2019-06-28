"""
Program to print all s-letter domain names.

Note that ord() and chr() convert between text and the ASCII or Unicode encoding:
"""

print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
while letter1 <= 'z': #outer loop
	letter2 = 'a'
	while letter2 <= 'z':
		print('%s%s.com' % (letter1, letter2))
		letter2 = chr(ord(letter2)+1)
	letter1 = chr(ord(letter1) + 1)

