# 04 — Структуры данных: Задачи-ловушки

> ⚠️ Попробуйте предсказать вывод **БЕЗ запуска**.

---

## Задача 1: dict и порядок

```python
d = {}
d['b'] = 2
d['a'] = 1
d['c'] = 3
print(list(d.keys()))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
['b', 'a', 'c']
```

**Объяснение:** С Python 3.7+ словари сохраняют порядок вставки.
</details>

---

## Задача 2: set и порядок

```python
s = {3, 1, 4, 1, 5, 9, 2, 6}
print(s)
print(len(s))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
{1, 2, 3, 4, 5, 6, 9}  # порядок может отличаться!
7
```

**Объяснение:** Set удаляет дубликаты (1 встречается дважды). Порядок вывода **не гарантирован** (зависит от хеширования).
</details>

---

## Задача 3: Словарь внутри списка

```python
d = {"a": 1}
lst = [d, d, d]
lst[0]["b"] = 2

print(lst)
print(lst[0] is lst[1])
```

<details>
<summary>🔍 Что выведет код?</summary>

```
[{'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}]
True
```

**Объяснение:** Все три элемента — ссылки на один и тот же словарь. Изменение через любой из них затрагивает все.
</details>

---

## Задача 4: `defaultdict` vs `dict`

```python
from collections import defaultdict

d = defaultdict(int)
print(d["missing"])
print(dict(d))

d2 = {}
print(d2.get("missing", 0))
print(d2)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
0
{'missing': 0}
0
{}
```

**Объяснение:** `defaultdict[key]` **создаёт** ключ с default-значением. `dict.get()` **не создаёт** ключ — только возвращает default.
</details>

---

## Задача 5: Умножение списка

```python
a = [[0]] * 3
a[0].append(1)
print(a)

b = [[0] for _ in range(3)]
b[0].append(1)
print(b)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
[[0, 1], [0, 1], [0, 1]]
[[0, 1], [0], [0]]
```

**Объяснение:** `[[0]] * 3` создаёт три ссылки на **один** список. Comprehension создаёт три **разных** списка.
</details>

---

## Задача 6: Counter арифметика

```python
from collections import Counter

a = Counter("aabbc")
b = Counter("abc")

print(a - b)
print(a + b)
print(a & b)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
Counter({'a': 1, 'b': 1})
Counter({'a': 3, 'b': 3, 'c': 2})
Counter({'a': 1, 'b': 1, 'c': 1})
```

**Объяснение:** `-` вычитает, `+` складывает, `&` — минимум (пересечение).
</details>

---

## Задача 7: Сортировка словаря

```python
d = {"banana": 3, "apple": 1, "cherry": 2}

by_key = dict(sorted(d.items()))
by_val = dict(sorted(d.items(), key=lambda x: x[1]))

print(by_key)
print(by_val)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
{'apple': 1, 'banana': 3, 'cherry': 2}
{'apple': 1, 'cherry': 2, 'banana': 3}
```

**Объяснение:** `sorted(d.items())` сортирует по ключу (первому элементу кортежа). `key=lambda x: x[1]` сортирует по значению.
</details>

---

## Задача 8: `tuple` как ключ

```python
d = {}
d[(1, 2)] = "point"
d[(1, 2)] = "updated"

print(d)
print(len(d))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
{(1, 2): 'updated'}
1
```

**Объяснение:** Кортежи хешируемы, поэтому могут быть ключами. `(1, 2)` — один и тот же ключ, значение перезаписано.
</details>

---

## Задача 9: `dict.setdefault()`

```python
d = {"a": 1}
result1 = d.setdefault("a", 99)
result2 = d.setdefault("b", 99)

print(result1)
print(result2)
print(d)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
1
99
{'a': 1, 'b': 99}
```

**Объяснение:** `setdefault` возвращает существующее значение, если ключ есть. Если нет — устанавливает default и возвращает его.
</details>

---

## Задача 10: `zip` и `dict`

```python
keys = ["a", "b", "c"]
values = [1, 2]

d = dict(zip(keys, values))
print(d)
print(len(d))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
{'a': 1, 'b': 2}
2
```

**Объяснение:** `zip` останавливается по самому короткому итерируемому. Ключ "c" не получает значения и не попадает в словарь.
</details>
