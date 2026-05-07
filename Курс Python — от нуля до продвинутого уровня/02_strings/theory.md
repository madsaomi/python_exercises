# 📘 Тема 2: Строки и их методы

## Создание строк

Строки можно создавать с помощью одинарных, двойных или тройных кавычек:

```python
s1 = 'Привет'
s2 = "Мир"
s3 = '''Многострочная
строка'''
s4 = """Ещё одна
многострочная строка"""
```

---

## Индексация строк

Каждый символ в строке имеет свой **индекс** (начиная с 0):

```python
text = "Python"
#       P y t h o n
#       0 1 2 3 4 5    — прямая индексация
#      -6-5-4-3-2-1    — обратная индексация

print(text[0])    # P
print(text[-1])   # n
print(text[2])    # t
```

---

## Срезы (slicing)

Синтаксис: `строка[start:stop:step]`

```python
text = "Hello, World!"

print(text[0:5])     # Hello
print(text[7:])      # World!
print(text[:5])      # Hello
print(text[::2])     # Hlo ol!
print(text[::-1])    # !dlroW ,olleH  — реверс строки
print(text[-6:-1])   # World
```

---

## Основные методы строк

### Регистр

```python
s = "hello world"

s.upper()        # "HELLO WORLD"
s.lower()        # "hello world"
s.capitalize()   # "Hello world"
s.title()        # "Hello World"
s.swapcase()     # "HELLO WORLD"
```

### Поиск и замена

```python
s = "Hello, World!"

s.find("World")       # 7  (индекс начала)
s.find("Python")      # -1 (не найдено)
s.index("World")      # 7  (как find, но вызовет ошибку если не найдено)
s.count("l")          # 3  (количество вхождений)
s.replace("World", "Python")  # "Hello, Python!"
s.startswith("Hello") # True
s.endswith("!")        # True
```

### Проверки

```python
"hello".isalpha()     # True  — только буквы
"12345".isdigit()     # True  — только цифры
"hello123".isalnum()  # True  — буквы и цифры
"   ".isspace()       # True  — только пробелы
"Hello".isupper()     # False
"hello".islower()     # True
```

### Удаление пробелов

```python
s = "   Hello   "

s.strip()    # "Hello"      — убирает с обеих сторон
s.lstrip()   # "Hello   "   — убирает слева
s.rstrip()   # "   Hello"   — убирает справа
```

### Разделение и объединение

```python
# split — разбить строку в список
"a,b,c,d".split(",")           # ['a', 'b', 'c', 'd']
"Hello World".split()           # ['Hello', 'World']

# join — объединить список в строку
", ".join(["a", "b", "c"])      # "a, b, c"
"-".join(["2024", "01", "15"])   # "2024-01-15"
```

---

## Форматирование строк

### f-строки (рекомендуется, Python 3.6+)

```python
name = "Алиса"
age = 25

print(f"Имя: {name}, возраст: {age}")
print(f"Через 5 лет будет {age + 5}")
print(f"Число пи: {3.14159:.2f}")      # 3.14
print(f"{'Python':>20}")               # выравнивание вправо
print(f"{'Python':<20}")               # выравнивание влево
print(f"{'Python':^20}")               # по центру
```

### Метод `.format()`

```python
print("Имя: {}, возраст: {}".format("Алиса", 25))
print("Имя: {name}, возраст: {age}".format(name="Алиса", age=25))
```

### Оператор `%` (устаревший стиль)

```python
print("Имя: %s, возраст: %d" % ("Алиса", 25))
```

---

## Экранирование символов

| Символ | Значение |
|--------|----------|
| `\n` | Перенос строки |
| `\t` | Табуляция |
| `\\` | Обратный слэш |
| `\'` | Одинарная кавычка |
| `\"` | Двойная кавычка |

```python
print("Строка 1\nСтрока 2")
print("Имя:\tАлиса")
print("Путь: C:\\Users\\Documents")
```

---

## Строки — неизменяемый тип

Строки в Python **нельзя изменить на месте**:

```python
s = "Hello"
# s[0] = "h"  # ❌ TypeError!

# Нужно создать новую строку:
s = "h" + s[1:]  # "hello"  ✅
```

---

## Полезные функции

```python
text = "Hello"

len(text)      # 5    — длина строки
"ell" in text  # True — проверка вхождения
min(text)      # 'H'  — минимальный символ (по ASCII)
max(text)      # 'o'  — максимальный символ
ord('A')       # 65   — код символа
chr(65)        # 'A'  — символ по коду
```
