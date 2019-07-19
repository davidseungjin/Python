print('Opening test.txt')

# Open a file for reading and appending
with open('test.txt', 'r+') as f:
    # Read in two integers
    str1 = f.readline()
    str2 = f.readline()

    product = str1 + str2

    # Write back result on own line
    f.write('\n')
    f.write(str(product))

# No need to call f.close() - f closed automatically 
print('Closed test.txt')
