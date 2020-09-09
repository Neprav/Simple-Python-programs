from bs4 import BeautifulSoup
import requests
from pathlib import *
import json


html_file = 'G:\\Behance-2\\Behance __ Лучшее из Behance.html'
project_path = Path('Behance-parse')
json_path = project_path / 'json-files'
file_txt = project_path / 'Behance-users.txt'
api_key = 'your API key'



def parse_from_file():

	with open(html_file, 'r', encoding='utf-8') as f:
		html = f.read()

	soup = BeautifulSoup(html, 'lxml')

	all_links = soup.find_all('a', class_='Owners-owner-2lB')

	for i, link in enumerate(all_links):
		all_links[i] = link.get('href').split('/')[-1]
	all_links = list(set(all_links))

	with open(file_txt, 'w') as f:
		for name in all_links:
			f.write(f'{name}\n')



def get_json(user):
	url = f'https://www.behance.net/v2/users/{user}?api_key={api_key}'
	r = requests.get(url)
	data_json = json.loads(r.text)
	return data_json



with open(file_txt) as f:
	user_list = f.read().split('\n')[:-1]

json_files = len(list(json_path.iterdir()))
total = len(user_list) + json_files
done = []

for user in user_list:	

	data_json = get_json(user)
	if data_json['http_code'] == 200:
		file_name = user + '.json'
		file = json_path / file_name
		with open(file, 'w', encoding='utf-8') as f:
			json.dump(data_json, f)
		done.append(user)
		print(f'Спарсили {json_files + len(done)} из {total}')
	else:
		print(f"HTTP CODE: {data_json['http_code']}")
		user_list = list(set(user_list) - set(done))
		with open(file_txt, 'w') as f:
			for name in user_list:
				f.write(f'{name}\n')			
		break






# user = 'federicocedrone'

# with open(file, encoding='utf-8') as f:
# 	data_json = json.load(f)





