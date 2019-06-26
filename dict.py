players = {'David Lee': 10, 'Abraham Lee':7}

print(players)

prices = {'apple':1.99, 'orange':2.45}
print('The price of apple is', prices['apple'])
#print('The price of lemon is', prices['lemons'])

# can I do add function without any dictionary created already?

students = {}

students['David'] = 'A+'
print(students)
students['Abraham'] = 'A+'
students['Alberton'] = 'B0'
students['Mey'] = 'C+'

print(students)
students['David'] = 'A0'

print(students)
del students['Mey']
print(students)
