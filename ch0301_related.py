myinput = 'davidlee'
mylist1 = list('davidlee1')
mylist2 = myinput.split()
mylist3 = list(myinput)
mylistlist= [myinput, mylist1, mylist2, mylist3]
mylist4 = 1
mylist5 = 2
mylistlistlist = [mylistlist, mylist1, mylist2]

print(myinput)
print(mylist1)
print(mylist2)
print(mylist3)
print(mylistlist)

print('mylist4 is:', mylist4)
print('mylist5 is:', mylist5)
print('mylistlistlist is:', mylistlistlist)
print('mylistlistlist[0][1][2]: ', mylistlistlist[0][1][2])

print('id of mylistlistlist[0] is', id(mylistlistlist[0]))
print('id of mylistlistlist is', id(mylistlistlist))
print('id of mylistlist which is also an element of mylistlistlist[0]', id(mylistlist))


my_list = [10, 'a', 'b']
print(my_list)

my_list.append('ab')
my_list.extend(['bc', 'cd'])
print(my_list)

my_list.pop(0)
my_list.remove('a')
print(my_list)
my_list2 = ['abc', 'bcd', 'cde']
print(my_list2)

my_list += my_list2

print(my_list)
max(my_list)
print('after max', my_list)

my_list.reverse()
print('after reverse\n', my_list)

my_list.sort()
print('after sort\n', my_list)
