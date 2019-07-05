class Time:
    def __init__(self):
        self.hours = 0
        self.minutes = 0

    def print_time(self):
        print('Hours:', self.hours, end=' ')
        print('Minutes:', self.minutes)


time1 = Time()
time1.hours = 7
time1.minutes = 15
time1.print_time()



class Employee:
    def __init__(self):
        self.wage = 0
        self.hours_worked = 0

#   def ... Add new method here ...
#        ...
    def calculate_pay(self):
        return self.wage*self.hours_worked 

alice = Employee()
alice.wage = 9.25
alice.hours_worked = 35
print('Alice:\n Net pay: %f' % alice.calculate_pay())

bob = Employee()
bob.wage = 11.50
bob.hours_worked = 20
print('Bob:\n Net pay: %f' % bob.calculate_pay())

