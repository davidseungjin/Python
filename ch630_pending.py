"""
6.30 LAB*: Program: Authoring assistant
(1) Prompt the user to enter a string of their choosing. Store the text in a string. Output the string. (1 pt) 

Ex:

Enter a sample text:
we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!

You entered: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!

(2) Implement a print_menu() function, which has a string as a parameter, outputs a menu of user options for analyzing/editing the string, and returns the user's entered menu option and the sample text string (which can be edited inside the print_menu() function). Each option is represented by a single character.

If an invalid character is entered, continue to prompt for a valid choice. Hint: Implement the Quit menu option before implementing other options. Call print_menu() in the main section of your code. Continue to call print_menu() until the user enters q to Quit. (3 pts) 

Ex:

MENU
c - Number of non-whitespace characters
w - Number of words
f - Fix capitalization
r - Replace punctuation
s - Shorten spaces
q - Quit

Choose an option:

(3) Implement the get_num_of_non_WS_characters() function. get_num_of_non_WS_characters() has a string parameter and returns the number of characters in the string, excluding all whitespace. Call get_num_of_non_WS_characters() in the print_menu() function. (4 pts) 

Ex:

Number of non-whitespace characters: 181

(4) Implement the get_num_of_words() function. get_num_of_words() has a string parameter and returns the number of words in the string. Hint: Words end when a space is reached except for the last word in a sentence. Call get_num_of_words() in the print_menu() function. (3 pts) 

Ex:

Number of words: 35

(5) Implement the fix_capilization() function. fix_capilization() has a string parameter and returns an updated string, where lowercase letters at the beginning of sentences are replaced with uppercase letters. fix_capilization() also returns the number of letters that have been capitalized. Call fix_capilization() in the print_menu() function, and then output the number of letters capitalized and the edited string. Hint 1: Look up and use Python functions .islower() and .upper() to complete this task. Hint 2: Create an empty string and use string concatenation to make edits to the string. (3 pts) 

Ex:

Number of letters capitalized: 3
Edited text: We'll continue our quest in space.  There will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  Nothing ends here;  our hopes and our journeys continue!

(6) Implement the replace_punctuation() function. replace_punctuation() has a string parameter and two keyword argument parameters exclamation_count and semicolon_count. replace_punctuation() updates the string by replacing each exclamation point (!) character with a period (.) and each semicolon (;) character with a comma (,). replace_punctuation() also counts the number of times each character is replaced and outputs those counts. Lastly, replace_punctuation() returns the updated string. Call replace_exclamation() in the print_menu() function, and then output the edited string. (3 pts) 

Ex:

Punctuation replaced
exclamation\_count: 1
semicolon\_count: 2
Edited text: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes,  more volunteers, more civilians,  more teachers in space.  nothing ends here,  our hopes and our journeys continue.

(7) Implement the shorten_space() function. shorten_space() has a string parameter and updates the string by replacing all sequences of 2 or more spaces with a single space. shorten_space() returns the string. Call shorten_space() in the print_menu() function, and then output the edited string. Hint: Look up and use Python function .isspace(). (3 pt) 

Ex:

Edited text: we'll continue our quest in space. there will be more shuttle flights and more shuttle crews and, yes, more volunteers, more civilians, more teachers in space. nothing ends here; our hopes and our journeys continue!
"""



# Type all other functions here

def print_menu(user_str):
    menu_op = ' '
    while menu_op != 'q':
        print('MENU')
        print('c - Number of non-whitespace characters')
        print('w - Number of words')
        print('f - Fix capitalization')
        print('r - Replace punctuation')
        print('s - Shorten spaces')
        print('q - Quit')
        print()
        menu_op = input('Choose an option:')
        if menu_op == 'c':
            print('Number of non-whitespace characters: %d' % get_num_of_non_WS_characters(user_str))
        if menu_op == 'w':
            print('Number of words: %d' % get_num_of_words(user_str))
        if menu_op == 'f':
            print('Number of letters capitalized:', fix_capitalization(user_str))
          #  print("Edited text: We'll continue our quest in space. There will be more shuttle flights and more shuttle crews and, yes; more volunteers, more civilians, more teachers in space. Nothing ends here; our hopes and our journeys continue!")
        print()
    return menu_op, user_str
def get_num_of_non_WS_characters(user_str):
    num_char = 0
    for i in user_str:
        if i != " ":
            num_char += 1
    return num_char
def get_num_of_words(user_str):
    words_list = user_str.split()
    num_word = 0
    for i in words_list:
        num_word += 1
    return num_word
def fix_capitalization(user_str):
    sentence_splitted = user_str.split('. ')
    capitalized_list = []
    num_sentence = 0
    for i in sentence_splitted:
        capitalized_list.append(i.capitalize())
        num_sentence += 1
        
    print('sentence_splitted is ', sentence_splitted)
    print('capitalized_list is ', capitalized_list)
    new_text = '. '.join(capitalized_list)
    print(new_text)
    return num_sentence

if __name__ == '__main__':
    # Complete main section of code
    input_txt = input('Enter a sample text:')
    print()
    print('\nYou entered: %s' % input_txt)
    print()
    print_menu(input_txt)
