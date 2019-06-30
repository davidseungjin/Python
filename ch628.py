"""
6.28 LAB: Output values in a list below a user defined amount - functions
Write a program that first gets a list of integers from input. The input begins with an integer indicating the number of integers that follow. Then, get the last value from the input, and output all integers less than or equal to that value.

Ex: If the input is:

5
50
60
140
200
75
100
the output is:

50
60
75
The 5 indicates that there are five integers in the list, namely 50, 60, 140, 200, and 75. The 100 indicates that the program should output all integers less than or equal to 100, so the program outputs 50, 60, and 75.

Such functionality is common on sites like Amazon, where a user can filter results.

Your code must define and call the following two functions:
def get_user_values()
def output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold)

Utilizing functions will help to make your main very clean and intuitive.

Note: This is a lab from a previous chapter that now requires the use of functions.
"""



''' Define your function here '''
def get_user_values():
    num_items = int(input())
    mylist = []
    for i in range(num_items):
        mylist.append(int(input()))
    #print('mylist is', mylist) <- working
    upper_threshold = int(input())
    return mylist, upper_threshold

def output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    for i in user_values:
        if i < upper_threshold:
            print(i)
# ==========================================================================
CAUTION: The reason I took a long time to fix it was because of FOR-LOOP.
I have tried to use user_values[i] instead of i to see value comparison
with upper_threshold.
But, it's i. i is not an index. KEEP IN MIND THIS!!!
# ==========================================================================

if __name__ == '__main__':
    user_values, upper_threshold = get_user_values()
#    print(user_values, upper_threshold) // working.
    output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold)
