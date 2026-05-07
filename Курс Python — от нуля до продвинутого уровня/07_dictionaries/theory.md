# 📘 Тема 7: Словари

## Создание словарей

```python
person = {"name": "Алиса", "age": 25, "city": "Москва"}
empty = {}
from_pairs = dict([("a", 1), ("b", 2)])
from_keys = dict.fromkeys(["x", "y", "z"], 0)
```

## Доступ к данным

```python
d = {"name": "Алиса", "age": 25}
d["name"]           # "Алиса"
d.get("name")       # "Алиса"
d.get("phone", "?") # "?" — значение по умолчанию
# d["phone"]        # ❌ KeyError
```

## Основные методы

```python
d = {"a": 1, "b": 2}
d["c"] = 3                # добавить/обновить
d.update({"d": 4, "e": 5})
d.pop("a")                # удалить и вернуть
del d["b"]                # удалить
d.keys()                  # ключи
d.values()                # значения
d.items()                 # пары (ключ, значение)
"c" in d                  # True — проверка ключа
d.setdefault("f", 6)      # если нет — добавить
```

## Перебор словаря

```python
d = {"name": "Алиса", "age": 25}

for key in d:
    print(key, d[key])

for key, value in d.items():
    print(f"{key}: {value}")
```

## Вложенные словари

```python
students = {
    "Алиса": {"age": 20, "grade": "A"},
    "Борис": {"age": 22, "grade": "B"},
}
students["Алиса"]["grade"]  # "A"
```

## defaultdict и Counter

```python
from collections import defaultdict, Counter

dd = defaultdict(list)
dd["fruits"].append("apple")  # не вызовет KeyError

words = ["a", "b", "a", "c", "b", "a"]
counter = Counter(words)  # Counter({'a': 3, 'b': 2, 'c': 1})
```
