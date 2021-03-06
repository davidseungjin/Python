7.14 LAB*: Program: Data visualization
(1) Prompt the user for a title for data. Output the title. (1 pt) 

Ex:

Enter a title for the data:
Number of Novels Authored
You entered: Number of Novels Authored

(2) Prompt the user for the headers of two columns of a table. Output the column headers. (1 pt) 

Ex:

Enter the column 1 header:
Author name
You entered: Author name

Enter the column 2 header:
Number of novels
You entered: Number of novels

(3) Prompt the user for data points. Data points must be in this format: string, int. Store the information before the comma into a string variable and the information after the comma into an integer. The user will enter -1 when they have finished entering data points. Output the data points. Store the string components of the data points in a list of strings. Store the integer components of the data points in a list of integers. (4 pts) 

Ex:

Enter a data point (-1 to stop input):
Jane Austen, 6
Data string: Jane Austen
Data integer: 6

(4) Perform error checking for the data point entries. If any of the following errors occurs, output the appropriate error message and prompt again for a valid data point.

If entry has no comma
Output: Error: No comma in string. (1 pt)
If entry has more than one comma
Output: Error: Too many commas in input. (1 pt)
If entry after the comma is not an integer
Output: Error: Comma not followed by an integer. (2 pts)

Ex:

Enter a data point (-1 to stop input):
Ernest Hemingway 9
Error: No comma in string.

Enter a data point (-1 to stop input):
Ernest, Hemingway, 9
Error: Too many commas in input.

Enter a data point (-1 to stop input):
Ernest Hemingway, nine
Error: Comma not followed by an integer.

Enter a data point (-1 to stop input):
Ernest Hemingway, 9
Data string: Ernest Hemingway
Data integer: 9

(5) Output the information in a formatted table. The title is right justified with a minimum field width value of 33. Column 1 has a minimum field width value of 20. Column 2 has a minimum field width value of 23. (3 pts) 

Ex:

        Number of Novels Authored
Author name         |       Number of novels
--------------------------------------------
Jane Austen         |                      6
Charles Dickens     |                     20
Ernest Hemingway    |                      9
Jack Kerouac        |                     22
F. Scott Fitzgerald |                      8
Mary Shelley        |                      7
Charlotte Bronte    |                      5
Mark Twain          |                     11
Agatha Christie     |                     73
Ian Flemming        |                     14
J.K. Rowling        |                     14
Stephen King        |                     54
Oscar Wilde         |                      1

(6) Output the information as a formatted histogram. Each name is right justified with a minimum field width value of 20. (4 pts) 

Ex:

         Jane Austen ******
     Charles Dickens ********************
    Ernest Hemingway *********
        Jack Kerouac **********************
 F. Scott Fitzgerald ********
        Mary Shelley *******
    Charlotte Bronte *****
          Mark Twain ***********
     Agatha Christie *************************************************************************
        Ian Flemming **************
        J.K. Rowling **************
        Stephen King ******************************************************
         Oscar Wilde *


# Type your code here
mytitle = input('Enter a title for the data:\n')
print('You entered: %s' % mytitle)

myheader = []
i = 0
while i < 2:
    temp = input('\nEnter the column %d header:' % (i+1))
    myheader.append(temp)
    print('\nYou entered: %s' % myheader[i])
    i += 1
data_point = ''
mylist1 = []
mylist2 = []
i = 0

print()
data_point = input('Enter a data point (-1 to stop input):\n')
while data_point != '-1':
    #print(data_split)
    if ',' in data_point:
        data_split = data_point.split(',')
        data_split[1] = data_split[1].strip()
        if data_point.count(",") == 1:
            if data_split[1].isdigit():
                print('Data string: %s' % data_split[0])
                print('Data integer: %d' % int(data_split[1]))
                mylist1.append(data_split[0])
                mylist2.append(int(data_split[1]))
                i += 1
            else:
                print('Error: Comma not followed by an integer.')
        else:
            print('Error: Too many commas in input.')
    else:
        print('Error: No comma in string.')
    print()
    data_point = input('Enter a data point (-1 to stop input):\n')

print()
i = 0
print('%33s' % mytitle)
print('%s' % myheader[0].ljust(20, ' '), end= '')
print('|', end='')
print('%s' % myheader[1].rjust(23, ' '))
print('--------------------------------------------')
while i < len(mylist1):
    print('%s' % mylist1[i].ljust(20,' '), end='')
    print('|', end='')
    print('{:23d}'.format(mylist2[i]))
    i += 1

print()
i = 0
while i < len(mylist1):
    print('%s' % mylist1[i].rjust(20,' '), end='')
    print(' ', end='')
    print('*' * mylist2[i])
    i += 1
