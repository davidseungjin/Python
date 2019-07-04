x = 500 + 500
y = 1000
z = x

if z is x:
    print("z and x are bound to the same object")
if z is y:
    print("z and y are same")
if z == x:
    print("z and x are same")
if z == y:
    print("z and y are same")
if id(z) == id(x):
    print("variable z and x are located in the same memory address")
if id(z) == id(y):
    print("variable z and y are located in the same memory address")
