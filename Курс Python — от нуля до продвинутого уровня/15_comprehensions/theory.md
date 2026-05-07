# 📘 Тема 15: Comprehensions

## List Comprehension

```python
# Базовый синтаксис:
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# С условием:
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# С if-else:
labels = ["чёт" if x % 2 == 0 else "нечёт" for x in range(5)]
# ["чёт", "нечёт", "чёт", "нечёт", "чёт"]

# Вложенный:
matrix = [[i*3+j for j in range(3)] for i in range(3)]
# [[0,1,2], [3,4,5], [6,7,8]]

# Развёртка матрицы:
flat = [x for row in matrix for x in row]
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
```

## Dict Comprehension

```python
squares = {x: x**2 for x in range(6)}
# {0:0, 1:1, 2:4, 3:9, 4:16, 5:25}

# Инвертировать словарь:
d = {"a": 1, "b": 2}
inv = {v: k for k, v in d.items()}
# {1: "a", 2: "b"}

# Фильтрация:
scores = {"Алиса": 90, "Борис": 60, "Виктор": 85}
good = {k: v for k, v in scores.items() if v >= 80}
```

## Set Comprehension

```python
unique_lengths = {len(word) for word in ["кот", "собака", "мяч"]}
# {3, 6}
```

## Generator Expression

```python
total = sum(x**2 for x in range(1000000))  # не создаёт список!
```

## Когда НЕ использовать

- Сложная логика → обычный цикл
- Побочные эффекты (print, append) → обычный цикл
- Более 2 уровней вложенности → обычный цикл
