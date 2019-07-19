import csv

row1 = ['100', '50', '29']
row2 = ['50', '60', '55']

with open('csvtestwrite.csv', 'w') as csvfile:
	grades_writer = csv.writer(csvfile)

	grades_writer.writerow(row1)
	grades_writer.writerow(row2)

	grades_writer.writerows([row1, row2])

