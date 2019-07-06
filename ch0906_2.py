class Employee:
	def __init__(self, name, wage = 8.25, hours = 20):
		'''
		Default employee is part time (20 hours per week)
		and earns minimum wage
		'''

		self.name = name
		self.wage = wage
		self.hours = hours

todd = Employee('Todd')
jason = Employee('Jason')
tricia = Employee('Tricia', wage=12.50, hours=40)

employees = [todd, jason, tricia]

for e in employees:
	print('%s earns %0.2f per week' % (e.name, e.wage*e.hours))

