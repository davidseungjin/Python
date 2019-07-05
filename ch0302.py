mylist = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e', 'c', 'c', 'd', 'b', 1, 2, 3, 4, 5]

print('mylist is ', mylist)

mylist.pop(0)

print('mylist is ', mylist)

print("mylist count 'c' is ", mylist.count('c'))
print('mylist count 1 is ', mylist.count(1))

mylist.remove('c')
mylist.remove('c')

print('mylist is ', mylist)

mytuple = (1.2345, 6.7890)
print(mytuple)

from collections import namedtuple

Car = namedtuple('Car', ['make','model','price','horsepower','seats'])  # Create the named tuple

chevy_blazer = Car('Chevrolet', 'Blazer', 32000, 275, 8)  # Use the named tuple to describe a car
chevy_impala = Car('Chevrolet', 'Impala', 37495, 305, 5)  # Use the named tuple to describe a different car

print(chevy_blazer)
print(chevy_impala)


myset1 = set([1,2,3])
myset2 = {1,2,3}

print('myset1 is ', myset1)
print('myset2 is', myset2)
print(id(myset1))
print(id(myset2))

myset1.add(4)
print('myset1 is ', myset1)
print('myset2 is', myset2)

#myset1.pop(0) <====== it is impossible because set is unordered.

myset1.add(4)
print('myset1 is ', myset1)

myset3 = {3, 4, 5}

print('difference of myset3 from myset2 is', myset3.difference(myset2))
print('symm diff between myset 3 and 2 is', myset3.symmetric_difference(myset2))

mydic1 = {'David':10, 'Abraham':20, 'Aaron':30}
print('mydic1 is', mydic1)
print('mydic1 David's value is ', mydic1['David'])

mydic1['David'] = 5

