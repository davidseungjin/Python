''' Type your code here. '''
i = int(input())
max_val = -1e10
min_val = 1e10
mylist = []
while i > 0:
    mylist.append(i)
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i
    i = int(input())
#print(mylist)
print(min_val, max_val)


# Figure out there is other way than using arbitrary small number to min/max.
# Probably there is min/max built-in function. 
