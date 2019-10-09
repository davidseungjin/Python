
L = ["Python", "David", "123", 345345]

file = open('20191008_02_test.txt', 'w')

file.write("START\n")

for i in range(3):
	file.write('%s\n' % L[i])

file.write("END")

file.close()

