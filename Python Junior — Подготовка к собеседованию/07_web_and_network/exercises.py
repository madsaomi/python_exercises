"""
07 — Веб и сети: Практические упражнения

Напишите решения прямо в этом файле.
Запустите для проверки: python exercises.py
"""
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


# ============================================================
# Упражнение 1: JSON валидатор
# ============================================================
# Напишите функцию, которая проверяет, является ли строка
# валидным JSON, и возвращает распарсенный объект или None.
#
# Пример:
#   parse_json('{"name": "Alice"}')  → {"name": "Alice"}
#   parse_json('not json')           → None
#   parse_json('')                   → None

def parse_json(text):
    # Ваш код здесь
    pass


# ============================================================
# Упражнение 2: URL парсер
# ============================================================
# Напишите функцию, которая разбирает URL на компоненты.
#
# Пример:
#   parse_url("https://api.example.com:8080/users?page=2&sort=name#section")
#   → {
#       "scheme": "https",
#       "host": "api.example.com",
#       "port": 8080,
#       "path": "/users",
#       "query": {"page": ["2"], "sort": ["name"]},
#       "fragment": "section"
#     }

def parse_url(url):
    # Ваш код здесь
    pass


# ============================================================
# Упражнение 3: Простой HTTP-клиент
# ============================================================
# Напишите функцию, которая имитирует HTTP-запрос/ответ
# (без реальной сети). Реализуйте роутер:
#
# GET  /users       → {"users": [...]}  (200)
# GET  /users/<id>  → {"user": {...}}   (200) или (404)
# POST /users       → {"created": ...}  (201)
# Другие           → {"error": "..."}  (404)

class SimpleRouter:
    def __init__(self):
        self.users = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
        ]

    def handle(self, method, path, body=None):
        """Возвращает (status_code, response_body_dict)"""
        # Ваш код здесь
        pass


# ============================================================
# Упражнение 4: Rate Limiter
# ============================================================
# Реализуйте простой rate limiter: максимум N запросов
# за period секунд.
#
# Пример:
#   limiter = RateLimiter(max_requests=3, period=1.0)
#   limiter.allow()  → True
#   limiter.allow()  → True
#   limiter.allow()  → True
#   limiter.allow()  → False (лимит исчерпан)

import time

class RateLimiter:
    # Ваш код здесь
    pass


# ============================================================
# Упражнение 5: Response builder
# ============================================================
# Напишите класс для построения HTTP-ответов (цепочка вызовов).
#
# Пример:
#   resp = (ResponseBuilder()
#       .status(200)
#       .header("Content-Type", "application/json")
#       .header("X-Request-Id", "abc123")
#       .body({"message": "OK"})
#       .build())
#   print(resp)
#   → {"status": 200, "headers": {...}, "body": {...}}

class ResponseBuilder:
    # Ваш код здесь
    pass


# ============================================================
# Тесты
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("Тестирование упражнений 07_web_and_network")
    print("=" * 50)

    # Тест 1
    print("\n--- Упражнение 1: parse_json ---")
    assert parse_json('{"name": "Alice"}') == {"name": "Alice"}
    assert parse_json("not json") is None
    assert parse_json("") is None
    assert parse_json("[1, 2, 3]") == [1, 2, 3]
    print("✅ Все тесты пройдены!")

    # Тест 2
    print("\n--- Упражнение 2: parse_url ---")
    result = parse_url("https://api.example.com:8080/users?page=2&sort=name#section")
    assert result["scheme"] == "https"
    assert result["host"] == "api.example.com"
    assert result["port"] == 8080
    assert result["path"] == "/users"
    assert result["fragment"] == "section"
    print("✅ Все тесты пройдены!")

    # Тест 3
    print("\n--- Упражнение 3: SimpleRouter ---")
    router = SimpleRouter()
    status, body = router.handle("GET", "/users")
    assert status == 200
    assert "users" in body
    status, body = router.handle("GET", "/users/1")
    assert status == 200
    status, body = router.handle("GET", "/users/99")
    assert status == 404
    print("✅ Все тесты пройдены!")

    # Тест 4
    print("\n--- Упражнение 4: RateLimiter ---")
    rl = RateLimiter(max_requests=3, period=1.0)
    assert rl.allow() is True
    assert rl.allow() is True
    assert rl.allow() is True
    assert rl.allow() is False
    print("✅ Все тесты пройдены!")

    print("\n" + "=" * 50)
    print("🎉 Все упражнения выполнены верно!")
    print("=" * 50)
