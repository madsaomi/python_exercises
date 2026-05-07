# 📘 Тема 8: Функции

## Определение функции

```python
def greet(name):
    """Приветствует пользователя."""
    return f"Привет, {name}!"

result = greet("Алиса")
print(result)
```

## Параметры по умолчанию

```python
def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"

greet("Алиса")            # "Привет, Алиса!"
greet("Борис", "Здравствуй")  # "Здравствуй, Борис!"
```

## `*args` и `**kwargs`

```python
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4)  # 10

def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info(name="Алиса", age=25)
```

## Возврат нескольких значений

```python
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([3, 1, 4, 1, 5])
```

## Область видимости (scope)

```python
x = 10         # глобальная

def func():
    x = 20     # локальная
    print(x)   # 20

func()
print(x)       # 10

def func2():
    global x
    x = 30     # меняет глобальную

func2()
print(x)       # 30
```

## Lambda-функции

```python
square = lambda x: x ** 2
add = lambda a, b: a + b

nums = [5, 2, 8, 1]
sorted(nums, key=lambda x: -x)  # [8, 5, 2, 1]
```

## Функции высшего порядка

```python
# map — применить функцию к каждому элементу
list(map(str.upper, ["a", "b", "c"]))  # ["A", "B", "C"]

# filter — отфильтровать
list(filter(lambda x: x > 3, [1, 2, 3, 4, 5]))  # [4, 5]

# reduce
from functools import reduce
reduce(lambda a, b: a + b, [1, 2, 3, 4])  # 10
```

## Рекурсия

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

## Аннотации типов

```python
def add(a: int, b: int) -> int:
    return a + b
```
