class Time:
	def __init__(self, hours, minutes):
		self.hours = hours
		self.minutes = minutes

	def __str__(self):
		return '%d:%d' % (self.hours, self.minutes)

	def __lt__(self, other):
		if self.hours < other.hours:
			return True
		elif self.hours == other.hours:
			if self.minutes < other.minutes:
				return True
		return False

""" 
Rich comparision methods are

__lt__(self, other) is less than, 
__le__(self, other) is less than or equal to
__gt__(self, other) is greater than
__ge__(self, other) is greater than or equal to
__eq__(self, other) is equal to
__ne__(self, other) is not equal to

"""


num_times = 3
times = []

#Obtain times from user input

for i in range(num_times):
	user_input = input('Enter time (Hrs:Mins): ')
	tokens = user_input.split(':')
	times.append(Time(int(tokens[0]), int(tokens[1])))

min_time = times[0]
for t in times:
	if t < min_time:
		min_time = t

print('\nEarliest time is', min_time)
print('times list is ', times)
print('times[0] in the list is', times[0])
print('times[0].minutes in the list is', times[0].minutes)
