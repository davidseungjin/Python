"""
6.27 LAB: Even/odd values in a list
Write a program that reads a list of integers, and outputs whether the list contains all even numbers, odd numbers, or neither. The input begins with an integer indicating the number of integers that follow.

Ex: If the input is:

5
2
4
6
8
10
the output is:

all even
Ex: If the input is:

5
1
3
5
7
9
the output is:

all odd
Ex: If the input is:

5
1
2
3
4
5
the output is:

not even or odd
Your program must define and call the following two functions. is_list_even() returns true if all integers in the list are even and false otherwise. is_list_odd() returns true if all integers in the list are odd and false otherwise.
def is_list_even(my_list)
def is_list_odd(my_list)
"""





''' Define your function here '''
def is_list_even(my_list):
    num = 0
    for i in my_list:
        if (i % 2 == 0):
            num += 1
    if (num == len(my_list)):
        return True
    else:
        return False

def is_list_odd(my_list):
    num = 0
    for i in my_list:
        if (i % 2 == 1):
            num += 1
    if (num == len(my_list)):
        return True
    else:
        return False
if __name__ == '__main__':
    my_list = []
    value = 0
    num_element = int(input())
    for i in range(num_element):
        value = int(input())
        my_list.append(value)
    if is_list_even(my_list):
        print('all even')
    elif is_list_odd(my_list):
        print('all odd')
    else:
        print('not even or odd')
