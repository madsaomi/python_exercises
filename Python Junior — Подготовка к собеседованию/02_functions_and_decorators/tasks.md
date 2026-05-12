# 02 — Функции и декораторы: Задачи-ловушки

> ⚠️ Попробуйте предсказать вывод **БЕЗ запуска**.

---

## Задача 1: Замыкание в цикле

```python
funcs = []
for i in range(5):
    funcs.append(lambda: i)

print([f() for f in funcs])
```

<details>
<summary>🔍 Что выведет код?</summary>

```
[4, 4, 4, 4, 4]
```

**Объяснение:** Все лямбды замкнуты на **одну и ту же** переменную `i`. К моменту вызова цикл уже завершился и `i == 4`. Решение: `lambda i=i: i` (значение по умолчанию фиксирует текущее значение).
</details>

---

## Задача 2: Порядок декораторов

```python
def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def greet():
    return "Hello"

print(greet())
```

<details>
<summary>🔍 Что выведет код?</summary>

```
<b><i>Hello</i></b>
```

**Объяснение:** Декораторы применяются снизу вверх: сначала `italic`, потом `bold`. Это эквивалентно `bold(italic(greet))()`.
</details>

---

## Задача 3: Генератор и `return`

```python
def my_gen():
    yield 1
    yield 2
    return "done"
    yield 3

gen = my_gen()
print(next(gen))
print(next(gen))
try:
    print(next(gen))
except StopIteration as e:
    print(f"Stop: {e.value}")
```

<details>
<summary>🔍 Что выведет код?</summary>

```
1
2
Stop: done
```

**Объяснение:** `return` в генераторе вызывает `StopIteration`, а значение `return` становится атрибутом `value` исключения. `yield 3` никогда не выполнится.
</details>

---

## Задача 4: Область видимости и присваивание

```python
x = 10

def foo():
    print(x)

def bar():
    print(x)
    x = 20

foo()
bar()
```

<details>
<summary>🔍 Что выведет код?</summary>

```
10
UnboundLocalError: local variable 'x' referenced before assignment
```

**Объяснение:** В `bar()` есть присваивание `x = 20`, поэтому Python считает `x` **локальной** переменной во всей функции. Попытка `print(x)` до присваивания — ошибка.
</details>

---

## Задача 5: `*args` ловушка

```python
def func(a, b, *args, key=True):
    print(a, b, args, key)

func(1, 2, 3, 4, 5)
func(1, 2, key=False)
func(1, 2, 3, key=False)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
1 2 (3, 4, 5) True
1 2 () False
1 2 (3,) False
```

**Объяснение:** `*args` собирает все «лишние» позиционные аргументы. `key` — keyword-only аргумент (после `*args`), по умолчанию `True`.
</details>

---

## Задача 6: Мутабельный default + рекурсия

```python
def collect(x, result=[]):
    result.append(x)
    if x > 1:
        collect(x - 1)
    return result

print(collect(3))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
[3, 2, 1]
```

**Объяснение:** Все рекурсивные вызовы используют один и тот же список `result` (мутабельный default). Элементы добавляются в порядке: 3, 2, 1. **Второй вызов** `collect(3)` даст `[3, 2, 1, 3, 2, 1]`!
</details>

---

## Задача 7: `lambda` и `if`

```python
funcs = [lambda x: x**2, lambda x: x**3, lambda x: x+1]
print([f(2) for f in funcs])

check = lambda x: "even" if x % 2 == 0 else "odd"
print(check(3))
print(check(4))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
[4, 8, 3]
odd
even
```

**Объяснение:** Лямбды могут содержать тернарный оператор `a if cond else b`, но не `if/elif/else` блоки.
</details>

---

## Задача 8: Генератор — одноразовый

```python
gen = (x**2 for x in range(5))

print(sum(gen))
print(sum(gen))
print(list(gen))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
30
0
[]
```

**Объяснение:** Генератор можно пройти только один раз. После первого `sum()` он исчерпан. Повторный `sum()` возвращает 0 (сумма пустого), `list()` — пустой список.
</details>

---

## Задача 9: `functools.wraps`

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@decorator
def hello():
    """Say hello"""
    pass

print(hello.__name__)
print(hello.__doc__)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
wrapper
None
```

**Объяснение:** Без `@functools.wraps(func)` декоратор заменяет метаданные функции. `__name__` становится `"wrapper"`, `__doc__` — `None`.
</details>

---

## Задача 10: Вложенные генераторы

```python
def gen1():
    yield from range(3)
    yield from range(3, 6)

def gen2():
    yield from gen1()
    yield 99

print(list(gen2()))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
[0, 1, 2, 3, 4, 5, 99]
```

**Объяснение:** `yield from` делегирует генерацию. `gen1()` выдаёт 0-5, затем `gen2()` добавляет 99.
</details>
