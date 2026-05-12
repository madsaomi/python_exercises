"""
03 — ООП под капотом: Практические упражнения

Напишите решения прямо в этом файле.
Запустите для проверки: python exercises.py
"""
from abc import ABC, abstractmethod


# ============================================================
# Упражнение 1: Singleton через __new__
# ============================================================
# Реализуйте паттерн Singleton: класс, у которого может быть
# только один экземпляр. Повторные вызовы возвращают тот же объект.
# __init__ НЕ должен сбрасывать данные при повторном создании.
#
# Пример:
#   a = SingletonDB("postgres://...")
#   b = SingletonDB("mysql://...")
#   print(a is b)  → True
#   print(a.url)   → "postgres://..."  (первое значение)

class SingletonDB:
    # Ваш код здесь
    pass


# ============================================================
# Упражнение 2: Стек с магическими методами
# ============================================================
# Реализуйте класс Stack с поддержкой:
# - push(item) / pop() — добавление/удаление
# - len(stack) — количество элементов (__len__)
# - str(stack) — строковое представление (__str__)
# - repr(stack) — для разработчика (__repr__)
# - stack1 + stack2 — конкатенация (__add__)
# - bool(stack) — False если пустой (__bool__)
# - item in stack — проверка наличия (__contains__)
#
# Пример:
#   s = Stack()
#   s.push(1); s.push(2)
#   print(len(s))      → 2
#   print(s)            → "Stack: [1, 2]"
#   print(bool(Stack()))→ False

class Stack:
    # Ваш код здесь
    pass


# ============================================================
# Упражнение 3: Абстрактный класс Shape
# ============================================================
# Создайте абстрактный класс Shape с методами area() и perimeter().
# Реализуйте наследников: Rectangle и Circle.
#
# Пример:
#   r = Rectangle(3, 4)
#   print(r.area())      → 12
#   print(r.perimeter())  → 14
#   c = Circle(5)
#   print(c.area())      → 78.54 (примерно)

class Shape(ABC):
    # Ваш код здесь
    pass


class Rectangle(Shape):
    # Ваш код здесь
    pass


class Circle(Shape):
    # Ваш код здесь
    pass


# ============================================================
# Упражнение 4: @property с валидацией
# ============================================================
# Создайте класс BankAccount с:
# - balance (property) — не может быть отрицательным
# - deposit(amount) — пополнение (amount > 0)
# - withdraw(amount) — снятие (если хватает средств)
#
# Пример:
#   acc = BankAccount(100)
#   acc.deposit(50)
#   print(acc.balance)    → 150
#   acc.withdraw(30)
#   print(acc.balance)    → 120
#   acc.withdraw(200)     → ValueError

class BankAccount:
    # Ваш код здесь
    pass


# ============================================================
# Упражнение 5: Миксин — сериализация
# ============================================================
# Создайте JsonMixin, который добавляет:
# - to_json() — сериализация в JSON-строку
# - from_json(json_str) — десериализация (classmethod)
#
# Пример:
#   class User(JsonMixin):
#       def __init__(self, name, age):
#           self.name = name
#           self.age = age
#
#   u = User("Alice", 30)
#   json_str = u.to_json()          → '{"name": "Alice", "age": 30}'
#   u2 = User.from_json(json_str)
#   print(u2.name)                  → "Alice"

class JsonMixin:
    # Ваш код здесь
    pass


# ============================================================
# Тесты
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("Тестирование упражнений 03_oop_under_the_hood")
    print("=" * 50)

    # Тест 1
    print("\n--- Упражнение 1: SingletonDB ---")
    a = SingletonDB("postgres://localhost")
    b = SingletonDB("mysql://localhost")
    assert a is b, "Должен быть один экземпляр"
    assert a.url == "postgres://localhost", f"URL должен быть первым: {a.url}"
    print("✅ Все тесты пройдены!")

    # Тест 4
    print("\n--- Упражнение 4: BankAccount ---")
    acc = BankAccount(100)
    acc.deposit(50)
    assert acc.balance == 150
    acc.withdraw(30)
    assert acc.balance == 120
    try:
        acc.withdraw(200)
        assert False, "Должен бросить ValueError"
    except ValueError:
        pass
    print("✅ Все тесты пройдены!")

    print("\n" + "=" * 50)
    print("🎉 Все упражнения выполнены верно!")
    print("=" * 50)
