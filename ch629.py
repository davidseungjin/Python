"""
6.29 LAB: Warm up: Text analyzer & modifier
(1) Prompt the user to enter a string of their choosing. Output the string. (1 pt) 

Ex:

Enter a sentence or phrase:
The only thing we have to fear is fear itself.

You entered: The only thing we have to fear is fear itself.
(2) Complete the get_num_of_characters() function, which returns the number of characters in the user's string. We encourage you to use a for loop in this function. (2 pts)

(3) Extend the program by calling the get_num_of_characters() function and then output the returned result. (1 pt)

(4) Extend the program further by implementing the output_without_whitespace() function. output_without_whitespace() outputs the string's characters except for whitespace (spaces, tabs). Note: A tab is '\t'. Call the output_without_whitespace() function in main(). (2 pts) 

Ex:

Enter a sentence or phrase: 
The only thing we have to fear is fear itself.

You entered: The only thing we have to fear is fear itself.

Number of characters: 46
String with no whitespace: Theonlythingwehavetofearisfearitself.

"""

def get_num_of_characters(input_str):
    num = 0
    for i in input_str:
        num += 1
    return num
    
def get_num_of_characters_wo_space(input_str):
    return input_str.replace(" ", "")

if __name__ == '__main__':
    # Type your code here
    input_str = input('Enter a sentence or phrase:\n')
    print('\nYou entered: %s' % input_str)
    print()
    print('Number of characters:', get_num_of_characters(input_str))
    print('String with no whitespace: %s' % get_num_of_characters_wo_space(input_str))
