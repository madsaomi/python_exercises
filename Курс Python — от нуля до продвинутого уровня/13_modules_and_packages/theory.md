# 📘 Тема 13: Модули и пакеты

## Импорт модулей

```python
import math
print(math.sqrt(16))   # 4.0
print(math.pi)          # 3.14159...

from math import sqrt, pi
print(sqrt(16))

from math import *      # импортировать всё (не рекомендуется)

import math as m        # псевдоним
print(m.sqrt(16))
```

## Популярные стандартные модули

| Модуль | Назначение |
|--------|-----------|
| `math` | Математика |
| `random` | Случайные числа |
| `datetime` | Дата и время |
| `os` | Работа с ОС |
| `sys` | Системные параметры |
| `json` | JSON |
| `re` | Регулярные выражения |
| `collections` | Специальные контейнеры |
| `itertools` | Итераторы |
| `functools` | Функциональные инструменты |

## Модуль random

```python
import random

random.random()              # [0.0, 1.0)
random.randint(1, 10)        # [1, 10]
random.choice([1, 2, 3])     # случайный элемент
random.shuffle(lst)          # перемешать на месте
random.sample(lst, 3)        # 3 случайных без повторов
```

## Модуль datetime

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime("%d.%m.%Y %H:%M"))

birthday = datetime(2000, 5, 15)
age = now - birthday

tomorrow = now + timedelta(days=1)
```

## Создание своего модуля

```python
# mymodule.py
def greet(name):
    return f"Привет, {name}!"

PI = 3.14159
```

```python
# main.py
import mymodule
print(mymodule.greet("Алиса"))
```

## Пакеты

```
mypackage/
├── __init__.py
├── math_utils.py
└── string_utils.py
```

```python
from mypackage import math_utils
from mypackage.string_utils import capitalize
```

## `if __name__ == "__main__"`

```python
def main():
    print("Это главный скрипт")

if __name__ == "__main__":
    main()
# Выполняется только при прямом запуске файла,
# НЕ при импорте.
```
