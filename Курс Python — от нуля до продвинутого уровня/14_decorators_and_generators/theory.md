# 📘 Тема 14: Декораторы и генераторы

## Декораторы

Декоратор — функция, которая принимает другую функцию и расширяет её поведение.

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
    print(f"Привет, {name}!")

say_hello("Алиса")
# До вызова
# Привет, Алиса!
# После вызова
```

### Декоратор с параметрами

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Привет!")
```

### functools.wraps

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)   # сохраняет имя и docstring
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## Генераторы

Генератор — функция с `yield` вместо `return`. Ленивая генерация значений.

```python
def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1

for num in count_up(5):
    print(num)  # 0, 1, 2, 3, 4
```

### Генераторное выражение

```python
squares = (x**2 for x in range(10))  # генератор, НЕ кортеж
print(next(squares))  # 0
print(next(squares))  # 1
```

### Преимущества генераторов

- Экономят память (значения создаются по одному)
- Подходят для больших данных и потоков
- Можно создавать бесконечные последовательности

### yield from

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

list(flatten([1, [2, 3], [4, [5, 6]]]))
# [1, 2, 3, 4, 5, 6]
```

### send() — отправка значений в генератор

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)         # запуск, получаем 0
acc.send(10)      # 10
acc.send(20)      # 30
```
