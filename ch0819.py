8.19 LAB: Middle item
Given a sorted list of integers, output the middle integer. Assume the number of integers is always odd.

Ex: If the input is:

2 3 4 8 11
the output is:

4
The maximum number of inputs for any test case should not exceed 9. If exceeded, output "Too many inputs".

Hint: First read the data into a list. Then, based on the list's size, find the middle item.

''' Type your code here. '''
myinput = input()
myinput2 = list(map(int, myinput.split()))
num_mylist2 = len(myinput2)
if num_mylist2 > 9:
    print('Too many inputs')
else:
    mid_num = (num_mylist2 - 1) // 2
    print(myinput2[mid_num])
