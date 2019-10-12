import re

text = "1998a The film Titanic was released in 1998"
text2 = "The film pulp Fiction was released in year 1994"
text3 = "The film, '@Pulp Fiction' was ? released in % $ year 1994 H0n3sty!."
text4 = "The                   film pulp Fiction         was released in year 1994"
text5 = "       The                   film pulp Fiction         was released in year 1994      "
text6 = "The film Pulp Fiction     s was b released in year 1994"
text7 = "The film,    Pulp Fiction was released in year 1994 regarding pulp and Pulp."
text8 = "I want to buy a mobile between 200 and 400 EUs"
text9 = "February 2011"


result2 = re.sub(r"[a-z]", "X", text2)
result3 = re.sub(r"[a-z]", "Y", text2, flags=re.I)
result4 = re.sub(r"\d", "", text2)
result4 = re.sub(r"[A-Z]", "-", text2)
result5 = re.sub(r"\W", "", text3)
result6 = re.sub(r"[,@\'?\.$%_  ]", "", text3, flags=re.I)
result7 = re.sub(r"\s+", " ", text4, flags=re.I)
result8 = re.sub(r"^\s+", "", text5)
result9 = re.sub(r"\s+$", "", text5)
result10 = re.sub(r"^\s+$", "", text5)
result11 = re.sub(r"\s+[a-zA-Z]\s+", " ", text6)
result12 = re.split(r"\s+", text7, flags = re.I)
result13 = re.split(r"\,", text7, flags = re.I)

result14 = re.search(r"\d+", text8)
result15 = re.findall(r"\d+", text8)
result16 = re.findall(r"Feb(ruary)? 2011", text9)

#result = re.search(r"[a-zA-Z]+", text)
result = re.search(r"1998$", text)


print('result is ', result)
print('result 2 is ', result2)
print('result 3 is ', result3)
print('result 4 is ', result4)
print('result 5 is ', result5)
print('result 6 is ', result6)
print('result 7 is ', result7)
print('result 8 is ', result8)
print('result 9 is ', result9)
print('result 10 is ', result10)
print('result 11 is ', result11)
print('result 12 is ', result12)
print('result 13 is ', result13)
print('result14.group(0) is ', result14.group(0))
print('result14 is ', result14)
print('result14.group() is ', result14.group())
print('result14.span() is ', result14.span())
print('result14.start() is ', result14.start())
print('result14.end() is ', result14.end())
print('result 15 is ', result15)
print('result 16 is ', result16)

#print('result.group(0) is ', result.group(0))
#print('the type of result is ', type(result))

