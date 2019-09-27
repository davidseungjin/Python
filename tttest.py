i = 0
c = 0
while i <= 100:
	print(i)
	i = i + 2
	c += 1

print(c)

my_set = {1, 2, 3, 4, 5, 6}
other_set = {2, 4, 6}
result_set = other_set.difference(my_set)
print(result_set)

temperatures = [-2, 8, 4, -7, 18, 3, -1]
count = 0
for t in temperatures:
    if t<0 :
        count = count + 1
print("Total negative temperatures:", count)

x = 7
if x < 7:
    x = x + 1
x = x + 2

print(x)

