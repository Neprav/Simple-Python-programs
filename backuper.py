from pathlib import *


main_dir = Path('H:\\Тест')
backup_dir = Path('H:\\Тест - бэкап')



def dipping (path):
	for pth in path.iterdir():
		print(pth.parts)
		if pth.is_dir():
			проверка: backup/pth Существует? Если нет, то создать
			dipping(d)
		проверка backup/pth Существует? Если нет, то копировать
		проверка даты изменения, если свежая, то заменить



dipping(main_dir)


Нужно отсечь от пути часть слева
заменить каталог и прибавить остаток пути


for i in parts: # Так прибавляем кусок пути
	d = d / i

len(main_dir.parts) # Так пределяем глубину вложенности


test_dir.stat().st_mtime # Так определяем дату последнего изменения













