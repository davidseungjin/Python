"""
This is chaptor 6.7 example. The original example was imcomplete between line 14 and line 42.
"""

size = 5

def get_numbers(num):
    numbers = []
    user_input = input('Enter %s integers:\n' % num)

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    # Print numbers
    print('Numbers:', end=' ')
    for i in range(len(numbers)):
        print(numbers[i], end = ' ')
    print()
    
def print_odd_numbers(numbers):
    # Print all odd numbers
    print('Odd numbers:', end=' ')
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            print(numbers[i], end=' ')
    print()

def print_negative_numbers(numbers):
    # Print all negative numbers
    print('Negative numbers:', end=' ')
    for i in range(len(numbers)):
        if numbers[i] < 0:
            print(numbers[i], end=' ')
    print()

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)
