import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
try:
	for line in lines:
		item = line.split(" ")
		user_name = item[item.index("name")+1]
		user_age = item[item.index("age")+1]
		user_city = item[item.index("city")+1]
		print(f'user_name, user_age, user_city is {user_name}, {user_age}, {user_city}')
		print()
except ValueError:
	print('Value Error occurs')
except:
	print('This shows when default error happens')

f.close()


# source: https://sancs.tistory.com/21

