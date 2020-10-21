from pathlib import *
import requests
from bs4 import BeautifulSoup as bs
import re
import json


HTML_FILE = 'G:\\ozon\\OZON.ru-favorites.html'
MAIN_URL = 'https://www.ozon.ru/context/detail/id/'
HEADERS = {
	'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
	'accept-language': 'ru',
}


def get_html_from_file(html_file):
	with open(html_file, 'r', encoding='utf-8') as f:
		html = f.read()
	return html

def get_html(url):
	r = requests.get(url, headers=HEADERS)	
	return r.text

def get_favorites():
	html = get_html_from_file(HTML_FILE)
	soup = bs(html, 'lxml')	
	divs = soup.select('div.a0c6.a0c9.a0c8 a.a2g0.tile-hover-target')
	favorites_id = []
	for div in divs:
		link = div.get('href')		
		favorites_id.append(Path(link).name)
	favorites_id.remove('1984-173401194')
	return favorites_id
	
def get_price(soup, selector):	
	try:
		price = soup.select_one(selector).text.split()[0] + ' руб.'
	except:
		price = 'цена не найдена'
	return price


# favorites_id = get_favorites()

# for fav_id in favorites_id:
# 	url = MAIN_URL + str(fav_id)
# 	print(url)	
# 	html = get_html(url)

# url = MAIN_URL + str(favorites_id[0])

url = MAIN_URL + '143714909'
html = get_html(url)
soup = bs(html, 'lxml')

title = soup.find('h1').text

sold_out = soup.find('h2', text=re.compile('товар закончился'))

if sold_out:
	another_seller = soup.find('p', text=re.compile('есть у другого продавца'))
	if another_seller:
		price = get_price(soup, 'span.b5o4')
	else:
		price = 'нет в наличии'
else:
	price = get_price(soup, 'span.b3d.b3n5')


print(title)
print(price)





