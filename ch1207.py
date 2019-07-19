import csv

with open('csvtest.csv', 'r') as csvfile:
	grades_reader = csv.reader(csvfile, delimiter=',')

	row_num = 1
	for row in grades_reader:
		print('Row #%d:' % row_num, row)
		row_num += 1


