class Employee:
	def __init__(self, name, wage=8.25, hours=20):
		self.name = name
		self.wage = wage
		self.hours = hours

#david = Employee()
abraham = Employee('abraham')
caleb = Employee('caleb')
peter = Employee('peter', wage = 25.00, hours = 40)

# no impact to use duplicated entry because it is set
# why printing order is peter abraham and peter
employees = {peter, caleb, abraham, caleb, peter}

print('peter address is', id(peter))
print('caleb address is', id(caleb))
print('abraham address is', id(abraham))



for e in employees:
	print('%s earns %.2f per hour and works %d per week' % (e.name, e.wage, e.hours))

