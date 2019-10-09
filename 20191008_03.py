L = []

file = open('20191008_02_test.txt', 'r')

while(1):
	line = file.readline()

	try:
		escape = line.index('\n')
	except:
		escape = len(line)

	if line:
		L.append(line[0:escape])
	else:
		break

file.close()

print(L)

