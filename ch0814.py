num_cal = dict(coke = 90, coke_zero=0, pepsi = 94)
for soda, calories in num_cal.items():
	print(soda, calories)

print()
for soda in num_cal.keys():
	print(soda)

print()
for soda in num_cal.values():
	print(soda)

solar_dist = dict(mars = 219.7e6, venus = 116.4e6, jupiter = 546e6, pluto = 2.95e9)
list_of_dist = list(solar_dist.values())

sorted_dist = sorted(list_of_dist)
closest = sorted_dist[0]
next_closest = sorted_dist[1]

print('Closest is %.5e' % closest)
print('Second closest is %.5e' % next_closest)

