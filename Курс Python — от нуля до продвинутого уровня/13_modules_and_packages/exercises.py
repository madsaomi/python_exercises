"""
============================================================
  ТЕМА 13: Модули и пакеты — Упражнения
============================================================
  Каждое задание содержит подробное описание, примеры
  ожидаемого результата и подсказки.
============================================================
"""

# ============================================================
# Задание 1: Работа с модулем math
# ============================================================
# Используя модуль math, напишите функции:
#   circle_area(r) → площадь круга
#   hypotenuse(a, b) → гипотенуза прямоугольного треугольника
#   degrees_to_radians(deg) → перевод градусов в радианы
#
# Ожидаемый результат:
#   print(circle_area(5))         → 78.53981633974483
#   print(hypotenuse(3, 4))       → 5.0
#   print(degrees_to_radians(180)) → 3.141592653589793
#
# Подсказка:
#   math.pi, math.sqrt(), math.hypot(), math.radians()

import math

# Ваш код здесь:


# ============================================================
# Задание 2: Работа с модулем random
# ============================================================
# Напишите функции:
#   roll_dice(n=2) → список из n случайных бросков кубика (1-6)
#   random_password(length=8) → случайный пароль из букв/цифр
#   shuffle_deck() → перемешанную колоду карт (масть + номинал)
#
# Ожидаемый результат:
#   print(roll_dice())          → [3, 5]
#   print(roll_dice(5))         → [1, 6, 2, 4, 3]
#   print(random_password())    → "aB3kL9mZ"
#   print(shuffle_deck()[:3])   → ["7♠", "К♥", "Т♦"]
#
# Подсказка:
#   random.randint(1, 6)
#   random.choices(chars, k=length)
#   random.shuffle(deck)

import random
import string

# Ваш код здесь:


# ============================================================
# Задание 3: Работа с модулем datetime
# ============================================================
# Напишите функции:
#   days_until_new_year() → дней до 1 января следующего года
#   age_in_days(birthdate_str) → возраст в днях ("ГГГГ-ММ-ДД")
#   format_date(dt, style="ru") → "07 мая 2025" или "May 7, 2025"
#
# Ожидаемый результат:
#   print(days_until_new_year())              → 239  (зависит от даты)
#   print(age_in_days("2000-01-01"))          → 9258 (зависит от даты)
#   print(format_date(datetime.now(), "ru"))  → "07 мая 2025"
#   print(format_date(datetime.now(), "en"))  → "May 7, 2025"
#
# Подсказка:
#   from datetime import datetime, date, timedelta
#   delta = target - date.today()
#   return delta.days

from datetime import datetime, date, timedelta

# Ваш код здесь:


# ============================================================
# Задание 4: Работа с модулем collections
# ============================================================
# Используя collections, решите задачи:
# 1. Counter — найдите 3 самых частых слова в тексте
# 2. defaultdict — сгруппируйте слова по первой букве
# 3. namedtuple — создайте Point(x, y) и вычислите расстояние
#
# Ожидаемый результат:
#   text = "кот кот собака кот собака рыба"
#   print(top_words(text, 2))
#   → [("кот", 3), ("собака", 2)]
#
#   words = ["арбуз", "апельсин", "банан", "ананас", "баклажан"]
#   print(group_by_letter(words))
#   → {"а": ["арбуз", "апельсин", "ананас"], "б": ["банан", "баклажан"]}
#
#   p1 = Point(0, 0); p2 = Point(3, 4)
#   print(distance(p1, p2))  → 5.0
#
# Подсказка:
#   from collections import Counter, defaultdict, namedtuple

from collections import Counter, defaultdict, namedtuple

# Ваш код здесь:


# ============================================================
# Задание 5: Работа с модулем os и sys
# ============================================================
# Напишите функцию system_info(), которая выводит:
#   - Операционную систему (os.name, sys.platform)
#   - Текущую директорию (os.getcwd())
#   - Версию Python (sys.version)
#   - Переменные окружения PATH (первые 3 пути)
#
# Ожидаемый результат:
#   system_info()
#   # ОС: nt (win32)
#   # Директория: C:\Users\user\project
#   # Python: 3.12.0
#   # PATH (первые 3):
#   #   - C:\Python312
#   #   - C:\Windows\system32
#   #   - C:\Windows
#
# Подсказка:
#   os.environ.get("PATH", "").split(os.pathsep)[:3]

import os
import sys

# Ваш код здесь:


# ============================================================
# Задание 6: Создание собственного модуля
# ============================================================
# Создайте (мысленно или в отдельном файле) модуль mathutils.py
# с функциями: factorial, fibonacci, is_prime, gcd.
# Здесь реализуйте эти функции и протестируйте.
#
# Ожидаемый результат:
#   print(factorial(5))    → 120
#   print(fibonacci(10))   → 55
#   print(is_prime(17))    → True
#   print(is_prime(4))     → False
#   print(gcd(12, 8))      → 4
#
# Подсказка: для is_prime проверяйте делимость до sqrt(n)
# Блок if __name__ == "__main__": для тестов.

# Ваш код здесь:


# ============================================================
# Задание 7: Работа с itertools
# ============================================================
# Используя itertools, решите задачи:
# 1. Все пары из двух списков (product)
# 2. Все перестановки букв слова (permutations)
# 3. Все комбинации по 2 из списка (combinations)
# 4. Бесконечный цикл по списку (cycle, взять первые 10)
#
# Ожидаемый результат:
#   print(all_pairs([1,2], ["a","b"]))
#   → [(1,"a"), (1,"b"), (2,"a"), (2,"b")]
#
#   print(word_permutations("ABC"))
#   → ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
#
#   print(choose_2([1, 2, 3, 4]))
#   → [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]
#
# Подсказка:
#   from itertools import product, permutations, combinations, cycle

from itertools import product, permutations, combinations, cycle, islice

# Ваш код здесь:


# ============================================================
# Задание 8: Работа с functools
# ============================================================
# Используя functools:
# 1. lru_cache — кэшируйте fibonacci для ускорения
# 2. reduce — вычислите произведение списка чисел
# 3. partial — создайте функцию double = multiply * 2
#
# Ожидаемый результат:
#   print(fibonacci_cached(100))  → 354224848179261915075 (мгновенно!)
#   print(product_of([1,2,3,4,5])) → 120
#   print(double(7))               → 14
#   print(triple(7))               → 21
#
# Подсказка:
#   from functools import lru_cache, reduce, partial
#   @lru_cache(maxsize=None)
#   def fibonacci_cached(n): ...

from functools import lru_cache, reduce, partial

# Ваш код здесь:


# ============================================================
# Задание 9: Работа с pathlib
# ============================================================
# Используя pathlib, напишите функцию analyze_directory(path),
# которая возвращает словарь с информацией:
#   - total_files: общее количество файлов
#   - total_dirs: количество поддиректорий
#   - by_extension: словарь {".py": 5, ".md": 3, ...}
#   - largest_file: (имя, размер_КБ) самого большого файла
#
# Ожидаемый результат:
#   info = analyze_directory(".")
#   print(info["total_files"])   → 15
#   print(info["by_extension"])  → {".py": 5, ".md": 3, ".txt": 2}
#   print(info["largest_file"])  → ("data.csv", 125.4)
#
# Подсказка: Path(path).rglob("*") для рекурсивного обхода

from pathlib import Path

# Ваш код здесь:


# ============================================================
# Задание 10: Пакетный импорт и __all__
# ============================================================
# Создайте структуру пакета (описание):
#   mypackage/
#       __init__.py     → from .math_ops import add, multiply
#       math_ops.py     → def add, subtract, multiply, divide
#       string_ops.py   → def reverse, capitalize_words, count_vowels
#
# Здесь реализуйте все функции и продемонстрируйте,
# как работает __all__ и относительный импорт.
#
# Ожидаемый результат:
#   # Если __all__ = ["add", "multiply"]:
#   # from mypackage import *  → доступны только add, multiply
#
#   print(add(2, 3))              → 5
#   print(multiply(4, 5))         → 20
#   print(reverse("Python"))      → "nohtyP"
#   print(capitalize_words("hello world")) → "Hello World"
#   print(count_vowels("привет")) → 2
#
# Подсказка:
#   __all__ = ["add", "multiply"]  # в __init__.py
#   Гласные: "аеёиоуыэюяaeiou"

# Ваш код здесь (реализуйте функции):
