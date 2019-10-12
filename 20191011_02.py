import operator
import sys
import re


def tokenize(f):
	line = f.readline()
	result = []
	while line:
		line = line.lower()
		line = re.sub(r'[-]', ' ', line)
		line = re.sub(r'\b[^A-Za-z0-9 ]\b','',line)
		result = result + re.split(r'\s+', line, flags = re.I)
		line = f.readline()
	return result 

def mapping(token):
	map_pending = {}
	if token is not None:
		for key in token:
			if key in map_pending:
				map_pending[key] += 1
			else:
				map_pending[key] = 1
		sorted_map_list = sorted(map_pending.items(), key=operator.itemgetter(1), reverse = True)
		sorted_map_dic = dict(sorted_map_list)
		return sorted_map_dic
	else:
		return None

def myintersect_dic(mydic1, mydic2):
	myintersect_dic = {}
	count_myintersect_dic = 0
	for i in mydic1.keys():
		if i in mydic2.keys():
			myintersect_dic[i] = min(mydic1[i], mydic2[i])
			count_myintersect_dic += 1
	return count_myintersect_dic
		
def showme(myintersect_dic):
	result = 0
	for i in myintersect_dic.keys():
#		print('%15s :		%4d' % (i, myintersect_dic[i]))
		result += myintersect_dic[i]
	print('total is %4d' % result)

def showmecount(a):
	print(a)

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('You need to provide two argument files')
	else:
		f1 = open(sys.argv[1], 'r')
		f2 = open(sys.argv[2], 'r')

		mydic1 = mapping(tokenize(f1))
		mydic2 = mapping(tokenize(f2))
		
		print(mydic1)
		print(mydic2)	
	
		myintersect_dic = myintersect_dic(mydic1, mydic2)
		print(myintersect_dic)

		showmecount(myintersect_dic)
	
		f1.close()
		f2.close()

