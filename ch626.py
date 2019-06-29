"""
6.26 LAB: Exact change - functions
Write a program with total change amount as an integer input that outputs the change using the fewest coins, one coin type per line. The coin types are dollars, quarters, dimes, nickels, and pennies. Use singular and plural coin names as appropriate, like 1 penny vs. 2 pennies.

Ex: If the input is:

0 
or less, the output is:

no change
Ex: If the input is:

45
the output is:

1 quarter
2 dimes 
Your program must define and call the following function. The function exact_change() should return num_dollars, num_quarters, num_dimes, num_nickels, and num_pennies.
def exact_change(user_total)

Note: This is a lab from a previous chapter that now requires the use of a function.
"""



''' Define your function here '''
def exact_change(user_total):
    n_dollar = user_total // 100
    user_total %= 100
    n_quarter = user_total // 25
    user_total %= 25
    n_dime = user_total // 10
    user_total %= 10
    n_nickel = user_total // 5
    user_total %= 5
    n_penny = user_total
    return n_dollar, n_quarter, n_dime, n_nickel, n_penny

if __name__ == '__main__': 
   input_val = int(input())    
   num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
   if input_val == 0:
       print('no change')
   if num_dollars > 0:
       if num_dollars >1:
           print('%d dollars' % num_dollars)
       else:
           print('%d dollar' % num_dollars)
   if num_quarters > 0:
       if num_quarters >1:
           print('%d quarters' % num_quarters)
       else:
           print('%d quarter' % num_quarters)
   if num_dimes > 0:
       if num_dimes >1:
           print('%d dimes' % num_dimes)
       else:
           print('%d dime' % num_dimes)
   if num_nickels > 0:
       if num_nickels >1:
           print('%d nickels' % num_nickels)
       else:
           print('%d nickel' % num_nickels)
   if num_pennies > 0:
       if num_pennies >1:
           print('%d pennies' % num_pennies)
       else:
           print('%d penny' % num_pennies)
