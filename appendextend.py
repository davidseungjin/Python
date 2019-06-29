import copy

my_list = ['David','Lee']
my_list.append('Abraham')
print('my_list is ', my_list)

another_list = [1,2,3,4]
my_list2 = copy.copy(my_list)
my_list.append(another_list)
print('my_list is ', my_list)

my_list3 = copy.deepcopy(my_list2)
print('my_list3 after deepcopying my_list2 is', my_list3)

my_list2.extend(another_list)
print('my_list2 is ', my_list2)
print('my_list is ', my_list)

my_list2.extend("EXTEND")
print('my_list2 is', my_list2)
print('my_list is ', my_list)


print('ID of my_list is', id(my_list))
print('ID of my_list2 is', id(my_list2))
print('ID of my_list3 is', id(my_list3))
