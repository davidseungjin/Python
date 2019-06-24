x = int(input('Enter 3-digit number'))

ones_digit = x % 10
tmp = x // 10

tens_digit = tmp % 10
tmp // 10

hundreds_digit = tmp % 10

print('hundreds digit is', hundreds_digit,'and tens digit is',tens_digit,'and ones digit is', ones_digit)

