"""
============================================================
  ТЕМА 19: Тестирование — Упражнения
============================================================
  Каждое задание содержит подробное описание, примеры
  ожидаемого результата и подсказки.
  Запуск тестов: python -m pytest exercises.py -v
  Или: python -m unittest exercises.py
============================================================
"""
import unittest

# ============================================================
# Задание 1: Первый unittest
# ============================================================
# Напишите функцию add(a, b) и класс TestAdd с тестами:
#   test_positive — сложение положительных
#   test_negative — сложение отрицательных
#   test_zero — сложение с нулём
#   test_float — сложение дробных чисел
#
# Ожидаемый результат (запуск тестов):
#   test_float ... ok
#   test_negative ... ok
#   test_positive ... ok
#   test_zero ... ok
#   Ran 4 tests in 0.001s — OK
#
# Подсказка:
#   class TestAdd(unittest.TestCase):
#       def test_positive(self):
#           self.assertEqual(add(2, 3), 5)

def add(a, b):
    return a + b

# Ваш тесты здесь:


# ============================================================
# Задание 2: Тестирование строковых функций
# ============================================================
# Напишите функции и тесты для каждой:
#   reverse_string(s) → "abc" → "cba"
#   is_palindrome(s) → "шалаш" → True
#   count_vowels(s) → "привет" → 2
#
# Ожидаемый результат:
#   class TestStringFunctions(unittest.TestCase):
#       def test_reverse(self):
#           self.assertEqual(reverse_string("hello"), "olleh")
#           self.assertEqual(reverse_string(""), "")
#
#       def test_palindrome(self):
#           self.assertTrue(is_palindrome("шалаш"))
#           self.assertFalse(is_palindrome("привет"))
#
#       def test_vowels(self):
#           self.assertEqual(count_vowels("привет"), 2)
#           self.assertEqual(count_vowels("бвгд"), 0)
#
# Подсказка: гласные = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU"

# Ваш код и тесты здесь:


# ============================================================
# Задание 3: setUp и tearDown
# ============================================================
# Создайте класс Calculator (add, sub, mul, div, history).
# Напишите TestCalculator с setUp (создаёт экземпляр)
# и tearDown (очищает историю).
#
# Ожидаемый результат:
#   class TestCalculator(unittest.TestCase):
#       def setUp(self):
#           self.calc = Calculator()
#
#       def test_add(self):
#           self.assertEqual(self.calc.add(2, 3), 5)
#
#       def test_history(self):
#           self.calc.add(1, 2)
#           self.calc.mul(3, 4)
#           self.assertEqual(len(self.calc.history), 2)
#
#       def tearDown(self):
#           self.calc.history.clear()
#
# Подсказка: self.history = []; каждый метод добавляет операцию

# Ваш код и тесты здесь:


# ============================================================
# Задание 4: Тестирование исключений
# ============================================================
# Напишите функцию divide(a, b), которая вызывает:
#   ZeroDivisionError при b == 0
#   TypeError при нечисловых аргументах
# Протестируйте оба исключения.
#
# Ожидаемый результат:
#   class TestDivide(unittest.TestCase):
#       def test_normal(self):
#           self.assertEqual(divide(10, 2), 5.0)
#
#       def test_zero_division(self):
#           with self.assertRaises(ZeroDivisionError):
#               divide(10, 0)
#
#       def test_type_error(self):
#           with self.assertRaises(TypeError):
#               divide("10", 2)
#
# Подсказка: self.assertRaises(ErrorType) как контекстный менеджер

# Ваш код и тесты здесь:


# ============================================================
# Задание 5: Параметризованные тесты
# ============================================================
# Напишите функцию fizzbuzz(n) → "Fizz"/"Buzz"/"FizzBuzz"/str(n).
# Протестируйте множество случаев с subTest.
#
# Ожидаемый результат:
#   class TestFizzBuzz(unittest.TestCase):
#       def test_cases(self):
#           cases = [
#               (1, "1"), (3, "Fizz"), (5, "Buzz"),
#               (15, "FizzBuzz"), (30, "FizzBuzz"),
#               (7, "7"), (9, "Fizz"), (10, "Buzz"),
#           ]
#           for n, expected in cases:
#               with self.subTest(n=n):
#                   self.assertEqual(fizzbuzz(n), expected)
#
# Подсказка: subTest позволяет видеть какой именно случай упал

# Ваш код и тесты здесь:


# ============================================================
# Задание 6: Тестирование класса (BankAccount)
# ============================================================
# Создайте BankAccount(owner, balance=0) с методами:
#   deposit, withdraw, transfer, get_balance.
# Напишите полный набор тестов.
#
# Ожидаемый результат:
#   class TestBankAccount(unittest.TestCase):
#       def setUp(self):
#           self.acc1 = BankAccount("Алиса", 1000)
#           self.acc2 = BankAccount("Борис", 500)
#
#       def test_deposit(self):
#           self.acc1.deposit(500)
#           self.assertEqual(self.acc1.get_balance(), 1500)
#
#       def test_withdraw_insufficient(self):
#           with self.assertRaises(ValueError):
#               self.acc1.withdraw(5000)
#
#       def test_transfer(self):
#           self.acc1.transfer(self.acc2, 300)
#           self.assertEqual(self.acc1.get_balance(), 700)
#           self.assertEqual(self.acc2.get_balance(), 800)
#
# Подсказка: withdraw должен вызывать ValueError при нехватке

# Ваш код и тесты здесь:


# ============================================================
# Задание 7: Mock-объекты
# ============================================================
# Напишите функцию get_user_data(user_id), которая
# "обращается к API" (имитация). Используйте unittest.mock
# для тестирования без реального запроса.
#
# Ожидаемый результат:
#   from unittest.mock import patch, MagicMock
#
#   class TestGetUserData(unittest.TestCase):
#       @patch("requests.get")
#       def test_success(self, mock_get):
#           mock_get.return_value.json.return_value = {
#               "name": "Алиса", "age": 25
#           }
#           mock_get.return_value.status_code = 200
#           result = get_user_data(1)
#           self.assertEqual(result["name"], "Алиса")
#           mock_get.assert_called_once()
#
# Подсказка: @patch заменяет реальный объект на mock

from unittest.mock import patch, MagicMock

# Ваш код и тесты здесь:


# ============================================================
# Задание 8: Тестирование работы с файлами
# ============================================================
# Напишите функцию read_config(path) → словарь из INI-файла.
# Протестируйте с использованием tempfile (временный файл).
#
# Ожидаемый результат:
#   import tempfile, os
#
#   class TestReadConfig(unittest.TestCase):
#       def test_read(self):
#           with tempfile.NamedTemporaryFile(mode="w", suffix=".ini",
#                                           delete=False) as f:
#               f.write("host=localhost\nport=8080\ndebug=true\n")
#               path = f.name
#           config = read_config(path)
#           self.assertEqual(config["host"], "localhost")
#           self.assertEqual(config["port"], "8080")
#           os.unlink(path)
#
# Подсказка: tempfile.NamedTemporaryFile для создания временных файлов

import tempfile
import os

# Ваш код и тесты здесь:


# ============================================================
# Задание 9: Покрытие кода (coverage)
# ============================================================
# Напишите функцию classify_age(age):
#   age < 0 → ValueError
#   0-12 → "ребёнок"
#   13-17 → "подросток"
#   18-64 → "взрослый"
#   65+ → "пожилой"
# Напишите тесты, покрывающие ВСЕ ветки (100% coverage).
#
# Ожидаемый результат (запуск с coverage):
#   pip install coverage
#   coverage run -m pytest exercises.py
#   coverage report
#   # Name           Stmts  Miss  Cover
#   # exercises.py      50     0   100%
#
# Подсказка: не забудьте граничные значения: 0, 12, 13, 17, 18, 64, 65

# Ваш код и тесты здесь:


# ============================================================
# Задание 10: Интеграционный тест — TodoApp
# ============================================================
# Создайте TodoApp (add_task, complete, delete, get_all).
# Хранение в списке. Напишите тест полного сценария:
# добавить → проверить → выполнить → удалить → проверить.
#
# Ожидаемый результат:
#   class TestTodoIntegration(unittest.TestCase):
#       def test_full_workflow(self):
#           app = TodoApp()
#           # Добавление
#           app.add_task("Задача 1")
#           app.add_task("Задача 2")
#           self.assertEqual(len(app.get_all()), 2)
#           # Выполнение
#           app.complete(1)
#           self.assertTrue(app.get_all()[0]["done"])
#           # Удаление
#           app.delete(1)
#           self.assertEqual(len(app.get_all()), 1)
#           self.assertEqual(app.get_all()[0]["text"], "Задача 2")
#
# Подсказка: полный workflow тест проверяет интеграцию всех методов

# Ваш код и тесты здесь:


# ============================================================
# Запуск тестов (раскомментируйте для запуска):
# ============================================================
# if __name__ == "__main__":
#     unittest.main()
