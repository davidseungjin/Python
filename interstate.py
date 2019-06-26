highway_number = int(input('Input number of interstate highway to know more'))

''' Type your code here. '''
auxiliary = highway_number % 100

if (highway_number < 100) and (highway_number > 0):
    if highway_number % 2 == 0:
        print('The %d is primary, going east/west.' % highway_number)
    else:
        print('The %d is primary, going north/south.' % highway_number)
elif (highway_number >= 100) and (highway_number < 1000):
    if highway_number % 2 ==0:
        print('The %d is auxiliary, serving the %d, going east/west.' % (highway_number, auxiliary))
    else:
        print('The %d is auxiliary, serving the %d, going north/south.' % (highway_number, auxiliary))
else:
    print('%d is not a valid interstate highway number.' % highway_number)
