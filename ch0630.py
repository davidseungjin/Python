
def fix_capitalization(usr_str):
    mylist = usr_str.split('.')
    for i in range(len(mylist)):
        mylist[i] = mylist[i].lstrip()
        mylist[i] = mylist[i].capitalize()
    myresult = mylist[0] + '. ' + mylist[1] + '. ' + mylist[2] + '.'
    return myresult


if __name__ == '__main__':
    # Complete main section of code
    input_txt = input('Enter a sample text:')
    print()
    print('\nYou entered: %s' % input_txt)
    print()
    print('Capitalizaed is', fix_capitalization(input_txt))
