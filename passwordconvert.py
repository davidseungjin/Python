word = input()
password = ''


while i in word:
    if i == "i":
        i = "!"
    elif i == "a":
        i = "@"
    elif i == "m":
        i = "M"
    elif i == "B":
        i = "8"
    elif i == "o":
        i = "."
    password += i
print(password)

