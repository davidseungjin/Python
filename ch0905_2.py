class Seat:
	def __init__(self):
		self.first_name = ''
		self.last_name = ''
		self.paid = 0.0

	def reserve(self, firstname, lastname, paid_or_not):
		self.first_name = firstname
		self.last_name = lastname
		self.paid = paid_or_not

	def make_empty(self):
		self.first_name = ''
		self.last_name = ''
		self.paid = 0.0

	def is_empty(self):
		return self.first_name == ''

	def print_seat(self):
		print('%s %s, Paid: %.2f' % (self.first_name, self.last_name, self.paid))

def make_seat_empty(seats):
	for s in seats:
		s.make_empty()

def print_seats(seats):
	for s in range(len(seats)):
		print('%d:' % s, end=' ')
		seats[s].print_seat()

num_seats = 5

available_seats = []
for i in range(num_seats):
	available_seats.append(Seat())

command = input('Enter command (p/r/e/q): ')
while command != 'q':
	if command == 'p':		# Print seats
		print_seats(available_seats)
	elif command == 'r':	# Reserve a seat
		seat_num = int(input('Enter seat num:\n'))
		if not available_seats[seat_num].is_empty():
			print('Seat not empty')
		else:
			fname = input('Enter first name:\n')
			lname = input('Enter last name:\n')
			paid = float(input('Enter amount paid:\n'))
			available_seats[seat_num].reserve(fname, lname, paid)
	elif command == 'e':
		seat_num = int(input('Enter seat num:\n'))
		available_seats[seat_num].make_empty()
	else:
		print('Invalid command.')

	command = input('Enter command (p/r/e/q):\n')


