# 📘 Тема 5: Списки

## Создание списков

```python
nums = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]
empty = []
from_range = list(range(10))
```

## Индексация и срезы

```python
lst = [10, 20, 30, 40, 50]
lst[0]      # 10
lst[-1]     # 50
lst[1:3]    # [20, 30]
lst[::-1]   # [50, 40, 30, 20, 10]
```

## Методы списков

```python
lst = [3, 1, 4]
lst.append(5)       # [3, 1, 4, 5]
lst.insert(0, 0)    # [0, 3, 1, 4, 5]
lst.extend([6, 7])  # [0, 3, 1, 4, 5, 6, 7]
lst.remove(3)       # удалить первое вхождение 3
lst.pop()           # удалить последний элемент
lst.pop(0)          # удалить по индексу
lst.sort()          # сортировка
lst.reverse()       # реверс
lst.index(4)        # индекс элемента
lst.count(1)        # количество вхождений
lst.clear()         # очистить
lst2 = lst.copy()   # копия
```

## Полезные функции

```python
nums = [5, 2, 8, 1, 9]
len(nums)     # 5
sum(nums)     # 25
min(nums)     # 1
max(nums)     # 9
sorted(nums)  # [1, 2, 5, 8, 9] — новый список
```

## Вложенные списки (матрицы)

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[0][1]  # 2
```

## Распаковка списков

```python
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4, 5]  # first=1, rest=[2,3,4,5]
```
