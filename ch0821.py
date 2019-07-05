8.21 LAB: Word frequencies
Write a program that reads a list of words. Then, the program outputs those words and their frequencies.

Ex: If the input is:

hey hi Mark hi mark
the output is:

hey 1
hi 2
Mark 1
hi 2
mark 1


"""
===================================
This is not for exact match. count +1 for searching 'a' in 'bread'.
===================================
''' Type your code here. '''
myinput = input()
myinput2 = list(map(str, myinput.split()))
for i in myinput2:
    print(i, end=' ')
    print(myinput.count(i))
===================================
"""

''' Type your code here. '''
myinput = input()
myinput2 = list(map(str, myinput.split()))
mycount = []
for i in range(len(myinput2)):
    count = 0
    for j in range(len(myinput2)):
        if myinput2[i] == myinput2[j]:
            count += 1
        #mycount.append(count)
    print(myinput2[i], count)
