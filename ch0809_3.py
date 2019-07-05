"""
names = []
prompt = 'Enter name: '

user_input = input(prompt)

while user_input != 'exit':
	names.append(user_input)
	user_input = input(prompt)

no_key_sort = sorted(names)
key_sort = sorted(names, key = str.lower)

print('Sorting without key: ', no_key_sort)
print('Sorting with key: ', key_sort)
"""

my_list = [[25], [15, 25, 35], [10, 40]]

sorted_list = sorted(my_list, key=max)

print('Sorted list: ', sorted_list)

mylist = [1, 5, 10, 20]
mylist2 = sorted(mylist, reverse = True)

print(mylist)
print(mylist2)

