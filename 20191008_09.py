

set1 = 'We reviewed the trip and credited the cancellation fee. The driver has been notified.'.split()
set2 = 'If a trip is cancelled more than 5 minutes after the driver-partner has confirmed the request, a cancellation fee will apply'.split()


print("set 1 intersection set2 :", set(set1).intersection(set2))


print("count is ", len(set(set1).intersection(set2)))


res = 0
for i in set1:
	if i in set2:
		res += 1

print(res)

