f = open('testwriting.txt', 'w', buffering = 1000) #open file
f.write('Example string: aaaaa aaaaa aaaaa') #write string
f.write('This is the second file.')

f.close() # close the file
