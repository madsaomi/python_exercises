# 📘 Тема 4: Циклы (for, while)

## Цикл `for`

Перебирает элементы последовательности:

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for char in "Python":
    print(char)

for item in [1, 2, 3]:
    print(item)
```

## Функция `range()`

```python
range(5)         # 0, 1, 2, 3, 4
range(2, 8)      # 2, 3, 4, 5, 6, 7
range(0, 10, 2)  # 0, 2, 4, 6, 8
range(10, 0, -1) # 10, 9, 8, ..., 1
```

## Цикл `while`

Выполняется, пока условие истинно:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## `break` — прервать цикл

```python
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4
```

## `continue` — пропустить итерацию

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9
```

## `else` в циклах

Блок `else` выполнится, если цикл **НЕ** был прерван через `break`:

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Цикл завершился без break")
```

## `enumerate()` — индекс + значение

```python
fruits = ["яблоко", "банан", "вишня"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

## `zip()` — параллельный обход

```python
names = ["Алиса", "Борис"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

## Вложенные циклы

```python
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()
```
