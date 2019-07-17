print('Opening file test.txt.')
f = open('test.txt')  # create file object

print('Reading file test.txt.')
contents = f.read(10)  # read file text into a string
# number between parentheses is byte to read

print('Closing file test.txt.')
f.close()  # close the file

print('\nContents of test.txt:\n', contents)


print('the other files')
myfile = open('test2.txt')
lines = myfile.readlines(3)
print('lines[0] is', lines[0])

