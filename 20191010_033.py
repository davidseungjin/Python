import operator
import sys
import re


def tokenize():
	line = f.readline()
	result = []
	while line:
		line = line.lower()
		line = line.replace(".", "")
		line = line.replace("\n", "")
		line = line.replace(",", "")
		result += line.split()
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

def showme(mapped_tokens):
	for i in mapped_tokens.keys():
		print('%15s :		%4d' % (i, mapped_tokens[i]))


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('You need to provide one argument file')
	else:
		f = open(sys.argv[1], 'r')
	
		'Prolems A-1'
		tokenizedlist = tokenize()
		print(tokenizedlist)
	
		'Problem A-2'
		mapped_token = mapping(tokenizedlist)
		print(mapped_token)
	
		'Problem A-3'
		showme(mapped_token)
	
		f.close()

