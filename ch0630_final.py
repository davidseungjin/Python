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




# Type all other functions here

def print_menu(usr_str):
    menu_op = ' '
    #Complete print_menu() function
    while(menu_op != 'q'):
        #print()
        print('\nMENU')
        print('c - Number of non-whitespace characters')
        print('w - Number of words')
        print('f - Fix capitalization')
        print('r - Replace punctuation')
        print('s - Shorten spaces')
        print('q - Quit')
        #print()
        menu_op = input('\nChoose an option:')
        print()
        if (menu_op == 'c'):
            get_num_of_non_WS_characters(user_input)
        if (menu_op == 'w'):
            get_num_of_words(user_input)
        if (menu_op == 'f'):
            fix_capitalization(user_input)
        if (menu_op == 'r'):    
            replace_punctuation(user_input)
        if (menu_op == 's'):    
            shorten_space(user_input)
    return menu_op, usr_str

def question1(user_input):
    print()
    print('You entered:', user_input)
    
def get_num_of_non_WS_characters(user_input):
    #mylist = list(map(str, user_input.split()))
    print('Number of non-whitespace characters:', len(user_input.replace(" ", "")))
    return len("".join(user_input.split()))

def get_num_of_words(user_input):
    print('Number of words:', len(list(map(str, user_input.split()))))
    return len(list(map(str, user_input.split())))

def fix_capitalization(user_input):
    i = 0
    num_edited = 0
    str_edited = ""
    thestring = {}
    need_capitalize = True
    for i in range(len(user_input)):
        if ((user_input[i] != " ") and (user_input[i].islower()) and (need_capitalize)):
            str_edited += user_input[i].upper()
            thestring[user_input[i]] = user_input[i].upper()
            num_edited += 1
            need_capitalize = False
        elif((not need_capitalize) and (user_input[i] == '.')):
            str_edited += user_input[i]
            need_capitalize = True
        else:
            str_edited += user_input[i]
        #i += 1
    print('Number of letters capitalized:', num_edited)
    print('Edited text:', str_edited)
    return str_edited, num_edited

def replace_punctuation(user_input, **kwargs):
    i = 0
    str_edited = ""
    exclamation_count = 0
    semicolon_count = 0
    while i < len(user_input):
        if (user_input[i] == "!"):
            str_edited += "."
            exclamation_count += 1
        elif(user_input[i] == ";"):
            str_edited += ","
            semicolon_count += 1
        else:
            str_edited += user_input[i]
        i += 1
    print('Punctuation replaced')
    print('exclamation_count:', exclamation_count)
    print('semicolon_count:', semicolon_count)
    print('Edited text:', str_edited)
    return str_edited

def shorten_space(user_input):
    str_edited = " ".join(user_input.split())
    print('Edited text:', str_edited)
    return str_edited

if __name__ == '__main__':
    # Complete main section of code
    user_input = input('Enter a sample text:\n')
    question1(user_input)
    
    #print_menu(user_input)
    #If this statement and below statement are executed together, error occurs in zyBook module.
    menu_op, user_input = print_menu(user_input)
    
