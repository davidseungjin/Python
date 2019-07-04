mytuple1 = (1,2,3,4,5)
print(mytuple1)

from collections import namedtuple

car = namedtuple('car', ['make', 'model', 'price', 'horsepower', 'seats'])

chevy_blazer = car('Chevrolet', 'Blazer', 32000, 275, 8)

print(chevy_blazer)
