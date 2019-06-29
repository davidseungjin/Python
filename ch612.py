
''' Your solution goes here '''
def swap(a):
    lastindex=0
    for i in a:
        lastindex += 1
        #print('lastindex is', lastindex)
    temp = a[0]
    a[0] = a[lastindex-1]
    a[lastindex-1] = temp
    
values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)
