# 📘 Binary Search — Теория

## Принцип

Бинарный поиск работает на **отсортированных** данных. На каждом шаге отсекается половина.

**Сложность:** O(log n)

## Базовый шаблон

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## Шаблон: поиск левой границы

```python
def left_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```

## Шаблон: поиск правой границы

```python
def right_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left - 1
```

## Python built-in

```python
import bisect
bisect.bisect_left(arr, x)   # левая граница
bisect.bisect_right(arr, x)  # правая граница
bisect.insort(arr, x)        # вставка с сохранением порядка
```

## Когда применять
- Массив **отсортирован**
- Нужно найти элемент / границу / минимум
- Задача на **поиск ответа** (binary search on answer)
- Ротированный отсортированный массив
