8.17 LAB: Varied amount of input data
Statistics are often calculated with varying amounts of input data. Write a program that takes any number of integers as input, and outputs the average and max.

Ex: If the input is:

15 20 0 5
the output is:

10 20


''' Type your code here. '''
myinput = input()
mylist2 = myinput.split()
mylist = []

for i in mylist2:
    mylist.append(int(i))

sum=0
for i in range(len(mylist)):
    sum += mylist[i]

average = sum // len(mylist)

print(average, max(mylist))
