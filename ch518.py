
i = ""

#KEEP IN MIND THAT != conditions should be with AND, not OR

while (i != "Quit") and (i != "quit") and (i !="q"):
	i = input()
	result = ''
	if (i != "Quit") and (i !="quit") and (i !="q"):
		for j in i:
			result = j + result
		print(result)

