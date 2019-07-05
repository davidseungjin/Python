user_input = input()
entries = user_input.split(',')
country_pop = dict(pair.split(':') for pair in entries)

for country, pop in country_pop.items():
	print(country, 'has', pop, 'people.')

