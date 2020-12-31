# Simple Python programs
Моя коллекция простых программ, написанных для личного использования.

## design-assist.py

Анализирует каталоги в заданной папке, заходит в каждый, находит там jpg, присваивает ему имя, аналогичное родительскому каталогу и вытаскивает этот jpg на уровень выше.

**Использованные модули:** pathlib

## invest-calc.py

Инвестиционный калькулятор. 

![invest-calc.jpg](https://raw.githubusercontent.com/Neprav/Simple-Python-programs/master/screenshots/invest-calc-1.jpg)

**Использованные модули:** tkinter

## backuper.py

Сравнивает две папки: контрольную и папку бэкапа. Если в контрольной папке появились новые папки или файлы — копирует их в бэкап. Если в контрольной папке есть файлы с датой изменения более свежей, чем их бэкап-копия — копирует их с заменой.

**Использованные модули:** pathlib, shutil

## ozon-parser.py

Парсит цены на заданный список товаров и сохраняет их в excel-таблицу. Удобно для отслеживания изменения цен.

![ozon-parser screenshot](https://github.com/Neprav/Simple-Python-programs/blob/master/screenshots/ozon-parser.JPG)

**Использованные модули:** pathlib, os, requests, bs4, re, datetime, xlrd, xlsxwriter
