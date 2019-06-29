<<<<<<< HEAD
def modify(my_list):
	my_list[1] = 99


my_list = [10, 20, 30]
modify(my_list)
print('my_list is', my_list) #my_list still contains 99!

def modify(my_list2):
	my_list2[1] = 99

my_list2 = [10, 20, 30]
modify(my_list2[:]) # Pass a copy of the list

print('my_list2 is', my_list2)


def modify(my_list3):
	my_list3[1] = 99
	return my_list3

my_list3 = [10, 20, 30]
modify(my_list3[:]) # Pass a copy of the list

print('my_list3 is', my_list3)
print('modify(my_list3) is', modify(my_list3[:]))
=======

''' Your solution goes here '''
def swap(a):
    lastindex=0
    for i in a:
        lastindex += 1
        #print('lastindex is', lastindex)
    temp = a[0]
    a[0] = a[lastindex-1]
    a[lastindex-1] = temp
    
values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)
>>>>>>> be8b1a86d6b6777a71a68f0aaa5c582c521a595d
