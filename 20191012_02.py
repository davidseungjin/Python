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
# I already mentioned this in PartA code.
# 
# Other than assigning (O(1)), two things are concerned
# The first one is while-loop which is O(n)
# The second one is regular expression.
# Since the pattern needed for this assignment is simple, so I don't 
# think it's complicated time complexity. I think it's O(n)
#########################################################################
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

#########################################################################
# Mapping() time complexity
# I already mentioned this in PartA code.
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
# myintersect_dic() time complexity
#
# for-loop, it is O(n), but other than this, it is O(1)
#########################################################################
def myintersect_dic(mydic1, mydic2):
	myintersect_dic = {}
	count_myintersect_dic = 0
	for i in mydic1.keys():
		if i in mydic2.keys():
			myintersect_dic[i] = min(mydic1[i], mydic2[i])
			count_myintersect_dic += 1
	return count_myintersect_dic
		
#########################################################################
# showmecount() time complexity
#
# O(1)
#########################################################################
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
		
		myintersect_dic = myintersect_dic(mydic1, mydic2)
		print('Number of common words from ' + sys.argv[1] +', ' + sys.argv[2] + ' is: \n')
		showmecount(myintersect_dic)
	
		f1.close()
		f2.close()

