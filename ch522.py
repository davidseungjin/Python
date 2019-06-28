''' Type your code here. '''
num_item = int(input('Input the number of item in a list'))
list_item = []
for i in range(num_item):
    item = int(input())
    list_item.append(item)
threshold_item = int(input('input the threshold value'))
for i in range(num_item):
    if list_item[i] < threshold_item:
        print(list_item[i])
