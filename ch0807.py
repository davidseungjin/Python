user_input = input('Enter numbers: ')

tokens = user_input.split()

# Convert strings to integers
nums = []
for token in tokens:
	nums.append(int(token))

#print each position and number
print()
for pos, val in enumerate(nums):
	print('%d: %d' % (pos, val))

#change negative values to 0
for pos in range(len(nums)):
	if nums[pos] <0:
		nums[pos] = 0

#print new numbers
print('New numbers: ')
for num in nums:
	print(num, end=' ')

