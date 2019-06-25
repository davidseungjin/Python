david = [123, 234, 'davidlee', 'abrahamlee', 345]

appendtest = david.append('appended component')

poptest = david.pop(0)

print(david)
print(appendtest)
print(poptest)

print(david)
david.remove(345)
print(david)
david.pop(1)
print(david)
print(len(david))

david2 = [111,222,333,444,'ohohoh']
print(david2)
print(len(david2))

listsum = david + david2
print(len(listsum))
print(listsum)

print(david2.count(444))

