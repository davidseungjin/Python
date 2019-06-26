set1 = { 1,2,3,4,5,6,7,8,9}
set2 = set(['aaa', 'bbb', 'ccc', 'ddd', 'eee'])

set2.add('fff')

set2.add(1)

print(set1)
print(set2)

seta = {1,2,3,4,5,6,7,8}
setb = {5,6,7,8,9,10,11,12}
setc = {4,6,8,10,12,14}
setd = {3,5,7,9,11,13}

abintersection = set.intersection(seta, setb)
abunion = set.union(seta, setb)
abdifferent = set.difference(seta, setb)
setsymdif = seta.symmetric_difference(setb)

print('intersection of seta and setb is ', abintersection)
print('union of seta and setb is ', abunion)
print('different is', abdifferent)
print('symmetric_difference is', setsymdif)


