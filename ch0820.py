8.20 LAB: Elements in a range
Write a program that first gets a list of integers from input. That list is followed by two more integers representing lower and upper bounds of a range. Your program should output all integers from the list that are within that range (inclusive of the bounds).

Ex: If the input is:

25 51 0 200 33
0 50
the output is:

25 0 33 
The bounds are 0-50, so 51 and 200 are out of range and thus not output.

For coding simplicity, follow each output integer by a space, even the last one. Do not end with newline.


''' Type your code here. '''
myinput = input()
mylimit = input()
myinput2 = list(map(int, myinput.split()))
mylimit2 = list(map(int, mylimit.split()))
myinput3 = []
for i in myinput2:
    if (i >= min(mylimit2)) and (i <= max(mylimit2)):
        myinput3.append(i)

for i in myinput3:
    print(i, end=' ')
