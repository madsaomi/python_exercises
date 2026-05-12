# 01 — Основы и устройство Python: Задачи-ловушки

> ⚠️ **Правила:** Попробуйте предсказать вывод кода **БЕЗ запуска**. Только после этого раскройте ответ.

---

## Задача 1: Коварный `is`

```python
a = 256
b = 256
print(a is b)

c = 257
d = 257
print(c is d)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
True
False
```

**Объяснение:** Python кэширует целые числа от -5 до 256. В интерактивном режиме 257 создаётся заново. В скрипте (.py) результат может быть True/True из-за оптимизации компилятора.
</details>

---

## Задача 2: Изменяемый аргумент по умолчанию

```python
def add_to(element, target=[]):
    target.append(element)
    return target

print(add_to(1))
print(add_to(2))
print(add_to(3))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
[1]
[1, 2]
[1, 2, 3]
```

**Объяснение:** Список `target=[]` создаётся один раз при определении функции. Все вызовы используют один и тот же список.
</details>

---

## Задача 3: Кортеж с одним элементом

```python
a = (1)
b = (1,)
c = 1,
print(type(a), type(b), type(c))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
<class 'int'> <class 'tuple'> <class 'tuple'>
```

**Объяснение:** `(1)` — это число в скобках. Для кортежа из одного элемента нужна запятая: `(1,)`.
</details>

---

## Задача 4: Shallow copy

```python
a = [[1, 2], [3, 4]]
b = a[:]
b.append([5, 6])
b[0].append(99)
print(a)
print(b)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
[[1, 2, 99], [3, 4]]
[[1, 2, 99], [3, 4], [5, 6]]
```

**Объяснение:** `a[:]` — shallow copy. Вложенные списки — те же объекты. `b[0].append(99)` изменил общий вложенный список.
</details>

---

## Задача 5: `or` и `and`

```python
print(0 or "" or [] or "hello" or 42)
print(1 and "world" and [1, 2] and 0 and "end")
print("" or 0 or None or False)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
hello
0
False
```

**Объяснение:** `or` возвращает первое истинное значение, `and` — первое ложное. Python возвращает сам объект, не bool.
</details>

---

## Задача 6: Множественное присваивание

```python
a = b = [1, 2, 3]
b.append(4)
print(a)
print(a is b)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
[1, 2, 3, 4]
True
```

**Объяснение:** `a = b = [...]` — обе переменные ссылаются на один объект.
</details>

---

## Задача 7: Распаковка с `*`

```python
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)

x, *y = [1]
print(x, y)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
1 [2, 3, 4] 5
1 []
```

**Объяснение:** `*b` собирает «лишние» элементы в список. Если элементов не хватает — пустой список.
</details>

---

## Задача 8: Цепочка сравнений

```python
print(1 < 2 < 3)
print(1 < 2 > 0)
print(1 == 1.0 == True)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
True
True
True
```

**Объяснение:** Python поддерживает цепочки сравнений: `a < b < c` это `a < b and b < c`. `bool` — подкласс `int`: `True == 1`, `False == 0`.
</details>

---

## Задача 9: Изменяемость строк

```python
s = "hello"
try:
    s[0] = "H"
    print(s)
except TypeError as e:
    print(f"Ошибка: {e}")

s = "H" + s[1:]
print(s)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
Ошибка: 'str' object does not support item assignment
Hello
```

**Объяснение:** Строки неизменяемы. Нельзя изменить символ по индексу. Нужно создать новую строку.
</details>

---

## Задача 10: Словарь и изменяемые ключи

```python
d = {}
d[True] = "yes"
d[1] = "one"
d[1.0] = "float_one"

print(d)
print(len(d))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
{True: 'float_one'}
1
```

**Объяснение:** `True == 1 == 1.0` и `hash(True) == hash(1) == hash(1.0)`. Для словаря это один и тот же ключ. Значение перезаписывается, но первый ключ (`True`) остаётся.
</details>
