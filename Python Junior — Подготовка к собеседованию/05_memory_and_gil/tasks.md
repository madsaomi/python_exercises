# 05 — Память, GIL и многопоточность: Задачи-ловушки

> ⚠️ Попробуйте предсказать вывод **БЕЗ запуска**.

---

## Задача 1: Счётчик ссылок

```python
import sys

a = [1, 2, 3]
b = a
c = [a, a]

print(sys.getrefcount(a) - 1)  # -1 т.к. getrefcount добавляет 1
del b
print(sys.getrefcount(a) - 1)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
4
3
```

**Объяснение:** Ссылки: `a` (1), `b` (1), `c[0]` (1), `c[1]` (1) = 4. После `del b` → 3. (`getrefcount` сам добавляет +1 при передаче аргумента, поэтому мы вычитаем 1).
</details>

---

## Задача 2: `id()` и повторное использование

```python
a = 1000
b = 1000
print(a is b)

del a
del b

c = 1000
print(id(c))  # может совпасть с id бывшего a!
```

<details>
<summary>🔍 Что выведет код?</summary>

```
True или False  # зависит от контекста (скрипт vs REPL)
<какой-то id>
```

**Объяснение:** В скрипте (.py файл) компилятор может оптимизировать и создать один объект. В REPL — два разных. После `del` Python может переиспользовать тот же адрес памяти для нового объекта.
</details>

---

## Задача 3: Размер объектов

```python
import sys

print(sys.getsizeof(1))
print(sys.getsizeof(""))
print(sys.getsizeof([]))
print(sys.getsizeof(()))
print(sys.getsizeof({}))
print(sys.getsizeof(set()))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
28
49
56
40
64
216
```

**Объяснение:** (Значения приблизительные, зависят от платформы и версии Python.) Пустой `set` занимает больше всех из-за хеш-таблицы. Кортеж легче списка. Словарь тоже содержит хеш-таблицу.
</details>

---

## Задача 4: Циклическая ссылка

```python
import gc

class Node:
    def __init__(self, name):
        self.name = name
        self.ref = None
    def __del__(self):
        print(f"Deleting {self.name}")

a = Node("A")
b = Node("B")
a.ref = b
b.ref = a

del a
del b

print("Before gc.collect")
gc.collect()
print("After gc.collect")
```

<details>
<summary>🔍 Что выведет код?</summary>

```
Before gc.collect
Deleting A
Deleting B
After gc.collect
```

**Объяснение:** `del a, b` не удаляет объекты (циклическая ссылка). `gc.collect()` находит цикл и удаляет оба. Порядок удаления может варьироваться.
</details>

---

## Задача 5: `__slots__` и память

```python
import sys

class Regular:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Slotted:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

r = Regular(1, 2)
s = Slotted(1, 2)

print(sys.getsizeof(r))
print(sys.getsizeof(s))
print(hasattr(r, '__dict__'))
print(hasattr(s, '__dict__'))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
48
48   # или меньше — зависит от реализации
True
False
```

**Объяснение:** `getsizeof` не учитывает `__dict__` (он считается отдельным объектом). Реальная экономия видна при массовом создании объектов. `Slotted` не имеет `__dict__`.
</details>

---

## Задача 6: Изменяемость и id

```python
a = (1, 2, 3)
print(id(a))
a += (4,)
print(id(a))
print(a)

b = [1, 2, 3]
print(id(b))
b += [4]
print(id(b))
print(b)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
<id1>
<id2>  # ДРУГОЙ id — создан новый кортеж
(1, 2, 3, 4)
<id3>
<id3>  # ТОТ ЖЕ id — список изменён на месте
[1, 2, 3, 4]
```

**Объяснение:** `+=` для кортежа (неизменяемый) создаёт новый объект. Для списка (изменяемый) — изменяет на месте (`extend`).
</details>

---

## Задача 7: `intern` строк

```python
import sys

a = "hello"
b = "hello"
print(a is b)

c = "hello world"
d = "hello world"
print(c is d)

e = sys.intern("hello world")
f = sys.intern("hello world")
print(e is f)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
True
False  # (может быть True в скрипте)
True
```

**Объяснение:** Короткие строки без спецсимволов интернируются автоматически. `sys.intern()` принудительно интернирует любую строку.
</details>

---

## Задача 8: Утечка памяти через замыкание

```python
def create_functions():
    funcs = []
    big_data = [0] * 1000000  # ~8MB

    for i in range(5):
        def func(x, data=big_data):
            return x + len(data)
        funcs.append(func)

    return funcs

# big_data не будет удалён, пока живы функции!
functions = create_functions()
print(functions[0](1))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
1000001
```

**Объяснение:** Каждая функция замыкает `big_data` через аргумент по умолчанию. Даже после выхода из `create_functions`, `big_data` остаётся в памяти, пока жива хоть одна функция.
</details>

---

## Задача 9: `is` для None, True, False

```python
a = None
b = None
print(a is b)

c = True
d = True
print(c is d)

e = False
f = False
print(e is f)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
True
True
True
```

**Объяснение:** `None`, `True`, `False` — синглтоны в Python. Всегда один и тот же объект. Поэтому `is` **всегда** работает для них.
</details>

---

## Задача 10: Копирование и память

```python
import copy

original = {"a": [1, 2, 3], "b": [4, 5, 6]}
shallow = copy.copy(original)
deep = copy.deepcopy(original)

print(original["a"] is shallow["a"])
print(original["a"] is deep["a"])

shallow["a"].append(99)
print(original["a"])
print(deep["a"])
```

<details>
<summary>🔍 Что выведет код?</summary>

```
True
False
[1, 2, 3, 99]
[1, 2, 3]
```

**Объяснение:** Shallow copy разделяет вложенные объекты с оригиналом. Deep copy создаёт полностью независимую копию.
</details>
