class Item:
	def __init__(self):
		self.name = ''
		self.quantity = 0

	def set_name(self, nm):
		self.name = nm

	def set_quantity(self, qty):
		self.quantity = qty

	def display(self):
		print(self.name, self.quantity)

class Produce(Item):
	def __init__(self):
		Item.__init__(self)
		self.expiration = ''

	def set_expiration(self, exp):
		self.expiration = exp

	def get_expiration(self):
		return self.expiration

item1 = Item()
item1.set_name('Smith Cereal')
item1.set_quantity(9)
item1.display()

item2 = Produce()
item2.set_name('Apples')
item2.set_quantity(40)
item2.set_expiration('May 5, 2012')
item2.display()
print('  (Expires:(%s))' % item2.get_expiration())
print('\nthe other way\n')
print('  (Expires:(%s))' % item2.expiration)

item3 = Produce()
item3.set_name('Banana')
item3.set_quantity(25)
item3.set_expiration('July 25, 2012')
item3.display()
print('  (Expires:(%s))' % item3.get_expiration())
print('\nthe other way\n')
print('  (Expires:(%s))' % item3.expiration)
