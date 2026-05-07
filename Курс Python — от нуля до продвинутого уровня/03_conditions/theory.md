# 📘 Тема 3: Условные конструкции

## Конструкция `if`

```python
age = 18
if age >= 18:
    print("Вы совершеннолетний")
```

## Конструкция `if-else`

```python
age = 15
if age >= 18:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")
```

## Конструкция `if-elif-else`

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

## Операторы сравнения

| Оператор | Описание | Пример |
|----------|----------|--------|
| `==` | Равно | `5 == 5` → True |
| `!=` | Не равно | `5 != 3` → True |
| `>` | Больше | `5 > 3` → True |
| `<` | Меньше | `3 < 5` → True |
| `>=` | Больше или равно | `5 >= 5` → True |
| `<=` | Меньше или равно | `3 <= 5` → True |

## Логические операторы

- `and` — логическое И: `True and False` → `False`
- `or` — логическое ИЛИ: `True or False` → `True`
- `not` — логическое НЕ: `not True` → `False`

```python
age = 25
has_passport = True
if age >= 18 and has_passport:
    print("Можете путешествовать")
```

## Тернарный оператор

```python
status = "взрослый" if age >= 18 else "ребёнок"
```

## Оператор `in`

```python
if name in ["Алиса", "Борис"]:
    print("Найдено")
```

## Falsy-значения

`False`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `None` — всё это `False` в условиях.

## match-case (Python 3.10+)

```python
match command:
    case "start":
        print("Запуск")
    case _:
        print("Неизвестно")
```
