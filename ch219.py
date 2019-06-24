item_name = input('Enter food item name:\n')

# FIXME (1): Finish reading item price and quantity, then output a receipt

item_price1 = float(input('Enter item price:\n'))
item_quantity1 = int(input('Enter item quantity:\n'))
item_total1 = item_price1 * item_quantity1

print('\nRECEIPT')
print(item_quantity1, item_name,'@ $', end='')
print('%0.2f' % item_price1,'= $', end='')
print('%0.2f' % item_total1)

print('Total cost:','$', end='')
print('%0.2f' % item_total1)


# FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt
print('\n')
item_name2 = input('Enter second food item name:\n')
item_price2 = float(input('Enter item price:\n'))
item_quantity2 = int(input('Enter item quantity:\n'))
item_total2 = item_price2 * item_quantity2

grand_total = item_total1 + item_total2

print('\nRECEIPT')
print(item_quantity1, item_name,'@ $', end='')
print('%0.2f' % item_price1,'= $', end='')
print('%0.2f' % item_total1)

print(item_quantity2, item_name2,'@ $', end='')
print('%0.2f' % item_price2,'= $', end='')
print('%0.2f' % item_total2)

print('Total cost:','$', end='')
print('%0.2f' % grand_total)

# FIXME (3): Add a gratuity and total with tip to the second receipt


gratuity = 0.15 * grand_total
print('\n15% gratuity: $', end='')
print('%0.2f' % gratuity)

grand_total_incl_tip = grand_total + gratuity
print('Total with tip: $', end='')
print('%0.2f' % grand_total_incl_tip)
