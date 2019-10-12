###############################################################################
# I don't copy code any code from the internet. 
# But I studied from resources on the web.
# I listed just because I am afraid of any penalty not mentioning any words
# regarding plagiarism(in HW1 instruction). 
# Please remind it is mandatory to mention an origin
# when there is no origin like my case.
# 
# Mostly I studied to complete my code from following web site.
#	For file argument			Lecture from EECS12 in Summer 2019
# For file reading			https://www.ics.uci.edu/~thornton/ics32a/
# For Regex study				Youtube search (Coding train etc)
# For Regex practice		https://regex101.com/
# For sort()						Lecture from EECS12 in Summer 2019
# For operator					Python STL document, stackoverflow, geeksforgeeks
###############################################################################


import operator
import sys
import re

#########################################################################
#	Tokenize() time complexity
# 
# Other than assigning (O(1)), two things are concerned
# The first one is while-loop which is O(n)
# The second one is regular expression.
# Since the pattern needed for this assignment is simple, so I don't 
# think it's complicated time complexity. I think it's O(n)
#########################################################################
def tokenize():
	line = f.readline()
	result = []
	while line:
		line = line.lower()
		line = re.sub(r'[-]', ' ', line)
		line = re.sub(r'[^A-Za-z0-9 ]','',line)
		result = result + re.split(r'\s+', line, flags = re.I)
		line = f.readline()
	return result 

#########################################################################
# Mapping() time complexity
# 
# Two things are concerned. The one is making dictionary with key relevant
# to its frequency. The other one is sorting in values.
#	Making dictionary is O(n).
# Making sort is O(nlogn) according to a python document.
#########################################################################
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

#########################################################################
# showme() time complexity
#
# This is O(n)
#########################################################################
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
		print('===== Problems A-1: Tokenize and make them a List =====\n')
		print(tokenizedlist)
	
		'Problem A-2'
		print('\n===== Problems A-2: Mapping to make a Dictionary =====\n')
		mapped_token = mapping(tokenizedlist)
		print(mapped_token)
	
		'Problem A-3'
		print('\n===== Problems A-3: Print Frequencies <Token, Count>  =====\n')
		showme(mapped_token)
	
		f.close()
