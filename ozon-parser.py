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

# Получаем id нужных товаров из оффлайн-файла
def get_favorites():
	html = get_html_from_file(HTML_FILE)
	soup = bs(html, 'lxml')	
	divs = soup.select('div.a0c6.a0c9.a0c8 a.a2g0.tile-hover-target')
	favorites_id = []
	for div in divs:
		link = div.get('href')		
		favorites_id.append(Path(link).name)
	favorites_id.remove('1984-173401194')
	return favorites_id#[:3] # список вида ['148744120', '148744119', ...]
	
def get_price(soup, class_):	
	try:
		price = soup.find('div', class_=class_).text.split()
		if price[1].isdigit():
			price = price[0] + price[1] + ' руб.'
		else:
			price = price[0] + ' руб.'
		# price2 = soup.find('div', class_=class_).text
		# price2 = re.match(r'\d+\s\d+', price2).group(0)
		# price2 = ''.join(price2.split())
	
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

def table_format(first_start=False, range_col=2):
	wb = xlsxwriter.Workbook(XL_FILE)
	ws = wb.add_worksheet()
	common_format = wb.add_format()
	common_format.set_align('left')
	common_format.set_align('vcenter')
	common_format.set_text_wrap()
	header_format = wb.add_format({'bold': True})
	ws.set_row(0, None, header_format)
	ws.set_column(0, 0, 15, common_format)
	ws.set_column(1, 1, 50, common_format)
	if not first_start:
		ws.set_column(2, range_col, 10, common_format)
	return wb, ws

def first_start(data):	
	wb, ws = table_format(first_start=True)
	ws.write('A1', 'id')
	ws.write('B1', 'Название')

	for i, raw in enumerate(data):
		ws.write(i+1, 0, int(raw['id']))
		ws.write(i+1, 1, raw['title'])
	wb.close()

def main():
	file_exists = XL_FILE.exists()
	if file_exists:
		try:
			myfile = open(XL_FILE, 'r+') 
		except IOError:
			print('Открыт Excel файл!')
			return

	favorites_id = get_favorites()
	data = parse(favorites_id) # data - список словарей
	if not file_exists:
		first_start(data)

	table = get_table(XL_FILE, 0) # (имя файла, индекс листа)
	current_date = date.today().strftime('%d.%m.%Y')

	for i, row in enumerate(table):
		if i == 0:
			row.append(current_date)
		else:
			item = data[i-1]
			row.append(item['price'])

	range_col=len(table[0])
	wb, ws = table_format(range_col=range_col)

	for row in range(len(table)):
		for col in range(len(table[0])):
			ws.write(row, col, table[row][col])

	wb.close()
	os.startfile(XL_FILE)

main()
