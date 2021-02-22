from pathlib import *
import datetime
import re

path = Path(r'Путь')
date_bad = r'\d{2}.\d{2}.\d{4}'
date_good = r'\d{4}.\d{2}.\d{2}'

for folder in path.iterdir():
	if folder.is_dir():
		print('Было:  ', folder)
		name = folder.name
		date = re.search(date_bad, name)
		if date:			
			date = date.group(0)
			name = name.replace(date, '')
			name = name.replace('—', '')
			date_split = date.split('.')
			date_inverse = date_split[::-1]
			date = '.'.join(date_inverse)
			name = date + ' — ' + name

		elif not re.search(date_good, name):
			creation_time = folder.stat().st_ctime
			creation_date = datetime.date.fromtimestamp(creation_time).strftime('%Y.%m.%d')
			name = creation_date + ' — ' + name

		else:
			print('Стало: ', folder)
			continue

		name = re.sub(' +', ' ', name)
		new_path = folder.parent / name
		print('Стало: ', new_path)
		folder.rename(new_path)
	

