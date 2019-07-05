class Time:
	def __init__(self):
		self.hours = 0
		self.minutes = 0

my_time = Time()
my_time.hours = 7
my_time.minutes = 15

mytime = Time()
mytime.hours = 2
mytime.minutes = 19

mycopy = mytime

print('%d hours' % my_time.hours, end=' ')
print('and %d minutes' % my_time.minutes)

print('%d hours' % mytime.hours, end=' ')
print('and %d minutes' % mytime.minutes)

print('mytime is', mytime)
print('mytime is', id(mytime))
print('mytime hours is', id(mytime.hours))
print('mytime minutes is', id(mytime.minutes))

print('mycopy is', mycopy)
print('mycopy is', id(mycopy))
print('mycopy hours is', id(mycopy.hours))
print('mycopy minutes is', id(mycopy.minutes))

