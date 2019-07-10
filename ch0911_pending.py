# Type code for classes here
class ItemToPurchase:
    def __init__(self):
        item_name = "none"
        item_price = 0
        item_quantity = 0

if __name__ == "__main__":
    # Type main section of code here
    i = 1
    while i < 3:
        print('Item %d' % i)
        myitem = input('Enter the item name:\n')
        myprice = float(input('Enter the item price:\n'))
        myquantity = int(input('Enter the item quantity:\n'))
        myitem = ItemToPurchase()
        myitem.item_name = myitem
        myitem.item_price = myprice
        myitem.item_quantity = myquantity
        print()
        i += 1
    
