
==============================================================================================================
9.11 LAB*: Warm up: Online shopping cart (Part 1)
(1) Build the ItemToPurchase class with the following specifications:

Attributes (3 pts)
item_name (string)
item_price (float)
item_quantity (int)
Default constructor (1 pt)
Initializes item's name = "none", item's price = 0, item's quantity = 0
Method
print_item_cost()

Ex. of print_item_cost() output:

Bottled Water 10 @ $1 = $10
(2) In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class. (2 pts) 

Ex:

Item 1
Enter the item name:
Chocolate Chips
Enter the item price:
3
Enter the item quantity:
1

Item 2
Enter the item name:
Bottled Water
Enter the item price:
1
Enter the item quantity:
10

(3) Add the costs of the two items together and output the total cost. (2 pts) 

Ex:

TOTAL COST
Chocolate Chips 1 @ $3 = $3
Bottled Water 10 @ $1 = $10

Total: $13
==============================================================================================================
==============================================================================================================

# Type code for classes here
class ItemToPurchase:
    def __init__(self, name="none", price=0, quantity=0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_total = price * quantity
    def __str__(self):
        return('%s %d @ $%0.0f = $%d' % (self.item_name, self.item_quantity, self.item_price, self.item_total))


if __name__ == "__main__":
    # Type main section of code here
    i = 1
    myobj = {}
    while i < 3:
        print('Item %d' % i)
        myitem = input('Enter the item name:\n')
        myprice = float(input('Enter the item price:\n'))
        myquantity = int(input('Enter the item quantity:\n'))
        myobj[i] = ItemToPurchase(myitem, myprice, myquantity)
        #myitem.item_name = myitem
        #myitem.item_price = myprice
        #myitem.item_quantity = myquantity
        print()
        i += 1
    print('TOTAL COST')
    print(myobj[1])
    print(myobj[2])
    print()
    print('Total: $%0.0f' % (myobj[1].item_total + myobj[2].item_total))
