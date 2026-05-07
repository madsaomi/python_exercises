# 📘 Arrays — Теория

## Что такое массив?

**Массив (Array)** — упорядоченная коллекция элементов, доступных по индексу.  
В Python массивы реализованы как `list`.

## Основные операции

| Операция | Сложность |
|----------|-----------|
| Доступ по индексу `arr[i]` | O(1) |
| Поиск элемента | O(n) |
| Вставка в конец `append()` | O(1)* |
| Вставка в начало/середину | O(n) |
| Удаление из конца `pop()` | O(1) |
| Удаление из начала/середины | O(n) |
| Срез `arr[i:j]` | O(j-i) |

## Ключевые подходы

### Two Pointers (Два указателя)
```python
left, right = 0, len(arr) - 1
while left < right:
    # логика
    left += 1
    right -= 1
```

### Sliding Window (Скользящее окно)
```python
window_sum = sum(arr[:k])
for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]
```

### Prefix Sum (Префиксные суммы)
```python
prefix = [0] * (len(arr) + 1)
for i in range(len(arr)):
    prefix[i + 1] = prefix[i] + arr[i]
# Сумма arr[l:r] = prefix[r] - prefix[l]
```

## Типичные паттерны

- **Сортировка** → потом Two Pointers
- **Хеш-таблица** → для быстрого поиска O(1)
- **In-place** → модификация без дополнительной памяти
- **Kadane's Algorithm** → максимальная подмассивная сумма
