#parsing test
import requests
from bs4 import BeautifulSoup

# Http get request
req = requests.get('https://beomi.github.io/beomi.github.io_old/')

# getting html source
html = req.text

soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
	'h3 > a'
	)

# my_titles is the object of list
for title in my_titles:
	print(title.text)
	print(title.get('href'))

