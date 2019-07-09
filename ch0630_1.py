mystring = 'David is a man'

print((mystring))

print((mystring.strip()))


user_input = '    david is my name. as usual.      i am the person.'

print('user_input is', user_input)

mylist = list(map(str, user_input.split('.')))

mylist2 = []

for i in range(len(mylist)):
	mylist2.append(mylist[i].lstrip().capitalize())

capitalized_text = mylist2[0]

mylist1 = []

i=0
while i < len(mylist):
	j=0
	while j < len(mylist[i]):
		print('mylist[%d][%d] is %s' % (i, j, mylist[i][j]))
		if ((mylist[i][j] != " ") and (mylist[i][j].islower())):
			mylist1.append(mylist[i][j].upper())
			print('condition satisfied. index[%d][%d]' % (i, j))
			print('upper is', mylist[i][j].upper())
			break
		else:
			mylist1.append(mylist[i][j])	
		j += 1
	i += 1

print('mylist1 copied from mylist is', mylist)

#for i in range(len(mylist)):


print('mylist is', mylist)
print('mylist1 is', mylist1)
print('mylist2 is', mylist2)

print('capitalized text first sentence is', capitalized_text)

