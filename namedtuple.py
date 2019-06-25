from collections import namedtuple

Car = namedtuple('Car', ['make', 'model', 'price', 'horsepower', 'seats'])

chevy_blazer = Car('Chevrolet', 'Blazer', 32000, 275, 8)
chevy_impala = Car('Chevrolet', 'Impala', 37495, 305, 5)

print(chevy_blazer)
print(chevy_impala)

print(chevy_blazer.model)
print(chevy_blazer[1])

