6.25 LAB: Swapping variables
Write a program whose input is two integers and whose output is the two integers swapped.

Ex: If the input is:

3
8
the output is:

8 3
Your program must define and call the following function. swap_values() returns the two values in swapped order.
def swap_values(user_val1, user_val2)


''' Define your function here. '''
def swap_values(user_val1, user_val2):
    temp = user_val1
    user_val1 = user_val2
    user_val2 = temp
    return user_val1, user_val2
    
if __name__ == '__main__': 
    ''' Type your code here. Your code must call the function. '''
    user_val1 = int(input())
    user_val2 = int(input())
    test1, test2 = swap_values(user_val1, user_val2)
    print(test1, test2)
