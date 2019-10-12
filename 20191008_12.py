import re

line = "Cats are smarter than dogs"

searchobj = re.search(r'(.*) are (.*) (.*) .*', line, re.M|re.I)

if searchobj:
	print("searchobj.group(): ", searchobj.group())
	print("searchobj.group(1): ", searchobj.group(1))
	print("searchobj.group(2): ", searchobj.group(2))
	print("searchobj.group(3): ", searchobj.group(3))
else:
	print("Nothing")
