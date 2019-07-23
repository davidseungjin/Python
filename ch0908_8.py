#Special method name, __str__

class Veggie:
	def __init__(self, name, price, qty):
		self.name = name
		self.price = price
		self.qty = qty

	def __str__(self):
		return('%s unit price is $%.2f. and quantity is %d, so total price of %s is $%.2f' % (self.name, self.price, self.qty, self.name, self.price*self.qty))

spinach = Veggie('Spinach', 2.5, 3)
print(spinach)

