fw = open('20191007.txt', 'w')
fw.write('David Lee is trying to test and practice how to write text into a file after creating file\n')
fw.write('\nThis is the second line. \n')
fw.write('\n This is the third line\n')
fw.close()

print('Following texts comes from text file\n')
fr = open('20191007.txt', 'r')
sentences = fr.read()
print(sentences)

fr.close()


