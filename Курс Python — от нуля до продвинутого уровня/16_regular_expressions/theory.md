# 📘 Тема 16: Регулярные выражения

## Модуль re

```python
import re

# Поиск первого совпадения
match = re.search(r"\d+", "Мне 25 лет")
if match:
    print(match.group())  # "25"

# Все совпадения
results = re.findall(r"\d+", "10 яблок и 20 груш")
# ["10", "20"]

# Замена
text = re.sub(r"\d+", "X", "10 яблок и 20 груш")
# "X яблок и X груш"

# Разбиение
parts = re.split(r"[,;]\s*", "a, b; c, d")
# ["a", "b", "c", "d"]
```

## Основные символы

| Символ | Значение |
|--------|----------|
| `.` | Любой символ (кроме \n) |
| `\d` | Цифра [0-9] |
| `\D` | НЕ цифра |
| `\w` | Буква, цифра, _ |
| `\W` | НЕ буква/цифра |
| `\s` | Пробельный символ |
| `\S` | НЕ пробельный |
| `^` | Начало строки |
| `$` | Конец строки |

## Квантификаторы

| Символ | Значение |
|--------|----------|
| `*` | 0 или более |
| `+` | 1 или более |
| `?` | 0 или 1 |
| `{n}` | Ровно n |
| `{n,m}` | От n до m |

## Группы

```python
match = re.search(r"(\d{2})\.(\d{2})\.(\d{4})", "Дата: 15.03.2024")
if match:
    day, month, year = match.groups()

# Именованные группы
match = re.search(r"(?P<name>\w+)@(?P<domain>\w+\.\w+)", "user@mail.com")
print(match.group("name"))    # "user"
print(match.group("domain"))  # "mail.com"
```

## Флаги

```python
re.findall(r"python", "Python PYTHON", re.IGNORECASE)
re.findall(r"^\w+", text, re.MULTILINE)
```

## Примеры паттернов

```python
email = r"[\w.-]+@[\w.-]+\.\w+"
phone = r"\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{2}[-.\s]?\d{2}"
url = r"https?://[\w./\-?=&]+"
```
