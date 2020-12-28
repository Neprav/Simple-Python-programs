from pathlib import *
import shutil

dirs = [{
'main_dir': Path('I:\\САЙТЫ ДЛЯ ФОТОГРАФОВ'),
'backup_dir': Path('H:\\Б - САЙТЫ ДЛЯ ФОТОГРАФОВ')},
{
'main_dir': Path('E:\\PYTHON'),
'backup_dir': Path('H:\\Б - Python')},
]

count_files, count_dirs = 0, 0

# Собираем путь 
def path_assemble(path):
	new_path = backup_dir
	parts = list(path.parts[len_main_dir:])
	for part in parts:
		new_path = new_path / part
	return new_path

# Рекурсивно погружаемся в каталоги
def dipping(path):
	global count_files
	global count_dirs
	for path in path.iterdir():		
		if path.is_dir():
			copy_dir = path_assemble(path)
			if not copy_dir.exists():
				copy_dir.mkdir()				
				print(f'Создана папка "{path}"')
				count_dirs += 1	
			dipping(path)
		else:
			copy_file = path_assemble(path)
			if not copy_file.exists() or path.stat().st_mtime > copy_file.stat().st_mtime:
				try:
					shutil.copy(path, copy_file)
				except PermissionError:
					print(f'Ошибка доступа! "{path}"')
				print(f'Скопирован файл "{path}"')
				count_files += 1

for item in dirs:
	main_dir = item['main_dir']
	backup_dir = item['backup_dir']
	len_main_dir = len(main_dir.parts)
	dipping(main_dir)

print('====================================')
print(f'Создано {count_dirs} папок, скопировано {count_files} файлов')
