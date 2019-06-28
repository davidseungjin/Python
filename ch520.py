''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

''' Type your code here. '''
solution_x = -10000
solution_y = -10000

for x in range(-10,11,1):
    for y in range(-10,11,1):
        if(a*x+b*y == c) and (d*x+e*y == f):
            solution_x = x
            solution_y = y
if solution_x == -10000 and solution_y == -10000:
    print('No solution')
else:
    print(solution_x, solution_y)
