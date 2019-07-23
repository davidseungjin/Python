9.12 LAB*: Program: Online shopping cart (Part 2)
This program extends the earlier "Online shopping cart" program. (Consider first saving your earlier program). 

(1) Extend the ItemToPurchase class to contain a new attribute. (2 pts)

item_description (string) - Set to "none" in default constructor
Implement the following method for the ItemToPurchase class.

print_item_description() - Prints item_description attribute for an ItemToPurchase object. Has an ItemToPurchase parameter.

Ex. of print_item_description() output:

Bottled Water: Deer Park, 12 oz.


(2) Build the ShoppingCart class with the following data attributes and related methods. Note: Some can be method stubs (empty methods) initially, to be completed in later steps.

Parameterized constructor which takes the customer name and date as parameters (2 pts)
Attributes
customer_name (string) - Initialized in default constructor to "none"
current_date (string) - Initialized in default constructor to "January 1, 2016"
cart_items (list)
Methods
add_item()
Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
remove_item()
Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
If item name cannot be found, output this message: Item not found in cart. Nothing removed.
modify_item()
Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
get_num_items_in_cart() (2 pts)
Returns quantity of all items in cart. Has no parameters.
get_cost_of_cart() (2 pts)
Determines and returns the total cost of items in cart. Has no parameters.
print_total()
Outputs total of objects in cart.
If cart is empty, output this message: SHOPPING CART IS EMPTY
print_descriptions()
Outputs each item's description. 
Ex. of print_total() output:

John Doe's Shopping Cart - February 1, 2016
Number of Items: 8

Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128

Total: $521

Ex. of print_descriptions() output:

John Doe's Shopping Cart - February 1, 2016

Item Descriptions
Nike Romaleos: Volt color, Weightlifting shoes
Chocolate Chips: Semi-sweet
Powerbeats 2 Headphones: Bluetooth headphones

(3) In main section of your code, prompt the user for a customer's name and today's date. Output the name and date. Create an object of type ShoppingCart. (1 pt) 

Ex.

Enter customer's name:
John Doe
Enter today's date:
February 1, 2016

Customer name: John Doe
Today's date: February 1, 2016

(4) Implement the print_menu() function. print_menu() has a ShoppingCart parameter, and outputs a menu of options to manipulate the shopping cart. Each option is represented by a single character. Build and output the menu within the function.

If the an invalid character is entered, continue to prompt for a valid choice. Hint: Implement Quit before implementing other options. Call print_menu() in the main() function. Continue to execute the menu until the user enters q to Quit. (3 pts) 

Ex:

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit

Choose an option:

(5) Implement Output shopping cart menu option. (3 pts) 

Ex:

OUTPUT SHOPPING CART
John Doe's Shopping Cart - February 1, 2016
Number of Items: 8

Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128

Total: $521

(6) Implement Output item's description menu option. (2 pts) 

Ex.

OUTPUT ITEMS' DESCRIPTIONS
John Doe's Shopping Cart - February 1, 2016

Item Descriptions
Nike Romaleos: Volt color, Weightlifting shoes
Chocolate Chips: Semi-sweet
Powerbeats 2 Headphones: Bluetooth headphones

(7) Implement Add item to cart menu option. (3 pts) 

Ex:

ADD ITEM TO CART
Enter the item name:
Nike Romaleos
Enter the item description:
Volt color, Weightlifting shoes
Enter the item price:
189
Enter the item quantity:
2

(8) Implement remove item menu option. (4 pts) 

Ex:

REMOVE ITEM FROM CART
Enter name of item to remove:
Chocolate Chips

(9) Implement Change item quantity menu option. Hint: Make new ItemToPurchase object before using ModifyItem() method. (5 pts) 

Ex:

CHANGE ITEM QUANTITY
Enter the item name:
Nike Romaleos
Enter the new quantity:
3

#============================================================================================================

# Type code here
class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity
        self.item_total = price * quantity
        
    def print_item_description(self):
        print("%s: %s" % (self.item_name, self.item_description))
        
    #def __str__(self):
    #    return('%s %d @ $%0.0f = $%d' % (self.item_name, self.item_quantity, self.item_price, self.item_total))

class ShoppingCart:
    def __init__(self, name="none", date="January 1, 2016"):
        self.customer_name = name
        self.current_date = date
        self.cart_item = []
    # ==============================================
    def add_item(self, itemtopurchase):
        
        self.cart_item.append(itemtopurchase)
        
    # ==============================================
    
    def remove_item(self, item_to_remove):
        result = 0
        i = 0
        target = 0
        while i < len(self.cart_item):
            if item_to_remove == self.cart_item[i].item_name:
                result += 1
                target = i
            i += 1
            
        if result > 0:
            del self.cart_item[target]
            #self.cart_item.remove(item_to_remove)
        else:
            print("Item not found in cart. Nothing removed.")
            # remove item from cart_item list. has a string(item's name) parameter. Does not return anything.
            # if item name cannot be found, output this message: Item not found in cart. Nothing removed.
    
    def modify_item(self, itemtochange, itemnewquantity):
        result = 0
        i = 0
        target = 0
        while i < len(self.cart_item):
            if itemtochange == self.cart_item[i].item_name:
                result += 1
                target = i
            i += 1
            
        if result > 0:
            self.cart_item[target].item_name = itemtochange
            self.cart_item[target].item_quantity = itemnewquantity
        else:
            print("Item not found in cart. Nothing modified.")
        # Modifies an item's description, price and/or quantity.
        # if item can be found (by name) in cart, check if parameter has default values for description, price and quantity.
        # if not, modify item in cart
        # If item cannot be found(by name) in cart, output this message:
        # Item not found in cart. Nothing modified.
    
    def get_num_items_in_cart(self):
        i = 0
        for s in self.cart_item:
            i += s.item_quantity
        return i
    
    def get_cost_of_cart(self):
        i = 0
        for s in self.cart_item:
            i += s.item_price * s.item_quantity
        # Determines and returns the total cost of items in cart. Has no parameters.
        return i

    def print_total():
        # outputs total of objects in cart
        # If cart is empty, output this message: SHOPPING CART IS EMPTY
        pass

    def print_descriptions(self):
        print("%s's Shopping Cart - %s" % (self.customer_name, self.current_date))
        print()
        print("Item Descriptions")
        i = 0
        while i < len(self.cart_item):
            print("%s: %s" % (self.cart_item[i].item_name, self.cart_item[i].item_description))
            i += 1

def print_menu():
    print()
    print('MENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print()
    #myselection = ""
    myselection = input("Choose an option:\n")
    while (myselection != "q"):
        if myselection == "o":
            selection_o(customer_list[0])
            print_menu2()
        elif myselection == "a":
            selection_a(customer_list[0])
            print_menu2()
        elif myselection == "r":
            selection_r(customer_list[0])
            print_menu2()
        elif myselection == "c":
            selection_c(customer_list[0])
            print_menu2()
        elif myselection == "i":
            selection_i(customer_list[0])
            print_menu2()
        myselection = input("Choose an option:\n")

def selection_o(customer):
    print("OUTPUT SHOPPING CART")
    print("%s's Shopping Cart - %s" % (customer.customer_name, customer.current_date))
    print("Number of Items:", customer.get_num_items_in_cart())
    print()
    if customer.get_num_items_in_cart() == 0:
        print("SHOPPING CART IS EMPTY")
    else:
        i = 0
        for i in range(len(customer.cart_item)):
            print("%s %d @ $%d = $%d" % (customer.cart_item[i].item_name, customer.cart_item[i].item_quantity, customer.cart_item[i].item_price, customer.cart_item[i].item_price * customer.cart_item[i].item_quantity))
        #Nike Romaleos 2 @ $189 = $378
    print()
    if customer.get_num_items_in_cart() == 0:
        print("Total: $0")
    else:
        print("Total: $%d" % (customer.get_cost_of_cart()))


def selection_a(customer):
    print("ADD ITEM TO CART")
    itemtopurchase = ItemToPurchase()
    itemtopurchase.item_name = input("Enter the item name:\n")
    itemtopurchase.item_description = input("Enter the item description:\n")
    itemtopurchase.item_price = int(input("Enter the item price:\n"))
    itemtopurchase.item_quantity = int(input("Enter the item quantity:\n"))
    customer.add_item(itemtopurchase)

def selection_r(customer):
    print("REMOVE ITEM FROM CART")
    itemtoremove = input("Enter name of item to remove:\n")
    customer.remove_item(itemtoremove)

def selection_c(customer):
    print("CHANGE ITEM QUANTITY")
    itemtochange = input("Enter the item name:\n")
    itemnewquantity = int(input("Enter the new quantity:\n"))
    customer.modify_item(itemtochange, itemnewquantity)

def selection_i(customer):
    print("OUTPUT ITEMS' DESCRIPTIONS")
    customer.print_descriptions()


def print_menu2():
    print()
    print('MENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print()


if __name__ == "__main__":
    # Type main section of code here
    customer_list = []
    customer_name = input("Enter customer's name:\n")
    customer_date = input("Enter today's date:\n")
    customer_list.append(ShoppingCart(customer_name, customer_date))
    
    print()
    print("Customer name: %s" % customer_list[0].customer_name)
    print("Today's date: %s" % customer_list[0].current_date)
    
    print_menu()



#============================================================================================================
