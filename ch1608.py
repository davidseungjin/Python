def partition(numbers, i, k):
	# Pick middle value as pivot

	midpoint = i + (k - i) // 2
	pivot = numbers[midpoint]  

	# Initialize variables
	done = False    
	l = i
	h = k
	while not done:
	# Increment l while numbers[l] < pivot
		while numbers[l] < pivot:
			l = l + 1
	# Decrement h while pivot < numbers[h]
		while pivot < numbers[h]:
			h = h - 1
			#If there are zero or one items remaining,
			#all numbers are partitioned. Return h """
			if l >= h:
				done = True
			else:
      #""" Swap numbers[l] and numbers[h],
      #update l and h """
				temp = numbers[l]
				numbers[l] = numbers[h]
				numbers[h] = temp
				l = l + 1
				h = h - 1
	return h
