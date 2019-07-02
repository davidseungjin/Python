7.11 LAB: Acronyms
An acronym is a word formed from the initial letters of words in a set phrase. Write a program whose input is a phrase and whose output is an acronym of the input. If a word begins with a lower case letter, don't include that letter in the acronym. Assume there will be at least one upper case letter in the input.

Ex: If the input is:

Institute of Electrical and Electronics Engineers
the output is:

IEEE

''' Type your code here. '''
original_string = input()
mylist = original_string.split()
new_result = ''
for i in range(len(mylist)):
    if mylist[i][0].isupper():
        new_result += mylist[i][0]
print(new_result)
