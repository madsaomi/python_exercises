# 📘 Strings — Теория

## Строки как массивы символов

В задачах на строки ключевое — что строка в Python **неизменяема**.  
Для модификации часто преобразуют в список: `list(s)`.

## Основные операции

| Операция | Сложность |
|----------|-----------|
| Доступ по индексу `s[i]` | O(1) |
| Срез `s[i:j]` | O(j-i) |
| Конкатенация `s1 + s2` | O(n+m) |
| Поиск подстроки `s.find(t)` | O(n*m) |
| `in` оператор | O(n) |
| `join` | O(n) |

## Ключевые подходы

### Two Pointers
```python
def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
```

### Sliding Window
Для задач на подстроки с условием (анаграммы, без повторов).

### Хеш-таблица (Counter)
```python
from collections import Counter
freq = Counter(s)
```

### ASCII / ord()
```python
ord('a')  # 97
chr(97)   # 'a'
# Массив частот без dict:
count = [0] * 26
count[ord(c) - ord('a')] += 1
```

## Типичные паттерны
- **Палиндром** → Two Pointers
- **Анаграммы** → Counter / сортировка
- **Подстрока без повторов** → Sliding Window + HashSet
- **Реверс** → Two Pointers или срез `[::-1]`
