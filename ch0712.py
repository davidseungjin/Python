7.12 LAB: Contains the character
Write a program that reads a character, then reads in a list of words. The output of the program is every word in the list that contains the character at least once. Assume at least one word in the list will contain the given character.

Ex: If the input is:

z
hello zoo sleep drizzle
the output is:

zoo
drizzle
Keep in mind that the character 'a' is not equal to the character 'A'.

''' Type your code here. '''
target_char = input()
original_string = input()
mylist = original_string.split()
for i in range(len(mylist)):
    if target_char in mylist[i]:
        print(mylist[i])
