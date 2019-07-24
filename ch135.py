class DrivingMixin(object):
	def drive(self, distance):
	def change_tire(self):
	def check_oil(self):

class FlyingMixin(object):
	def fly(self, distance, altitude):
	def roll(self):
	def eject(self):

class TransportMode(object):
	def __init__(self, name, speed):
		self.name = name
		self.speed = speed

	def display(self):
		print('%s can go %d mpg' % (self.name, self.speed))

class SemiTruck(TransportMode, DrivingMixin):
	def __init__(self, name, speed, cargo):
		TransportMode.__init__(self, name, speed)
		self.cargo = cargo

	def go(self, distance):
		self.drive(distance)

class FlyingCar(TransportMode, FlyingMixin, DrivingMixin)
	def __init__(self, name, speed, max_altitude):
		TransportMode.__init__(self, name, speed)
		self.max_altitude = max_altitude

	def go(self, distance):
		self.fly(distance / 2, self.max_altitude)
		self.drive(distance / 2)

s = SemiTruck('MacTruck', 85, 'Frozen beans')
f = FlyingCar('Jetson35K', 325, 15000)

s.go()
f.go()

