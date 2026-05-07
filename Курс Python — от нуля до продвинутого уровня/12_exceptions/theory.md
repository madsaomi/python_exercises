# 📘 Тема 12: Обработка исключений

## try-except

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Деление на ноль!")
```

## try-except-else-finally

```python
try:
    num = int(input("Число: "))
except ValueError:
    print("Это не число!")
else:
    print(f"Вы ввели: {num}")  # если ошибки не было
finally:
    print("Всегда выполняется")  # всегда
```

## Несколько исключений

```python
try:
    # опасный код
    pass
except (ValueError, TypeError) as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")
```

## Основные исключения

| Исключение | Когда возникает |
|-----------|----------------|
| `ValueError` | Неверное значение |
| `TypeError` | Неверный тип |
| `IndexError` | Индекс вне диапазона |
| `KeyError` | Ключ не найден |
| `FileNotFoundError` | Файл не найден |
| `ZeroDivisionError` | Деление на ноль |
| `AttributeError` | Атрибут не найден |
| `ImportError` | Ошибка импорта |

## raise — вызов исключения

```python
def set_age(age):
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным")
    return age
```

## Собственные исключения

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Недостаточно средств: баланс {balance}, запрошено {amount}"
        )

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
```

## Цепочки исключений

```python
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Ошибка парсинга") from e
```

## LBYL vs EAFP

```python
# LBYL (Look Before You Leap) — проверка заранее
if key in dictionary:
    value = dictionary[key]

# EAFP (Easier to Ask Forgiveness) — Pythonic способ
try:
    value = dictionary[key]
except KeyError:
    value = default
```
