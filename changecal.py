''' Type your code here. '''
amount = int(input())

num_dollar = amount // 100
num_quarter = (amount % 100) // 25
num_dime = ((amount % 100) % 25 ) // 10
num_nickel = (((amount % 100) % 25) % 10) // 5
num_penny = ((((amount % 100) % 25) % 10) % 5)

if (num_dollar > 0):
    print('%d dollars' % num_dollar) if (num_dollar >= 2) else print('%d dollar' % num_dollar)
if num_quarter > 0:
    print('%d quarters' % num_quarter) if (num_quarter >= 2) else print('%d quarter' % num_quarter)
if num_dime > 0:
    print('%d dimes' % num_dime) if (num_dime >= 2) else print('%d dime' % num_dime)
if num_nickel > 0:
    print('%d nickels' % num_nickel) if (num_nickel >= 2) else print('%d nickel' % num_nickel)
if num_penny > 0:
    print('%d pennies' % num_penny) if (num_penny >= 2) else print('%d penny' % num_penny)
if num_dollar == num_quarter == num_dime == num_nickel == num_penny == 0 :
    print('no change')
