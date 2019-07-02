mytitle = input('Enter a title for the data:\n')
print('You entered: %s' % mytitle)

myheader = []
i = 0
while i < 2:	
	temp = input('Enter the column %d header:\n' % (i+1))
	myheader.append(temp)
	print('You entered: %s\n' % myheader[i])
	i += 1

data_point = ''

while data_point != '-1':
	 
