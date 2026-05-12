"""
============================================================
  ТЕМА 10: Основы ООП — Упражнения
============================================================
  Каждое задание содержит подробное описание, примеры
  ожидаемого результата и подсказки.
============================================================
"""

# ============================================================
# Задание 1: Класс Student
# ============================================================
# Создайте класс Student с атрибутами: name, age, grades (список).
# Методы:
#   - average_grade() → средний балл
#   - is_excellent() → True если средний >= 4.5
#   - __str__
#
# Ожидаемый результат:
#   s = Student("Алиса", 20, [5, 4, 5, 5, 4])
#   print(s)                 → "Студент: Алиса, 20 лет, ср. балл: 4.60"
#   print(s.average_grade()) → 4.6
#   print(s.is_excellent())  → True
#
# Подсказка: sum(self.grades) / len(self.grades)

# Ваш код здесь:


# ============================================================
# Задание 2: Класс Rectangle
# ============================================================
# Атрибуты: width, height. Методы: area(), perimeter(),
# is_square(), scale(factor), __str__, __repr__.
#
# Ожидаемый результат:
#   r = Rectangle(5, 3)
#   print(r.area())       → 15
#   print(r.perimeter())  → 16
#   print(r.is_square())  → False
#   r.scale(2)
#   print(r)              → "Rectangle(10, 6)"
#
# Подсказка: is_square → self.width == self.height

# Ваш код здесь:


# ============================================================
# Задание 3: Класс BankAccount
# ============================================================
# Атрибуты: owner, _balance (начально 0).
# Методы: deposit(amount), withdraw(amount), get_balance(),
# transfer(other_account, amount), __str__.
#
# Ожидаемый результат:
#   acc = BankAccount("Алиса")
#   acc.deposit(1000)
#   acc.withdraw(300)
#   print(acc.get_balance())  → 700
#   acc.withdraw(5000)        → "Недостаточно средств!"
#
#   acc2 = BankAccount("Борис")
#   acc.transfer(acc2, 200)
#   print(acc.get_balance())  → 500
#   print(acc2.get_balance()) → 200
#
# Подсказка: проверяйте amount > 0 и amount <= self._balance

# Ваш код здесь:


# ============================================================
# Задание 4: Класс Book и магические методы
# ============================================================
# Атрибуты: title, author, pages. Реализуйте:
#   __str__  → "Название — Автор (стр. N)"
#   __eq__   → по title и author
#   __lt__   → по pages (для сортировки)
#   __len__  → pages
#   __contains__ → слово in title
#
# Ожидаемый результат:
#   b1 = Book("Война и мир", "Толстой", 1225)
#   b2 = Book("Анна Каренина", "Толстой", 864)
#   print(b1)           → "Война и мир — Толстой (стр. 1225)"
#   print(b1 == b2)     → False
#   print(b2 < b1)      → True
#   print("мир" in b1)  → True
#   books = [b1, b2]; books.sort()
#   print(books[0].title) → "Анна Каренина"
#
# Подсказка: __contains__(self, item) → item in self.title

# Ваш код здесь:


# ============================================================
# Задание 5: Класс Stack (стек)
# ============================================================
# LIFO-структура. Методы: push, pop, peek, is_empty.
# Магические: __len__, __str__, __bool__.
#
# Ожидаемый результат:
#   s = Stack()
#   s.push(1); s.push(2); s.push(3)
#   print(s)         → "Stack([1, 2, 3])"
#   print(len(s))    → 3
#   print(s.peek())  → 3
#   print(s.pop())   → 3
#   print(s.pop())   → 2
#   print(len(s))    → 1
#
# Подсказка: self._items = []; pop → self._items.pop()

# Ваш код здесь:


# ============================================================
# Задание 6: Класс Temperature с @property
# ============================================================
# Хранит температуру в Цельсиях. @property для:
#   celsius (getter + setter, не ниже -273.15)
#   fahrenheit (getter): F = C * 9/5 + 32
#   kelvin (getter): K = C + 273.15
#
# Ожидаемый результат:
#   t = Temperature(100)
#   print(t.celsius)     → 100
#   print(t.fahrenheit)  → 212.0
#   print(t.kelvin)      → 373.15
#   t.celsius = -300     → "Ошибка: ниже абс. нуля!"
#   print(t.celsius)     → 100  (не изменилось)
#
# Подсказка:
#   @celsius.setter
#   def celsius(self, value):
#       if value < -273.15: ...

# Ваш код здесь:


# ============================================================
# Задание 7: Класс Counter с перегрузкой операторов
# ============================================================
# Атрибут value (начально 0). Методы: increment(n=1),
# decrement(n=1, не ниже 0), reset().
# Магические: __add__, __iadd__, __eq__, __lt__, __str__.
#
# Ожидаемый результат:
#   c1 = Counter(); c1.increment(5); c1.decrement(2)
#   print(c1)       → "Counter(3)"
#   c2 = Counter(); c2.increment(7)
#   c3 = c1 + c2
#   print(c3)       → "Counter(10)"
#   c1 += 10
#   print(c1)       → "Counter(13)"
#
# Подсказка: __add__ → Counter(self.value + other.value)

# Ваш код здесь:


# ============================================================
# Задание 8: Класс TodoList
# ============================================================
# Задача — словарь {"id", "text", "done"}.
# Методы: add_task, complete_task, delete_task,
# show_tasks, pending_count.
#
# Ожидаемый результат:
#   todo = TodoList()
#   todo.add_task("Купить продукты")
#   todo.add_task("Выучить Python")
#   todo.show_tasks()
#   # [ ] 1. Купить продукты
#   # [ ] 2. Выучить Python
#   todo.complete_task(2)
#   todo.show_tasks()
#   # [ ] 1. Купить продукты
#   # [✓] 2. Выучить Python
#   print(todo.pending_count()) → 1
#
# Подсказка: self._tasks = []; self._next_id = 1

# Ваш код здесь:


# ============================================================
# Задание 9: Класс Vector (2D)
# ============================================================
# Координаты x, y. Магические методы:
#   __add__, __sub__, __mul__(скаляр), __rmul__,
#   __abs__ (длина), __eq__, dot(other), __str__.
#
# Ожидаемый результат:
#   v1 = Vector(3, 4); v2 = Vector(1, 2)
#   print(v1 + v2)    → "Vector(4, 6)"
#   print(v1 - v2)    → "Vector(2, 2)"
#   print(v1 * 3)     → "Vector(9, 12)"
#   print(abs(v1))    → 5.0
#   print(v1.dot(v2)) → 11
#
# Подсказка: abs → math.sqrt(x² + y²)

import math

# Ваш код здесь:


# ============================================================
# Задание 10: Класс Playlist
# ============================================================
# Атрибуты: name, _songs (list), _current (int).
# Методы: add_song, remove_song, current_song,
# next_song (циклично), prev_song, shuffle.
# Магические: __len__, __contains__, __iter__.
#
# Ожидаемый результат:
#   pl = Playlist("Rock")
#   pl.add_song("Bohemian Rhapsody")
#   pl.add_song("Imagine")
#   pl.add_song("Hotel California")
#   print(pl.current_song()) → "Bohemian Rhapsody"
#   pl.next_song(); pl.next_song(); pl.next_song()
#   print(pl.current_song()) → "Bohemian Rhapsody"  # цикл!
#   print("Imagine" in pl)   → True
#
# Подсказка: self._current %= len(self._songs)

import random

# Ваш код здесь:
