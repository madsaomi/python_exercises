# 04 — Структуры данных: глубокое погружение — Теоретические вопросы

---

## Вопрос 1: Как устроен словарь (dict) внутри?

<details>
<summary>💡 Ответ</summary>

Python `dict` — это **хеш-таблица**.

1. При добавлении ключа вычисляется `hash(key)`
2. По хешу определяется позиция (слот) в массиве
3. При коллизии (два ключа → один слот) используется **open addressing** (зондирование)
4. При заполнении ~2/3 — массив увеличивается (rehashing)

**Следствия:**
- Средняя сложность `O(1)` для get/set/delete
- Порядок вставки **сохраняется** (с Python 3.7+)
- Ключи должны быть **хешируемыми** (неизменяемыми)
</details>

---

## Вопрос 2: Почему ключи словаря должны быть хешируемыми?

<details>
<summary>💡 Ответ</summary>

Словарь использует хеш для определения позиции ключа. Если объект **изменяемый**, его хеш может измениться после добавления, и ключ станет «потерянным».

```python
# ✅ Хешируемые — можно использовать как ключи
d = {42: "int", "hello": "str", (1, 2): "tuple", True: "bool"}

# ❌ НЕ хешируемые — нельзя
# d = {[1, 2]: "list"}      # TypeError: unhashable type: 'list'
# d = {{1: 2}: "dict"}      # TypeError: unhashable type: 'dict'
# d = {{1, 2}: "set"}       # TypeError: unhashable type: 'set'
```

**Правило:** Все неизменяемые встроенные типы — хешируемые. Все изменяемые — нет.
</details>

---

## Вопрос 3: Какова сложность основных операций?

<details>
<summary>💡 Ответ</summary>

| Операция | `list` | `dict` | `set` | `deque` |
|----------|--------|--------|-------|---------|
| Доступ по индексу | O(1) | — | — | O(n) |
| Поиск `in` | O(n) | O(1) | O(1) | O(n) |
| Добавление в конец | O(1)* | O(1)* | O(1)* | O(1) |
| Добавление в начало | O(n) | — | — | O(1) |
| Удаление с конца | O(1) | — | — | O(1) |
| Удаление из середины | O(n) | O(1) | O(1) | O(n) |
| Сортировка | O(n log n) | — | — | — |

`*` — амортизированная сложность
</details>

---

## Вопрос 4: Что такое `defaultdict`?

<details>
<summary>💡 Ответ</summary>

`defaultdict` автоматически создаёт значение по умолчанию для несуществующих ключей:

```python
from collections import defaultdict

# Группировка
groups = defaultdict(list)
for word in ["apple", "banana", "avocado", "blueberry"]:
    groups[word[0]].append(word)
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry']}

# Подсчёт
counts = defaultdict(int)
for char in "hello":
    counts[char] += 1
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

В отличие от обычного `dict`, не бросает `KeyError`.
</details>

---

## Вопрос 5: Что такое `Counter` и как его использовать?

<details>
<summary>💡 Ответ</summary>

`Counter` — специализированный словарь для подсчёта:

```python
from collections import Counter

c = Counter("abracadabra")
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

print(c.most_common(2))     # [('a', 5), ('b', 2)]
print(c['a'])                # 5
print(c['z'])                # 0 (не KeyError!)

# Арифметика
c2 = Counter("abc")
print(c + c2)  # объединение
print(c - c2)  # вычитание
```
</details>

---

## Вопрос 6: Когда использовать `deque` вместо `list`?

<details>
<summary>💡 Ответ</summary>

`collections.deque` — двусторонняя очередь с O(1) для добавления/удаления с обоих концов:

```python
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)    # O(1) — у list было бы O(n)
d.popleft()        # O(1) — у list.pop(0) — O(n)
d.rotate(1)        # [3, 1, 2] — циклический сдвиг
d.rotate(-1)       # [1, 2, 3]

# Ограниченная длина
recent = deque(maxlen=3)
recent.extend([1, 2, 3, 4, 5])
print(recent)  # deque([3, 4, 5]) — старые элементы вытесняются
```

**Используйте deque** для очередей, BFS, скользящего окна.
</details>

---

## Вопрос 7: В чём разница между `list.sort()` и `sorted()`?

<details>
<summary>💡 Ответ</summary>

| | `list.sort()` | `sorted()` |
|--|---------------|------------|
| Возвращает | `None` (изменяет на месте) | Новый список |
| Работает с | Только `list` | Любой iterable |
| Память | O(1) дополнительной | O(n) — создаёт новый список |

```python
nums = [3, 1, 2]
result = nums.sort()   # None! nums изменён
print(nums)            # [1, 2, 3]
print(result)          # None

nums = [3, 1, 2]
result = sorted(nums)  # новый список
print(nums)            # [3, 1, 2] — не изменён
print(result)          # [1, 2, 3]
```
</details>

---

## Вопрос 8: Что такое `namedtuple`?

<details>
<summary>💡 Ответ</summary>

`namedtuple` — кортеж с именованными полями. Неизменяемый, легковесный:

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)

print(p.x, p.y)     # 3 4 (доступ по имени)
print(p[0], p[1])   # 3 4 (доступ по индексу)
x, y = p             # распаковка

# Нельзя изменить: p.x = 5 → AttributeError
```

Современная альтернатива — `dataclasses` или `typing.NamedTuple`.
</details>

---

## Вопрос 9: Чем `set` отличается от `frozenset`?

<details>
<summary>💡 Ответ</summary>

| | `set` | `frozenset` |
|--|-------|-------------|
| Изменяемый | Да | Нет |
| Хешируемый | Нет | Да |
| Ключ словаря | Нельзя | Можно |
| Методы | add, remove, discard... | Только чтение |

```python
s = {1, 2, 3}
fs = frozenset([1, 2, 3])

s.add(4)     # OK
# fs.add(4)  # AttributeError

d = {fs: "value"}  # OK — frozenset хешируемый
# d = {s: "value"} # TypeError — set не хешируемый
```
</details>

---

## Вопрос 10: Что такое `OrderedDict` и нужен ли он в Python 3.7+?

<details>
<summary>💡 Ответ</summary>

`OrderedDict` — словарь, который запоминает порядок вставки. В Python 3.7+ обычный `dict` тоже сохраняет порядок.

**Когда `OrderedDict` всё ещё нужен:**
- `move_to_end(key)` — переместить ключ в конец/начало
- Сравнение с учётом порядка: `OrderedDict` считает порядок при `==`

```python
from collections import OrderedDict

d1 = OrderedDict([('a', 1), ('b', 2)])
d2 = OrderedDict([('b', 2), ('a', 1)])
print(d1 == d2)  # False — разный порядок

d3 = {'a': 1, 'b': 2}
d4 = {'b': 2, 'a': 1}
print(d3 == d4)  # True — обычный dict не сравнивает порядок
```
</details>

---

## Вопрос 11: Как эффективно проверить наличие элемента?

<details>
<summary>💡 Ответ</summary>

```python
items = [1, 2, 3, 4, 5]

# ❌ Плохо — O(n) для каждой проверки
if 3 in items:
    pass

# ✅ Хорошо — O(1) для каждой проверки
items_set = set(items)
if 3 in items_set:
    pass
```

**Правило:** Если проверка `in` выполняется многократно — преобразуйте в `set`.
</details>

---

## Вопрос 12: Как объединить два словаря?

<details>
<summary>💡 Ответ</summary>

```python
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

# Python 3.9+
merged = a | b         # {'x': 1, 'y': 3, 'z': 4}

# Python 3.5+
merged = {**a, **b}    # {'x': 1, 'y': 3, 'z': 4}

# Любая версия
merged = a.copy()
merged.update(b)
```

При конфликте ключей побеждает **правый** словарь.
</details>

---

## Вопрос 13: Что такое `heapq`?

<details>
<summary>💡 Ответ</summary>

`heapq` — модуль для работы с **кучей** (min-heap). Элементы хранятся в списке:

```python
import heapq

nums = [5, 3, 8, 1, 2]
heapq.heapify(nums)        # [1, 2, 8, 5, 3]

heapq.heappush(nums, 0)    # добавить
smallest = heapq.heappop(nums)  # извлечь минимум → 0

# Top-3 наибольших/наименьших
print(heapq.nlargest(3, [5, 3, 8, 1, 2]))   # [8, 5, 3]
print(heapq.nsmallest(3, [5, 3, 8, 1, 2]))  # [1, 2, 3]
```
</details>

---

## Вопрос 14: Как удалить дубликаты из списка с сохранением порядка?

<details>
<summary>💡 Ответ</summary>

```python
# Способ 1: dict.fromkeys (Python 3.7+)
items = [3, 1, 2, 1, 3, 4, 2]
unique = list(dict.fromkeys(items))  # [3, 1, 2, 4]

# Способ 2: set + цикл
seen = set()
unique = []
for item in items:
    if item not in seen:
        seen.add(item)
        unique.append(item)

# ❌ set(items) — НЕ сохраняет порядок (до 3.7)
```
</details>

---

## Вопрос 15: В чём разница между `list` и `tuple`? Когда что использовать?

<details>
<summary>💡 Ответ</summary>

| | `list` | `tuple` |
|--|--------|---------|
| Изменяемый | Да | Нет |
| Хешируемый | Нет | Да (если элементы хешируемые) |
| Создание | `[1, 2]` | `(1, 2)` |
| Память | Больше | Меньше (~16 байт разницы) |
| Скорость | Чуть медленнее | Чуть быстрее |

**Когда tuple:** Координаты, ключи словаря, неизменяемые записи, возврат нескольких значений из функции.  
**Когда list:** Коллекция, которую нужно изменять.
</details>
