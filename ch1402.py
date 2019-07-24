def find(l, h):
	mid = (h-l)/2 + l
	answer = input('Is it %d (l/ h/ y): ' % mid)

	if (answer!= 'l') and (answer != 'h'):
		print('Go it!')
	else:
		if answer == 'l':
			find(l, mid)
		else:
			find(mid+1, h)

print("Choose a number from 0 to 100.")
print('Answer with:')
print('	l (your num is lower)')
print('	h (your num is higher)')

find(0,100)
