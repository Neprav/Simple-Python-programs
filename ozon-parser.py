from pathlib import *
import os
import requests
from bs4 import BeautifulSoup as bs
import re
from datetime import date, datetime
import xlrd
import xlsxwriter


HTML_FILE = 'G:\\ozon\\OZON.ru-favorites.html'
MAIN_URL = 'https://www.ozon.ru/context/detail/id/'
HEADERS = {
	'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
	'accept-language': 'ru'}
XL_FILE = Path('my-favorites-ozon.xlsx')



def get_html_from_file(html_file):
	with open(html_file, 'r', encoding='utf-8') as f:
		html = f.read()
	return html

def get_html(url):
	r = requests.get(url, headers=HEADERS)
	print(r.status_code)
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
	
def get_price(soup, class_):	
	try:
		price = soup.find('div', class_=class_).text.split()[0] + ' руб.'		
	except AttributeError:
		price = 'цена не найдена'		
	return price

def parse(favorites_id):
	data = []
	for fav_id in favorites_id:		
		url = MAIN_URL + str(fav_id)
		print(url)
		html = get_html(url)
		soup = bs(html, 'lxml')
		title = soup.find('h1')
		if title:
			title = title.text
		else:
			title = ''
		sold_out = soup.find('h2', text=re.compile('товар закончился'))
		if sold_out:
			another_seller = soup.find('p', text=re.compile('есть у другого продавца'))
			if another_seller:
				price = get_price(soup, 'span.b5o4')
			else:
				price = 'нет в наличии'
		else:
			price = get_price(soup, 'c8q5 c8r0 b1k2')
		data.append({'id': fav_id, 'title': title, 'price': price})
		print(title, '\n')		
	return data


def get_table(path, sheet_index):
	wb = xlrd.open_workbook(path)
	ws = wb.sheet_by_index(sheet_index)
	table = []
	for row in range(ws.nrows):
		curr_row = []
		for col in range(ws.ncols):
			cell = ws.cell(row, col)
			value = cell.value
			if cell.ctype == 3:  # xldate
				converted_date = xlrd.xldate_as_tuple(value, wb.datemode)
				value = datetime(*converted_date).strftime('%d.%m.%Y')
			if row > 0 and col == 0: # первый столбец с id
				value = int(value)
			curr_row.append(value)
		table.append(curr_row)
	return table

def go():
	try:
		myfile = open(XL_FILE, 'r+') 
	except IOError:
		print('Открыт Excel файл!')
		return

	favorites_id = get_favorites()
	data = parse(favorites_id)
	table = get_table(XL_FILE, 0)
	current_date = date.today().strftime('%d.%m.%Y')

	for i, row in enumerate(table):
		if i == 0:
			row.append(current_date)
		else:
			item = data[i-1]
			row.append(item['price'])

	new_workbook = xlsxwriter.Workbook(XL_FILE)
	new_worksheet = new_workbook.add_worksheet()

	for row in range(len(table)):
		for col in range(len(table[0])):
			new_worksheet.write(row, col, table[row][col])
	new_workbook.close()
	os.startfile(XL_FILE)

go()
