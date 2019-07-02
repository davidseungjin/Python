7.10 LAB: Palindrome
A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

Ex: If the input is:

bob
the output is:

bob is a palindrome
Ex: If the input is:

bobby
the output is:

bobby is not a palindrome
Hint: Start by removing spaces. Then check if a string is equivalent to it's reverse.


''' Type your code here. '''
input_string = input()
striped_txt = input_string.replace(" ", "")
palindrome_count = 0
i = 0
while i < len(striped_txt):
    if striped_txt[i] == striped_txt[-1*i-1]:
        palindrome_count += 1
    i += 1

if palindrome_count == len(striped_txt):
    print('%s is a palindrome' % input_string)
else:
    print('%s is not a palindrome' % input_string)
