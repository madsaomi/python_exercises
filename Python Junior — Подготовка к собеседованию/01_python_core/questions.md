# 01 — Основы и устройство Python: Теоретические вопросы

---

## Вопрос 1: Чем отличается `is` от `==`?

<details>
<summary>💡 Ответ</summary>

- `==` сравнивает **значения** объектов (вызывает метод `__eq__`)
- `is` сравнивает **идентичность** объектов (совпадают ли адреса в памяти, т.е. `id()`)

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True — значения одинаковые
print(a is b)  # False — это разные объекты в памяти

c = a
print(a is c)  # True — c ссылается на тот же объект
```

**Важно:** Для `None` всегда используйте `is`:
```python
if x is None:    # ✅ правильно
if x == None:    # ❌ неправильно (может быть переопределён __eq__)
```
</details>

---

## Вопрос 2: Какие типы данных в Python изменяемые, а какие — нет?

<details>
<summary>💡 Ответ</summary>

**Неизменяемые (immutable):**
- `int`, `float`, `bool`
- `str`
- `tuple`
- `frozenset`
- `None`

**Изменяемые (mutable):**
- `list`
- `dict`
- `set`
- Пользовательские объекты (по умолчанию)

**Почему это важно:**
- Неизменяемые объекты могут быть ключами словаря и элементами множества
- Изменяемые объекты нельзя хешировать
- При передаче изменяемого объекта в функцию — он может быть изменён внутри

```python
def add_item(lst):
    lst.append(42)

my_list = [1, 2, 3]
add_item(my_list)
print(my_list)  # [1, 2, 3, 42] — список изменился!
```
</details>

---

## Вопрос 3: Что такое интернирование (interning) в Python?

<details>
<summary>💡 Ответ</summary>

Python кэширует (интернирует) некоторые объекты для экономии памяти:

**Целые числа от -5 до 256:**
```python
a = 256
b = 256
print(a is b)  # True — один и тот же объект

a = 257
b = 257
print(a is b)  # False (в интерактивном режиме) — разные объекты
```

**Короткие строки (без пробелов и спецсимволов):**
```python
a = "hello"
b = "hello"
print(a is b)  # True — строка интернирована

a = "hello world"
b = "hello world"
print(a is b)  # Может быть False (зависит от реализации)
```

**Зачем знать:** Чтобы понимать, почему `is` иногда «работает» для чисел и строк, но это — деталь реализации CPython, а не гарантия языка.
</details>

---

## Вопрос 4: Как работает передача аргументов в Python — по ссылке или по значению?

<details>
<summary>💡 Ответ</summary>

В Python — **ни то, ни другое**. Используется механизм **«передача по присваиванию» (pass by assignment)**, также называемый **«передача по ссылке на объект» (pass by object reference)**.

- Функция получает **ссылку** на объект
- Если объект **изменяемый** — его можно изменить внутри функции
- Если объект **неизменяемый** — создаётся новый объект

```python
# Изменяемый объект — изменяется
def modify(lst):
    lst.append(4)

data = [1, 2, 3]
modify(data)
print(data)  # [1, 2, 3, 4]

# Неизменяемый объект — НЕ изменяется
def modify(x):
    x = x + 1  # создаётся новый int

num = 10
modify(num)
print(num)  # 10
```

**Ловушка:** Переприсваивание внутри функции НЕ влияет на внешнюю переменную:
```python
def modify(lst):
    lst = [4, 5, 6]  # создаёт НОВЫЙ список, не меняет оригинал

data = [1, 2, 3]
modify(data)
print(data)  # [1, 2, 3] — не изменился!
```
</details>

---

## Вопрос 5: В чём разница между shallow copy и deep copy?

<details>
<summary>💡 Ответ</summary>

**Shallow copy (поверхностная копия):**
- Создаёт новый объект, но вложенные объекты копируются **по ссылке**
- Способы: `list.copy()`, `dict.copy()`, `copy.copy()`, срез `[:]`

**Deep copy (глубокая копия):**
- Создаёт новый объект и **рекурсивно** копирует все вложенные объекты
- Способ: `copy.deepcopy()`

```python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append(99)

print(shallow)  # [[1, 2, 99], [3, 4]] — вложенный список изменился!
print(deep)     # [[1, 2], [3, 4]]     — глубокая копия независима
```
</details>

---

## Вопрос 6: Что такое PEP 8 и зачем он нужен?

<details>
<summary>💡 Ответ</summary>

**PEP 8** — это официальное руководство по стилю кода Python (Python Enhancement Proposal #8).

**Ключевые правила:**
- Отступы: **4 пробела** (не табы)
- Максимальная длина строки: **79 символов** (120 для некоторых проектов)
- Именование:
  - Переменные и функции: `snake_case`
  - Классы: `PascalCase`
  - Константы: `UPPER_SNAKE_CASE`
  - Приватные атрибуты: `_single_underscore`
  - Name mangling: `__double_underscore`
- Пустые строки: 2 перед функцией/классом верхнего уровня, 1 между методами
- Импорты: каждый на отдельной строке, в порядке: стандартная библиотека → сторонние → локальные

**Зачем знать:** Код читается чаще, чем пишется. Единый стиль упрощает работу в команде.
</details>

---

## Вопрос 7: Что такое duck typing?

<details>
<summary>💡 Ответ</summary>

**Duck typing** — принцип в Python: «Если объект ходит как утка и крякает как утка — значит, это утка».

Python не проверяет тип объекта — он проверяет, есть ли у объекта нужный **метод или атрибут**.

```python
class Duck:
    def quack(self):
        print("Кря!")

class Person:
    def quack(self):
        print("Я притворяюсь уткой!")

def make_quack(thing):
    thing.quack()  # Python не проверяет тип — только наличие метода

make_quack(Duck())    # Кря!
make_quack(Person())  # Я притворяюсь уткой!
```

**На собеседовании** часто спрашивают как пример динамической типизации Python и противопоставляют статической типизации (Java, C++).
</details>

---

## Вопрос 8: Какие есть области видимости переменных в Python?

<details>
<summary>💡 Ответ</summary>

Python использует правило **LEGB** для поиска переменных:

1. **L**ocal — внутри текущей функции
2. **E**nclosing — в объемлющей функции (замыкание)
3. **G**lobal — на уровне модуля
4. **B**uilt-in — встроенные имена (`print`, `len`, `range` и т.д.)

```python
x = "global"  # Global

def outer():
    x = "enclosing"  # Enclosing
    
    def inner():
        x = "local"  # Local
        print(x)     # → "local"
    
    inner()

outer()
```

**Ключевые слова:**
- `global` — для изменения глобальной переменной изнутри функции
- `nonlocal` — для изменения переменной из объемлющей функции
</details>

---

## Вопрос 9: Что такое list comprehension и когда его лучше НЕ использовать?

<details>
<summary>💡 Ответ</summary>

**List comprehension** — компактный способ создания списков:

```python
# Обычный цикл
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension
squares = [x ** 2 for x in range(10)]
```

**Когда НЕ использовать:**
- Логика слишком сложная (вложенные условия, вызовы функций с побочными эффектами)
- Нужно больше одного уровня вложенности — лучше обычный цикл
- Когда не нужен результирующий список — используйте генератор `()` вместо `[]`

```python
# ❌ Плохо — слишком сложно читать
result = [transform(x) for x in data if validate(x) and x.is_active() for y in x.items if y > 0]

# ✅ Лучше — обычный цикл
result = []
for x in data:
    if validate(x) and x.is_active():
        for y in x.items:
            if y > 0:
                result.append(transform(x))
```
</details>

---

## Вопрос 10: Что такое `*args` и `**kwargs`?

<details>
<summary>💡 Ответ</summary>

- `*args` — принимает **произвольное количество позиционных** аргументов как **кортеж**
- `**kwargs` — принимает **произвольное количество именованных** аргументов как **словарь**

```python
def example(*args, **kwargs):
    print(f"args: {args}")      # кортеж
    print(f"kwargs: {kwargs}")  # словарь

example(1, 2, 3, name="Python", version=3)
# args: (1, 2, 3)
# kwargs: {'name': 'Python', 'version': 3}
```

**Порядок аргументов в определении функции:**
```python
def func(positional, /, normal, *args, keyword_only, **kwargs):
    pass
```

**Распаковка:**
```python
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))  # 6

data = {"a": 1, "b": 2, "c": 3}
print(add(**data))  # 6
```
</details>

---

## Вопрос 11: Что будет, если использовать изменяемый объект как аргумент по умолчанию?

<details>
<summary>💡 Ответ</summary>

Это **классическая ловушка Python**! Аргумент по умолчанию создаётся **один раз** при определении функции, а не при каждом вызове.

```python
def add_item(item, lst=[]):  # ⚠️ опасно!
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] — тот же список!
print(add_item(3))  # [1, 2, 3] — тот же список!
```

**Правильный способ:**
```python
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

**Почему так:** Аргументы по умолчанию вычисляются один раз — при создании объекта функции, а не при каждом вызове.
</details>

---

## Вопрос 12: Чем отличается `__str__` от `__repr__`?

<details>
<summary>💡 Ответ</summary>

- `__str__` — **для пользователя**. Вызывается через `str()` и `print()`. Должен быть читаемым.
- `__repr__` — **для разработчика**. Вызывается в интерактивной консоли. Должен быть однозначным (в идеале — воспроизводимым).

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} лет"
    
    def __repr__(self):
        return f"User(name='{self.name}', age={self.age})"

u = User("Анна", 25)
print(str(u))   # Анна, 25 лет
print(repr(u))  # User(name='Анна', age=25)
```

**Правило:** Если определяете только один — определяйте `__repr__`. Если `__str__` не определён, Python вызовет `__repr__` вместо него.
</details>

---

## Вопрос 13: Что такое итератор и итерируемый объект?

<details>
<summary>💡 Ответ</summary>

**Iterable (итерируемый объект):**
- Объект, у которого есть метод `__iter__()`, возвращающий итератор
- Примеры: `list`, `tuple`, `str`, `dict`, `set`, `range`

**Iterator (итератор):**
- Объект, у которого есть метод `__next__()` (возвращает следующий элемент)
- И метод `__iter__()` (возвращает самого себя)
- Бросает `StopIteration`, когда элементы закончились

```python
my_list = [1, 2, 3]          # iterable
my_iter = iter(my_list)       # iterator

print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
print(next(my_iter))  # StopIteration!
```

**Ключевое отличие:** Итерируемый объект можно пройти многократно. Итератор — только один раз (он «расходуется»).
</details>

---

## Вопрос 14: Для чего используется конструкция `if __name__ == "__main__"`?

<details>
<summary>💡 Ответ</summary>

Эта конструкция позволяет **отличить запуск файла напрямую от импорта**.

- Когда файл запускается напрямую (`python script.py`), переменная `__name__` равна `"__main__"`
- Когда файл импортируется (`import script`), `__name__` равна имени модуля (`"script"`)

```python
# utils.py
def helper():
    return "Привет!"

if __name__ == "__main__":
    # Этот код выполнится ТОЛЬКО при прямом запуске
    print(helper())
    print("Тесты пройдены!")
```

**Зачем нужно:** Чтобы модуль можно было и импортировать (без побочных эффектов), и запускать отдельно (для тестирования).
</details>

---

## Вопрос 15: Что такое GIL и зачем он нужен? (кратко)

<details>
<summary>💡 Ответ</summary>

**GIL (Global Interpreter Lock)** — глобальная блокировка интерпретатора в CPython, которая позволяет **только одному потоку** выполнять Python-байткод в каждый момент времени.

**Зачем:** Упрощает управление памятью (reference counting) и делает C-расширения потокобезопасными.

**Последствия:**
- Многопоточность (`threading`) **НЕ ускоряет** CPU-bound задачи
- Для CPU-bound задач используйте `multiprocessing` (отдельные процессы, каждый со своим GIL)
- Для I/O-bound задач (сеть, файлы) — `threading` или `asyncio` работают нормально

```
CPU-bound → multiprocessing  ✅
I/O-bound → threading / asyncio  ✅
CPU-bound + threading → НЕ ускорит ❌
```

**Важно:** GIL — это особенность реализации **CPython**, а не самого языка Python.
</details>
