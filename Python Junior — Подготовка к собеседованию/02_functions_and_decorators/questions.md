# 02 — Функции и декораторы: Теоретические вопросы

---

## Вопрос 1: Что такое замыкание (closure)?

<details>
<summary>💡 Ответ</summary>

**Замыкание** — это функция, которая запоминает переменные из своей объемлющей области видимости, даже после того как внешняя функция завершила выполнение.

```python
def make_multiplier(x):
    def multiplier(n):
        return x * n  # x «замкнута» — сохранена из внешней функции
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

Переменная `x` хранится в `__closure__` возвращённой функции.
</details>

---

## Вопрос 2: Что такое декоратор и как он работает?

<details>
<summary>💡 Ответ</summary>

**Декоратор** — это функция, которая принимает другую функцию и возвращает модифицированную версию.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("До вызова")
        result = func(*args, **kwargs)
        print("После вызова")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Эквивалентно: say_hello = my_decorator(say_hello)
say_hello("World")
```

Вывод:
```
До вызова
Hello, World!
После вызова
```
</details>

---

## Вопрос 3: Зачем нужен `functools.wraps`?

<details>
<summary>💡 Ответ</summary>

Без `@wraps` декорированная функция теряет своё имя, docstring и другие атрибуты:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # сохраняет __name__, __doc__ оригинальной функции
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def hello():
    """Приветствие"""
    pass

print(hello.__name__)  # "hello" (без @wraps было бы "wrapper")
print(hello.__doc__)   # "Приветствие" (без @wraps было бы None)
```
</details>

---

## Вопрос 4: В чём разница между генератором и обычной функцией?

<details>
<summary>💡 Ответ</summary>

| Функция | Генератор |
|---------|-----------|
| `return` — возвращает значение и завершается | `yield` — «приостанавливается», сохраняя состояние |
| Выполняется полностью за один вызов | Ленивое вычисление — по одному элементу |
| Хранит весь результат в памяти | Хранит только текущее состояние |

```python
# Функция — всё в памяти
def get_squares_list(n):
    return [x**2 for x in range(n)]

# Генератор — ленивое вычисление
def get_squares_gen(n):
    for x in range(n):
        yield x**2

# Для 10 млн элементов генератор экономит гигабайты памяти
```
</details>

---

## Вопрос 5: Как работает `yield from`?

<details>
<summary>💡 Ответ</summary>

`yield from` делегирует генерацию другому итерируемому объекту:

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)  # делегирует вложенному генератору
        else:
            yield item

print(list(flatten([1, [2, [3, 4]], 5])))  # [1, 2, 3, 4, 5]
```

Без `yield from` пришлось бы писать вложенный `for`:
```python
for x in flatten(item):
    yield x
```
</details>

---

## Вопрос 6: Что такое лямбда-функция и когда её использовать?

<details>
<summary>💡 Ответ</summary>

**Lambda** — анонимная функция из одного выражения:

```python
square = lambda x: x ** 2

# Основное применение — передача в функции высшего порядка
sorted_data = sorted(users, key=lambda u: u["age"])
filtered = list(filter(lambda x: x > 0, numbers))
```

**Когда НЕ использовать:**
- Сложная логика (используйте обычную функцию)
- Присваивание переменной (нарушает PEP 8: `square = lambda x: x**2` ❌)
- Нужен docstring или несколько выражений
</details>

---

## Вопрос 7: Как создать декоратор с параметрами?

<details>
<summary>💡 Ответ</summary>

Нужен **тройной** уровень вложенности:

```python
from functools import wraps

def repeat(n):                     # принимает параметр декоратора
    def decorator(func):           # принимает функцию
        @wraps(func)
        def wrapper(*args, **kwargs):  # принимает аргументы функции
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("World")  # Напечатает "Hello, World!" три раза
```
</details>

---

## Вопрос 8: Что такое `map()`, `filter()`, `reduce()`?

<details>
<summary>💡 Ответ</summary>

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]

# map — применяет функцию к каждому элементу
squares = list(map(lambda x: x**2, nums))  # [1, 4, 9, 16, 25]

# filter — оставляет элементы, для которых функция вернула True
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

# reduce — сворачивает список в одно значение
total = reduce(lambda a, b: a + b, nums)  # 15
```

**В современном Python** чаще используют comprehensions и `sum()`:
```python
squares = [x**2 for x in nums]       # вместо map
evens = [x for x in nums if x % 2 == 0]  # вместо filter
total = sum(nums)                     # вместо reduce
```
</details>

---

## Вопрос 9: Что такое рекурсия и какие у неё ограничения в Python?

<details>
<summary>💡 Ответ</summary>

**Рекурсия** — функция, которая вызывает сама себя.

**Ограничения:**
- Лимит глубины рекурсии: **~1000** вызовов по умолчанию
- Можно изменить: `sys.setrecursionlimit(5000)` (опасно — может привести к segfault)
- Python **не оптимизирует хвостовую рекурсию** (в отличие от некоторых языков)

```python
# Рекурсивный факториал
def factorial(n):
    if n <= 1:    # базовый случай
        return 1
    return n * factorial(n - 1)  # рекурсивный вызов

# Итеративная альтернатива (предпочтительнее для больших n)
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```
</details>

---

## Вопрос 10: Что такое `nonlocal` и `global`?

<details>
<summary>💡 Ответ</summary>

- `global` — позволяет **изменять** переменную из глобальной области видимости
- `nonlocal` — позволяет **изменять** переменную из объемлющей функции

```python
count = 0

def increment():
    global count    # без этого будет UnboundLocalError
    count += 1

def outer():
    x = 10
    def inner():
        nonlocal x  # без этого создалась бы локальная переменная
        x += 1
    inner()
    print(x)  # 11

outer()
```

**Совет:** Избегайте `global` — это усложняет отладку. Лучше передавайте и возвращайте значения явно.
</details>

---

## Вопрос 11: Чем `*args` отличается от `**kwargs`?

<details>
<summary>💡 Ответ</summary>

- `*args` — собирает позиционные аргументы в **кортеж**
- `**kwargs` — собирает именованные аргументы в **словарь**

```python
def example(*args, **kwargs):
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

example(1, 2, 3, name="Py", ver=3)
# args = (1, 2, 3)
# kwargs = {'name': 'Py', 'ver': 3}
```

**Порядок:** `def f(pos, /, normal, *args, kw_only, **kwargs)`
</details>

---

## Вопрос 12: Как работает протокол итераторов в Python?

<details>
<summary>💡 Ответ</summary>

Итератор должен реализовать два метода:
- `__iter__()` — возвращает самого себя
- `__next__()` — возвращает следующий элемент или бросает `StopIteration`

```python
class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for num in CountUp(1, 4):
    print(num)  # 1, 2, 3
```
</details>

---

## Вопрос 13: Можно ли применить несколько декораторов к одной функции?

<details>
<summary>💡 Ответ</summary>

Да. Декораторы применяются **снизу вверх** (ближайший к функции — первый):

```python
@decorator_a
@decorator_b
def my_func():
    pass

# Эквивалентно:
# my_func = decorator_a(decorator_b(my_func))
```

Порядок важен! `decorator_b` оборачивает функцию первым, `decorator_a` — вторым.
</details>

---

## Вопрос 14: Что такое генераторное выражение?

<details>
<summary>💡 Ответ</summary>

Генераторное выражение — синтаксис создания генератора в одну строку (как list comprehension, но с круглыми скобками):

```python
# List comprehension — создаёт весь список в памяти
squares_list = [x**2 for x in range(1000000)]

# Generator expression — ленивое вычисление
squares_gen = (x**2 for x in range(1000000))

# Можно передавать напрямую в функции
total = sum(x**2 for x in range(1000000))  # скобки не нужны
```

Генераторное выражение экономит память, но его можно пройти только один раз.
</details>

---

## Вопрос 15: Что такое функция высшего порядка?

<details>
<summary>💡 Ответ</summary>

**Функция высшего порядка** — функция, которая принимает другую функцию как аргумент или возвращает функцию.

```python
# Принимает функцию
def apply_twice(func, value):
    return func(func(value))

result = apply_twice(lambda x: x * 2, 3)  # 12

# Возвращает функцию
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add5 = make_adder(5)
print(add5(10))  # 15
```

Примеры из стандартной библиотеки: `map()`, `filter()`, `sorted(key=...)`, `functools.reduce()`.
</details>
