wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of soolishness'

wordlist = wordstring.split()

wordfreq = []

for w in wordlist:
	wordfreq.append(wordlist.count(w))

print("String \n " + wordstring + "\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies \n" + str(wordfreq) + "\n")
print("Pairs\n" + str(zip(wordlist, wordfreq)))

print()
print()

d = {'world':1, 'hello':0}
print(f'value of one of the key hello')
print(d['hello'])
print(f'same thing for world')
print(d['world'])
print(f'd.keys() is {d.keys()}')
print(f'd.values() is {(d.values())}')




