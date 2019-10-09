import sys

f = open(sys.argv[1], "w")

f.write("David is now practicing how to use command augment and")
f.write("How to utilize file writing using the augment.")

f.close()

f = open(sys.argv[1], "r")
david = f.readline()
f.close()

print(david)

