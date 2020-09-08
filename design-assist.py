from pathlib import *

path_win = Path(r'I:\САЙТЫ ДЛЯ ФОТОГРАФОВ\Графика')

for content in path_win.iterdir():
	if content.is_dir():
		jpg = False		
		name = str(content.name)
		name = name[:100] + '.jpg'
		for inner in content.iterdir():
			if inner.suffix == '.jpg':				
				inner.replace(inner.parents[1] / name)
				jpg = True
		if not jpg:
			print(f'В папке "{content.name}" jpg не найден')









