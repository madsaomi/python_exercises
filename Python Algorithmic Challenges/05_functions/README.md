# 📘 Functions — Теория

## Функции как объекты первого класса

В Python функции можно передавать как аргументы, возвращать и хранить в переменных.

```python
def apply(func, value):
    return func(value)

apply(abs, -5)  # 5
```

## Замыкания (Closures)

```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
double(5)  # 10
```

## Мемоизация

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)
```

## Полезные встроенные функции

```python
map(func, iterable)       # применить к каждому
filter(pred, iterable)    # отфильтровать
sorted(iterable, key=func)  # сортировка с ключом
any(iterable)             # хоть один True?
all(iterable)             # все True?
zip(iter1, iter2)         # параллельный обход
enumerate(iterable)       # индекс + значение
```

## Паттерны
- **Callback** → передача функции как аргумента
- **Factory** → функция возвращает функцию
- **Декоратор** → обёртка над функцией
- **Мемоизация** → кэширование результатов
