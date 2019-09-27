names = [ 'Gerry', 'Preet', 'Jimin', 'Susan' ]
index = 0
while index < len(names):
	if names[index] == 'Susan':
		break
	else:
		index += 1
else:
	print('Done')
print(index)
