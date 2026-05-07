# 📘 Тема 9: Работа с файлами

## Открытие и закрытие файлов

```python
# Рекомендуемый способ (with):
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
# файл автоматически закрывается

# Ручной способ (НЕ рекомендуется):
f = open("file.txt", "r")
content = f.read()
f.close()
```

## Режимы открытия

| Режим | Описание |
|-------|----------|
| `"r"` | Чтение (по умолчанию) |
| `"w"` | Запись (перезаписывает!) |
| `"a"` | Дополнение (добавляет в конец) |
| `"x"` | Создание (ошибка если существует) |
| `"rb"` | Чтение в бинарном режиме |
| `"wb"` | Запись в бинарном режиме |

## Чтение файлов

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()          # весь файл как строка
    lines = f.readlines()       # список строк
    line = f.readline()         # одна строка
    
    # Построчно (экономит память):
    for line in f:
        print(line.strip())
```

## Запись в файл

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Первая строка\n")
    f.write("Вторая строка\n")
    f.writelines(["a\n", "b\n", "c\n"])

# Дополнение:
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("Новая строка\n")
```

## Работа с путями (pathlib)

```python
from pathlib import Path

p = Path("data/file.txt")
p.exists()          # существует ли?
p.is_file()         # это файл?
p.is_dir()          # это директория?
p.name              # "file.txt"
p.stem              # "file"
p.suffix            # ".txt"
p.parent            # Path("data")
p.read_text()       # прочитать
p.write_text("hi")  # записать
```

## JSON

```python
import json

# Запись
data = {"name": "Алиса", "age": 25}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Чтение
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
```

## CSV

```python
import csv

# Запись
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Имя", "Возраст"])
    writer.writerow(["Алиса", 25])

# Чтение
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

## os и shutil

```python
import os, shutil

os.listdir(".")           # содержимое директории
os.makedirs("dir/sub")    # создать директории
os.remove("file.txt")     # удалить файл
os.rename("old", "new")   # переименовать
shutil.copy("a.txt", "b.txt")  # копировать
shutil.rmtree("dir")      # удалить директорию
```
