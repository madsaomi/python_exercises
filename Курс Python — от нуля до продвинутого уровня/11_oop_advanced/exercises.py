"""
============================================================
  ТЕМА 11: Продвинутое ООП — Упражнения
============================================================
  Каждое задание содержит подробное описание, примеры
  ожидаемого результата и подсказки.
============================================================
"""

# ============================================================
# Задание 1: Наследование — Фигуры
# ============================================================
# Создайте базовый класс Shape с методами area() и perimeter(),
# которые вызывают NotImplementedError (или используйте ABC).
# Наследники: Circle(radius), Rectangle(width, height).
# Каждый реализует свои area() и perimeter().
#
# Ожидаемый результат:
#   c = Circle(5)
#   print(c.area())       → 78.54  (π * r²)
#   print(c.perimeter())  → 31.42  (2 * π * r)
#
#   r = Rectangle(4, 6)
#   print(r.area())       → 24
#   print(r.perimeter())  → 20
#
#   shapes = [Circle(3), Rectangle(2, 5), Circle(1)]
#   total = sum(s.area() for s in shapes)
#   print(f"Общая площадь: {total:.2f}")
#
# Подсказка:
#   from abc import ABC, abstractmethod
#   class Shape(ABC):
#       @abstractmethod
#       def area(self): ...

from abc import ABC, abstractmethod
import math

# Ваш код здесь:


# ============================================================
# Задание 2: Иерархия сотрудников
# ============================================================
# Базовый класс Employee(name, salary).
# Наследники:
#   Manager(name, salary, bonus) → total_pay = salary + bonus
#   Developer(name, salary, language) → total_pay = salary * 1.2
# Метод __str__ у каждого. Метод total_pay() у каждого свой.
#
# Ожидаемый результат:
#   m = Manager("Анна", 100000, 20000)
#   d = Developer("Борис", 90000, "Python")
#   print(m)             → "Manager: Анна, зарплата: 120000"
#   print(d)             → "Developer: Борис (Python), зарплата: 108000"
#   print(m.total_pay()) → 120000
#   print(d.total_pay()) → 108000.0
#
# Подсказка: super().__init__(name, salary)

# Ваш код здесь:


# ============================================================
# Задание 3: Множественное наследование — Миксины
# ============================================================
# Создайте миксины:
#   JsonMixin — методы to_json() и from_json(cls, json_str)
#   DisplayMixin — метод display() для красивого вывода
# Класс User(name, email) наследует оба миксина.
#
# Ожидаемый результат:
#   u = User("Алиса", "alice@mail.ru")
#   json_str = u.to_json()
#   print(json_str)  → '{"name": "Алиса", "email": "alice@mail.ru"}'
#
#   u2 = User.from_json('{"name": "Борис", "email": "bob@mail.ru"}')
#   u2.display()
#   # === User ===
#   # name: Борис
#   # email: bob@mail.ru
#
# Подсказка:
#   import json
#   def to_json(self): return json.dumps(self.__dict__,
#                                         ensure_ascii=False)

import json

# Ваш код здесь:


# ============================================================
# Задание 4: Полиморфизм — Зоопарк
# ============================================================
# Базовый класс Animal(name). Подклассы: Dog, Cat, Bird.
# Каждый реализует speak() и move().
# Создайте список животных и вызовите методы полиморфно.
#
# Ожидаемый результат:
#   zoo = [Dog("Шарик"), Cat("Мурка"), Bird("Кеша")]
#   for animal in zoo:
#       print(f"{animal.name}: {animal.speak()}, {animal.move()}")
#   # Шарик: Гав!, бегает
#   # Мурка: Мяу!, крадётся
#   # Кеша: Чирик!, летает
#
# Подсказка: каждый подкласс возвращает свою строку

# Ваш код здесь:


# ============================================================
# Задание 5: Dataclass — Товар
# ============================================================
# Создайте @dataclass Product(name, price, quantity).
# Методы: total_cost() → price * quantity.
# Создайте корзину (список товаров) и вычислите
# общую стоимость и самый дорогой товар.
#
# Ожидаемый результат:
#   cart = [
#       Product("Ноутбук", 75000, 1),
#       Product("Мышь", 1500, 2),
#       Product("Монитор", 25000, 1),
#   ]
#   total = sum(p.total_cost() for p in cart)
#   print(f"Итого: {total}")  → "Итого: 103000"
#   expensive = max(cart, key=lambda p: p.price)
#   print(expensive.name)     → "Ноутбук"
#
# Подсказка: from dataclasses import dataclass

from dataclasses import dataclass

# Ваш код здесь:


# ============================================================
# Задание 6: Композиция — Компьютер
# ============================================================
# Создайте классы: CPU(model, cores, ghz),
# RAM(size_gb, type), HDD(size_gb, ssd: bool).
# Класс Computer содержит экземпляры каждого компонента.
# Метод specs() возвращает строку с характеристиками.
#
# Ожидаемый результат:
#   pc = Computer(
#       CPU("i7-12700K", 12, 3.6),
#       RAM(32, "DDR5"),
#       HDD(1000, ssd=True)
#   )
#   print(pc.specs())
#   # Процессор: i7-12700K (12 ядер, 3.6 GHz)
#   # Память: 32 GB DDR5
#   # Диск: 1000 GB (SSD)
#
# Подсказка: композиция = «имеет» (has-a), не «является» (is-a)

# Ваш код здесь:


# ============================================================
# Задание 7: Цепочка наследования
# ============================================================
# Vehicle(brand, year) → Car(brand, year, doors)
# → ElectricCar(brand, year, doors, battery_kwh).
# Каждый уровень добавляет атрибуты и расширяет __str__.
# Используйте super().__init__().
#
# Ожидаемый результат:
#   e = ElectricCar("Tesla", 2024, 4, 100)
#   print(e)
#   → "ElectricCar: Tesla 2024, 4 двери, батарея: 100 kWh"
#   print(isinstance(e, Vehicle))  → True
#   print(isinstance(e, Car))      → True
#
# Подсказка: super().__init__(brand, year) в каждом __init__

# Ваш код здесь:


# ============================================================
# Задание 8: Паттерн Наблюдатель (Observer)
# ============================================================
# Создайте класс EventEmitter с методами:
#   on(event, callback) — подписаться на событие
#   off(event, callback) — отписаться
#   emit(event, *args) — вызвать все обработчики
#
# Ожидаемый результат:
#   emitter = EventEmitter()
#   emitter.on("greet", lambda name: print(f"Привет, {name}!"))
#   emitter.on("greet", lambda name: print(f"Hello, {name}!"))
#   emitter.emit("greet", "Алиса")
#   # Привет, Алиса!
#   # Hello, Алиса!
#
# Подсказка: self._events = {} (словарь: событие → список функций)

# Ваш код здесь:


# ============================================================
# Задание 9: Связный список (LinkedList)
# ============================================================
# Создайте Node(value, next=None) и LinkedList.
# Методы: append, prepend, delete(value),
# search(value) → bool, __str__, __len__, __iter__.
#
# Ожидаемый результат:
#   ll = LinkedList()
#   ll.append(1); ll.append(2); ll.append(3)
#   ll.prepend(0)
#   print(ll)           → "0 → 1 → 2 → 3 → None"
#   print(len(ll))      → 4
#   print(ll.search(2)) → True
#   ll.delete(2)
#   print(ll)           → "0 → 1 → 3 → None"
#
# Подсказка: self.head = None; каждый Node хранит value и next

# Ваш код здесь:


# ============================================================
# Задание 10: Контекстный менеджер
# ============================================================
# Создайте класс Timer, реализующий __enter__ и __exit__,
# который измеряет время выполнения блока with.
# Также создайте FileManager для безопасной работы с файлами.
#
# Ожидаемый результат:
#   with Timer("Тест") as t:
#       sum(range(1000000))
#   # Блок 'Тест' выполнен за 0.0234 сек.
#
#   with FileManager("test.txt", "w") as f:
#       f.write("Привет!")
#   # файл автоматически закрыт
#
# Подсказка:
#   import time
#   def __enter__(self):
#       self.start = time.perf_counter()
#       return self
#   def __exit__(self, *args):
#       elapsed = time.perf_counter() - self.start

import time

# Ваш код здесь:
