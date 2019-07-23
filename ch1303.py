class Item:
	def __init__(self):
		self.name = ''
		self.quantity = 0
	
	def set_name(self, n):
		self.name = n
	
	def set_quantity(self, q):
		self.quantity = q
	
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

	def display(self):
		print(self.name, self.quantity, end=' ')
		print('   (Expires: %s)' % self.expiration)

item1 = Item()
item1.set_name('Smith Cereal')
item1.set_quantity(9)
item1.display()					# This will call Item class' display method.

print('Now below is Produce class')
p1 = Produce()
p1.set_name('Apple')
p1.set_quantity(40)
p1.set_expiration('May 5, 2012')
p1.display()						# This will call Produce's display method

