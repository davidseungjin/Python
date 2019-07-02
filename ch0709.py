7.9 LAB: Mad Lib - loops
Mad Libs are activities that have a person provide various words, which are then used to complete a short story in unexpected (and hopefully funny) ways.

Write a program that takes a string and integer as input, and outputs a sentence using those items as below. The program repeats until the input string is quit.

Ex: If the input is:

apples 5
shoes 2
quit 0
the output is:

Eating 5 apples a day keeps the doctor away.
Eating 2 shoes a day keeps the doctor away.
Note: This is a lab from a previous chapter that now requires the use of a loop.

''' Type your code here. '''
input_string = input()
while input_string[0:4] != 'quit':
    mylist=input_string.split()
    print('Eating {1} {0} a day keeps the doctor away.'.format(mylist[0], mylist[1]))
    input_string = input()

