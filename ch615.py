student_scores = [75, 84, 66, 99, 51, 65]

def get_grade_stats(scores):
	mean = sum(scores)/len(scores)

	tmp =0
	for score in scores:
		tmp += (score - mean)**2
	std_dev = (tmp/len(scores))**0.5

	# Package and return average, std dev in a tuple
	return mean, std_dev	# <== this is a tuple container
	# equivalent statement is return (mean, std_dev)
	# the return output can be a list container, expression is return [mean, std_dev]
	# return a, b, [c, d] is possible. If then, it means (a, b, [c, d]) tuple.


#Unpack tuple
average, standard_deviation = get_grade_stats(student_scores)

print('Average score:', '%0.2f' % average)
print('Standard deviation:', '%0.2f' % standard_deviation)
