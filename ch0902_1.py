class Score:
	student = 'student_YES'
	def __init__(self, ICS6B = 3, ICS6D = 3, ICS6N = 3, ICS46 = 3, ICS51 = 3):
		self.ICS6B = int(input('ICS6B?'))

	def print_obj(self):
		print("%s's ICS6B is %d" % (self, self.ICS6B))

	def print_obj2(self):
		return (self.ICS6B)


david = Score()
david.ICS6B = 5
print("David's ICS6B score is %d" % david.ICS6B)

print('trying print function by using method')
david.print_obj()

print('doing it with return')
print(david.print_obj2())

print("try to print class attribute, student_YES. See below")
print(david.student)

print("change class attribute to 'STUDENT_yes', and print it again")
Score.student = "STUDENT_yes"
print(david.student)
