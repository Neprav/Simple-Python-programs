from pathlib import *
import shutil

main_dir = Path('контрольный каталог')
backup_dir = Path('каталог для бэкапа')
len_main = len(main_dir.parts)
len_backup = len(backup_dir.parts)
count_f, count_d = 0, 0

def path_assemble(pth):
	path = backup_dir
	parts = list(pth.parts[len_main:])
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

dipping(main_dir)

print(f'Создано {count_d} папок, скопировано {count_f} файлов')












