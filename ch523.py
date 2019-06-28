"""
5.23 LAB: Adjust values in a list by normalizing
When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data. This can be done by normalizing to values between 0 and 1, or throwing away outliers.

Write a program that first gets a list of integers from input. The input begins with an integer indicating the number of integers that follow. Then, adjust each integer in the list by subtracting the smallest value from all the integers.
"""


''' Type your code here. '''
num_item = int(input())
mylist = []
min_var = 1e10
for i in range(num_item):
    a = int(input())
    mylist.append(a)
    if a < min_var:
        min_var = a
for i in range(num_item):
    print(mylist[i]-min_var)

