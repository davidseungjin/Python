import os
p = os.path.join('.', 'test.txt')
if os.path.isfile(p):
    print('Found a file...')
else:
    print('Not a file...')

print()
print('Size of file: ', os.path.getsize(p), 'bytes')


year = input('Enter year: ')
path = os.path.join('logs', year)
print()
for dirname, subdirs, files in os.walk(path):
    print(dirname, 'contains subdirectories:', subdirs, end=' ')
    print('and the files:', files)


