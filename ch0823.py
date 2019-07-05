========================================================================================================
To avoid code like line 33~37, there maybe a way by using join function in string container.
========================================================================================================
8.23 LAB: Replacement words
Write a program that replaces words in a sentence. The input begins with word replacement pairs (original and replacement). The next line of input is the sentence where any word on the original list is replaced.

Ex: If the input is:

automobile car   manufacturer maker   children kids
The automobile manufacturer recommends car seats for children if the automobile doesn't already have one.
the output is:

The car maker recommends car seats for kids if the car doesn't already have one. 
You can assume the original words are unique.
========================================================================================================


''' Type your code here. '''
myinput = input()
myinput2 = list(map(str, myinput.split()))
mydic1 = {}
i = 0
while i < len(myinput2):
    mydic1[myinput2[i]] = myinput2[i+1]
    i += 2
#print(mydic1)

mysentence = input()
mysentence2 = list(map(str, mysentence.split()))
#print(mysentence2)
#print(len(mydic1.keys()))

for i in mydic1.keys():
    j = 0
    while j < len(mysentence2):
        if mysentence2[j] == i:
            mysentence2[j] = mydic1[i]
        j += 1
j = 0
while j < len(mysentence2)-1:
    print(mysentence2[j], end=' ')
    j += 1
print(mysentence2[j])
