house_coordinates = (135, 246)
print('Coordinates:', house_coordinates)
print('Tuple length:', len(house_coordinates))

# Access tuples via index
print('\nLatitude:', house_coordinates[0],'north')
print('Longitude:', house_coordinates[1], 'west\n')

#Error. Tuples are immutable
#house_coordinates[1] = 50

print(type(house_coordinates))
