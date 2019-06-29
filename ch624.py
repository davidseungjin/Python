''' Define your function here. '''
def integer_to_reverse_binary(integer_value):
    x = ''
    while integer_value == 1 or integer_value == 0:
        remainder = integer_value % 2
        integer_value = (integer_value - remainder) // 2
        x += remainder
    print(x)
    return x

def reverse_string(input_string):
    reversed_string = ''
    for i in input_string:
        reversed_string += i
    return reversed_string

if __name__ == '__main__':
    ''' Type your code here. Your code must call the function. '''
    integer_value = int(input())
    reversed_binary = integer_to_reverse_binary(integer_value)
    result = reverse_string(reversed_binary)
    print(result)

