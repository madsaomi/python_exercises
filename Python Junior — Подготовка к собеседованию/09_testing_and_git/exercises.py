"""
09 — Тестирование и Git: Практические упражнения

Напишите решения прямо в этом файле.
Запустите для проверки: python exercises.py
"""
import unittest
from unittest.mock import patch, MagicMock


# ============================================================
# Код для тестирования
# ============================================================
class Calculator:
    """Простой калькулятор для тестирования."""

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero!")
        return a / b

    def average(self, numbers):
        if not numbers:
            raise ValueError("Empty list!")
        return sum(numbers) / len(numbers)


class UserService:
    """Сервис пользователей (имитация работы с API)."""

    def __init__(self, api_client):
        self.api_client = api_client

    def get_user(self, user_id):
        response = self.api_client.get(f"/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        return None

    def create_user(self, name, email):
        if not name or not email:
            raise ValueError("Name and email are required")
        response = self.api_client.post("/users", {"name": name, "email": email})
        return response.status_code == 201


# ============================================================
# Упражнение 1: Unit-тесты для Calculator
# ============================================================
# Напишите тесты для Calculator. Покройте:
# - Нормальные сценарии (add, divide, average)
# - Граничные случаи (деление на 0, пустой список)
# - Разные типы данных (int, float, отрицательные)

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Ваши тесты здесь
    def test_add(self):
        pass  # Замените pass на тесты

    def test_divide(self):
        pass

    def test_average(self):
        pass


# ============================================================
# Упражнение 2: Тесты с mock для UserService
# ============================================================
# Напишите тесты для UserService, замокав api_client.
# Не делайте реальных HTTP-запросов!

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.mock_client = MagicMock()
        self.service = UserService(self.mock_client)

    # Ваши тесты здесь
    def test_get_user_success(self):
        pass

    def test_get_user_not_found(self):
        pass

    def test_create_user_success(self):
        pass

    def test_create_user_validation(self):
        pass


# ============================================================
# Упражнение 3: Параметризованные тесты
# ============================================================
# Напишите функцию is_palindrome и тесты для неё.
# Используйте параметризацию (subTest в unittest).
#
# Пример: "racecar" → True, "hello" → False, "" → True

def is_palindrome(s):
    """Проверяет, является ли строка палиндромом (без учёта регистра)."""
    # Ваш код здесь
    pass


class TestPalindrome(unittest.TestCase):
    # Используйте subTest для параметризации
    def test_palindromes(self):
        test_cases = [
            ("racecar", True),
            ("hello", False),
            ("", True),
            ("A", True),
            ("Aba", True),       # регистр не важен
            ("ab", False),
        ]
        for s, expected in test_cases:
            with self.subTest(s=s):
                pass  # Ваш assert здесь


# ============================================================
# Упражнение 4: Тестирование исключений
# ============================================================
# Напишите функцию validate_age и тесты для неё.
#
# Правила: возраст 0-150, целое число, не None

def validate_age(age):
    """Валидирует возраст. Бросает ValueError/TypeError при невалидном вводе."""
    # Ваш код здесь
    pass


class TestValidateAge(unittest.TestCase):
    # Ваши тесты здесь
    def test_valid_ages(self):
        pass

    def test_invalid_ages(self):
        pass


# ============================================================
# Упражнение 5: Фикстура — временный файл
# ============================================================
# Напишите функцию count_lines(filepath) и тесты.
# Используйте setUp/tearDown для создания временного файла.

import os
import tempfile

def count_lines(filepath):
    """Считает количество строк в файле."""
    # Ваш код здесь
    pass


class TestCountLines(unittest.TestCase):
    def setUp(self):
        # Создайте временный файл
        pass

    def tearDown(self):
        # Удалите временный файл
        pass

    def test_count_lines(self):
        pass


# ============================================================
# Тесты
# ============================================================
if __name__ == "__main__":
    unittest.main(verbosity=2)
