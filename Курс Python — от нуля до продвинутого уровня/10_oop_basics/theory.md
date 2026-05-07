# 📘 Тема 10: Основы ООП

## Классы и объекты

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name      # атрибут экземпляра
        self.breed = breed

    def bark(self):
        return f"{self.name} говорит: Гав!"

dog = Dog("Рекс", "Овчарка")
print(dog.bark())
```

## `__init__` — конструктор

Вызывается при создании объекта. `self` — ссылка на экземпляр.

## Атрибуты класса vs экземпляра

```python
class Cat:
    species = "Кошка"        # атрибут класса (общий для всех)

    def __init__(self, name):
        self.name = name     # атрибут экземпляра

cat1 = Cat("Мурка")
cat2 = Cat("Барсик")
print(Cat.species)    # "Кошка"
```

## Методы

```python
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):           # обычный метод
        result = a + b
        self.history.append(result)
        return result

    @staticmethod
    def info():                     # статический метод
        return "Простой калькулятор"

    @classmethod
    def from_string(cls, s):        # метод класса
        return cls()
```

## `__str__` и `__repr__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):    # для пользователя (print)
        return f"({self.x}, {self.y})"

    def __repr__(self):   # для разработчика
        return f"Point({self.x}, {self.y})"
```

## Инкапсуляция

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance       # "приватный" (соглашение)
        self.__secret = "hidden"      # name mangling

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value

acc = BankAccount(1000)
print(acc.balance)   # 1000
acc.balance = 500    # через setter
```

## Магические методы

| Метод | Назначение |
|-------|-----------|
| `__init__` | Конструктор |
| `__str__` | Строковое представление |
| `__len__` | len(obj) |
| `__eq__` | obj1 == obj2 |
| `__lt__` | obj1 < obj2 |
| `__add__` | obj1 + obj2 |
| `__getitem__` | obj[key] |
| `__contains__` | item in obj |
