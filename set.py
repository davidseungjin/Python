# two ways to making set. The one is to use

num1 = set([1,2,3])

num2 = {7,8,9}

print(num1)
print(num2)

print(len(num1))
num1.update(num2) #Adds the elements in num2 set to num1 set.
print(num1)

num1.add(100)
print(num1)
num1.add(2000)
print(num1)
num1.add(300)
print(num1)
num1.remove(1)
print(num1)
num1.pop()
print(num1)

