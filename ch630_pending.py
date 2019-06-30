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
