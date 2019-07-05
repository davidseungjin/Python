======================================================================
LOOK. IS THERE SOMETHING ELSE I CAN MAKE THE CODE MUCH EASIER TO READ?
OR SOME OTHER WAY TO MAKE DICTIONARY MORE STRAIGITFORWARD
======================================================================

8.22 LAB: Contact list
A contact list is a place where you can store a specific contact with other associated information such as a phone number, email address, birthday, etc. Write a program that first takes in word pairs that consist of a name and a phone number (both strings). That list is followed by a name, and your program should output the phone number associated with that name.

Ex: If the input is:

Joe 123-5432 Linda 983-4123 Frank 867-5309
Frank
the output is:

867-5309


''' Type your code here. '''
myinput = input()
myentry = list(map(str, myinput.split()))
print(myentry)
mydic = {}
i = 0
while i < len(myentry):
    mydic[myentry[i]] = myentry[i+1]
    i += 2

print(mydic)
mysearch = input()
print(mydic[mysearch]) if mysearch in mydic else print('nothing in the list')
