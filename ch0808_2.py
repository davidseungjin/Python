numbers = [int(i) for i in input('Enter numbers:').split()]

even_numbers = [i for i in numbers if (i%2) ==0]
odd_numbers = [i for i in numbers if (i%2) == 1]

print('list numbers is ', numbers)
print('even list numbers is ', even_numbers)
print('off list numbers is ', odd_numbers)

