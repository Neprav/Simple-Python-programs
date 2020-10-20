from pathlib import *
import shutil


dirs = [{
'main_dir': Path('I:\\САЙТЫ ДЛЯ ФОТОГРАФОВ'),
'backup_dir': Path('H:\\Б - САЙТЫ ДЛЯ ФОТОГРАФОВ')},
{
'main_dir': Path('E:\\PYTHON'),
'backup_dir': Path('H:\\Б - Python')},
]

count_f, count_d = 0, 0

def path_assemble(pth):
	path = backup_dir
	parts = list(pth.parts[len_main_dir:])
	for part in parts: 
		path = path / part
	return path

def dipping (path):
	global count_f
	global count_d
	for pth in path.iterdir():		
		if pth.is_dir():
			copy_dir = path_assemble(pth)
			if not copy_dir.exists():
				copy_dir.mkdir()				
				print(f'Создана папка "{pth.name}"')
				count_d += 1	
			dipping(pth)
		else:
			copy_file = path_assemble(pth)
			if not copy_file.exists() or pth.stat().st_mtime > copy_file.stat().st_mtime:
				try:
					shutil.copy(pth, copy_file)
				except PermissionError:
					print(f'Ошибка доступа! "{pth.name}"')
				print(f'Скопирован файл "{pth.name}"')
				count_f += 1


for item in dirs:
	main_dir = item['main_dir']
	backup_dir = item['backup_dir']
	len_main_dir = len(main_dir.parts)
	dipping(main_dir)


print(f'Создано {count_d} папок, скопировано {count_f} файлов')











