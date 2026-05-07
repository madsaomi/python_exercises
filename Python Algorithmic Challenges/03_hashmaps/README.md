# 📘 Hashmaps — Теория

## Хеш-таблица (Hash Map / Dictionary)

Структура данных, обеспечивающая **O(1)** для вставки, удаления и поиска по ключу.

## Сложность операций

| Операция | Средняя | Худшая |
|----------|---------|--------|
| Поиск | O(1) | O(n) |
| Вставка | O(1) | O(n) |
| Удаление | O(1) | O(n) |

## В Python

```python
# dict
d = {}
d[key] = value
value = d.get(key, default)

# defaultdict
from collections import defaultdict
dd = defaultdict(int)    # по умолчанию 0
dd = defaultdict(list)   # по умолчанию []

# Counter
from collections import Counter
freq = Counter([1, 2, 2, 3, 3, 3])
# Counter({3: 3, 2: 2, 1: 1})

# set — хеш-множество
s = set()
s.add(x)
x in s  # O(1)
```

## Ключевые паттерны

- **Подсчёт частоты** → `Counter` или `defaultdict(int)`
- **Проверка наличия** → `set` или `dict`
- **Маппинг** → `dict` для соответствий
- **Группировка** → `defaultdict(list)`
- **Two Sum паттерн** → запоминаем `complement = target - num`
