books = []
prompt = 'Enter new book: '
user_input = input(prompt).strip()

while (user_input.lower() != 'exit'):
	books.append(user_input)
	user_input = input(prompt).strip()

print(books)

books.sort()
print(books)

for book in books:
	print(book)
