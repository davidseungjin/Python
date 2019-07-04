mylist = [1, 2, 3]

print(mylist)

mylist2 = list('123')
print(mylist2)

#mylist3 = mylist1 + mylist2
#print(mylist3)

mylist4 = mylist2 + [7]
print(mylist4)

mylist4[len(mylist4):] = [9]
print(mylist4)

mylist5 = mylist4[:]
print(mylist5)

#mylist6 = list(123)
#print(mylist6)
# this errors.

#mylist5.sort()
#print(mylist5)
mylist5.reverse()
print(mylist5)


