=======================================================================================================
mylist.sort() or mylist2 = sorted(mylist)
=======================================================================================================
8.24 LAB: Warm up: People's weights (Lists)
(1) Prompt the user to enter four numbers, each corresponding to a person's weight in pounds. Store all weights in a list. Output the list. (2 pts) 

Ex:

Enter weight 1:
236.0
Enter weight 2:
89.5
Enter weight 3:
176.0
Enter weight 4:
166.3
Weights: [236.0, 89.5, 176.0, 166.3]
(2) Output the average of the list's elements with two digits after the decimal point. Hint: Use a conversion specifier to output with a certain number of digits after the decimal point. (1 pt)

(3) Output the max list element with two digits after the decimal point. (1 pt) 

Ex:

Enter weight 1:
236.0
Enter weight 2:
89.5
Enter weight 3:
176.0
Enter weight 4:
166.3
Weights: [236.0, 89.5, 176.0, 166.3]

Average weight: 166.95
Max weight: 236.00
(4) Prompt the user for a number between 1 and 4. Output the weight at the user specified location and the corresponding value in kilograms. 1 kilogram is equal to 2.2 pounds. (3 pts) 


Ex:

Enter a list location (1 - 4):
3
Weight in pounds: 176.00
Weight in kilograms: 80.00
(5) Sort the list's elements from least heavy to heaviest weight. (2 pts) 


Ex:

Sorted list: [89.5, 166.3, 176.0, 236.0]
=======================================================================================================



# FIXME (1): Prompt for four weights. Add all weights to a list. Output list.
i = 0
mylist = []
while i < 4:
    a = float(input('Enter weight %d:' % (i+1)))
    mylist.append(a)
    i += 1
    print()
print('Weights: ', end='')
print(mylist)

# FIXME (2): Output average of weights.
print()
print('Average weight: ', end='')
print(sum(mylist)/len(mylist))

# FIXME (3): Output max weight from list.

print('Max weight: %0.2f' % (max(mylist)))
    

# FIXME (4): Prompt the user for a list index and output that weight in pounds and kilograms.
print()
myselection = int(input('Enter a list location (1 - 4):\n'))
print('Weight in pounds: %0.2f' % (mylist[myselection-1]))
print('Weight in kilograms: %0.2f' % (mylist[myselection-1]/2.2))

# FIXME (5): Sort the list and output it.
print()
#mylist.sort()
mylist2 = sorted(mylist)

print('Sorted list:', mylist2)
