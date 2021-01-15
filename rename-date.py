from pathlib import *
import re

path = Path(r'Путь')
date_mask = r'\d{2}.\d{2}.\d{4}'

for folder in path.iterdir():
	if folder.is_dir():
		print('Было:  ', folder)
		name = folder.name
		date = re.search(date_mask, name)
		if date:
			date = date.group(0)
			name = name.replace(date, '')
			name = name.replace('—', '')
			date_split = date.split('.')
			date_inverse = date_split[::-1]
			date = '.'.join(date_inverse)
			name = date + ' — ' + name
			name = re.sub(' +', ' ', name)
			new_path = folder.parent / name
			print('Стало: ', new_path)
			folder.rename(new_path)
		else:
			print('Стало: ', folder)
