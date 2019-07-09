def sandwich(bread, meat, *args):
	print('%s on %s' % (meat, bread), end=' ')
	if len(args) > 0:
		print('with', end=' ')
	for extra in args:
		print(extra, end=' ')
	print("")

sandwich('sourdough', 'turkey', 'mayo')
sandwich('wheat', 'ham', 'mustard', 'tomato', 'lettuce')

print()
print()

def sandwich2(bread, meat, **kwargs):
	print('%s on %s' % (bread, meat))
	for category, extra in kwargs.items():
		print('  %s: %s' % (category, extra))

sandwich2('sourdough', 'turkey', sauce = 'mayo')
sandwich2('wheat', 'ham', sauce1 = 'mustard', veggie1='tomato', veggie2='lettuce')

