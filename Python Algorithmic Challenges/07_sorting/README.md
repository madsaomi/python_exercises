# 📘 Sorting — Теория

## Алгоритмы сортировки

| Алгоритм | Время (средн.) | Время (худш.) | Память | Стабильная? |
|----------|---------------|---------------|--------|------------|
| Bubble Sort | O(n²) | O(n²) | O(1) | ✅ |
| Selection Sort | O(n²) | O(n²) | O(1) | ❌ |
| Insertion Sort | O(n²) | O(n²) | O(1) | ✅ |
| Merge Sort | O(n log n) | O(n log n) | O(n) | ✅ |
| Quick Sort | O(n log n) | O(n²) | O(log n) | ❌ |
| Heap Sort | O(n log n) | O(n log n) | O(1) | ❌ |
| Counting Sort | O(n + k) | O(n + k) | O(k) | ✅ |

## Merge Sort

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

## Quick Sort

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)
```

## Python built-in

```python
sorted(arr)                    # новый список
arr.sort()                     # in-place
sorted(arr, key=lambda x: -x)  # кастомный ключ
sorted(arr, reverse=True)      # по убыванию
```

## Паттерны
- **Сортировка + Two Pointers** → эффективный поиск пар
- **Сортировка + бинарный поиск** → быстрый поиск
- **Кастомная сортировка** → key-функция
- **Counting Sort** → когда диапазон значений ограничен
