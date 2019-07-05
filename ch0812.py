user_input = input()
entries = user_input.split(',')
country_capital = dict(pair.split(':') for pair in entries)
# country_capital is now a dictionary, Ex. { 'Germany': 'Berlin', 'France': 'Paris' }

''' Your solution goes here '''
del country_capital['Prussia']

print('Prussia deleted?', end=' ')
if 'Prussia' in country_capital:
    print('No.')
else:
    print('Yes.')

print ('Spain deleted?', end=' ')
if 'Spain' in country_capital:
    print('No.')
else:
    print('Yes.')

print ('Togo deleted?', end=' ')
if 'Togo' in country_capital:
    print('No.')
else:
    print('Yes.')
