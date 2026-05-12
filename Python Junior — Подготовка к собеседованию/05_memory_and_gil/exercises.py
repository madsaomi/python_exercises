"""
05 — Память, GIL и многопоточность: Практические упражнения

Напишите решения прямо в этом файле.
Запустите для проверки: python exercises.py
"""
import threading
from concurrent.futures import ThreadPoolExecutor


# ============================================================
# Упражнение 1: Потокобезопасный счётчик
# ============================================================
# Реализуйте потокобезопасный счётчик с Lock.
#
# Пример:
#   counter = SafeCounter()
#   # запуск 10 потоков, каждый вызывает increment() 1000 раз
#   print(counter.value)  → 10000 (всегда!)

class SafeCounter:
    # Ваш код здесь
    pass


# ============================================================
# Упражнение 2: Параллельная загрузка (имитация)
# ============================================================
# Используя ThreadPoolExecutor, напишите функцию, которая
# "загружает" список URL параллельно (имитация через time.sleep).
# Верните список результатов.
#
# Пример:
#   results = parallel_download(["url1", "url2", "url3"], workers=3)
#   print(results)  → [("url1", 200), ("url2", 200), ("url3", 200)]

import time

def parallel_download(urls, workers=3):
    # Ваш код здесь
    # Имитация: def download(url): time.sleep(0.1); return (url, 200)
    pass


# ============================================================
# Упражнение 3: Контекстный менеджер для ресурса
# ============================================================
# Напишите контекстный менеджер, который гарантирует
# освобождение ресурса (файла/соединения).
# Реализуйте через __enter__ / __exit__.
#
# Пример:
#   with ManagedResource("db_connection") as res:
#       print(res.name)     → "db_connection"
#       print(res.is_open)  → True
#   print(res.is_open)      → False

class ManagedResource:
    # Ваш код здесь
    pass


# ============================================================
# Упражнение 4: Измерение памяти
# ============================================================
# Напишите функцию, которая сравнивает потребление памяти
# list vs tuple vs набор с __slots__ для N элементов.
# Верните словарь с размерами.
#
# Пример:
#   compare_memory(1000)
#   → {"list": ..., "tuple": ..., "slots": ...}

import sys

def compare_memory(n):
    # Ваш код здесь
    pass


# ============================================================
# Упражнение 5: Producer-Consumer с Queue
# ============================================================
# Реализуйте паттерн Producer-Consumer:
# - Producer добавляет числа от 0 до n в очередь
# - Consumer читает из очереди и возвращает сумму
# Используйте threading и queue.Queue.
#
# Пример:
#   result = producer_consumer(10)
#   print(result)  → 45 (сумма 0+1+...+9)

from queue import Queue

def producer_consumer(n):
    # Ваш код здесь
    pass


# ============================================================
# Тесты
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("Тестирование упражнений 05_memory_and_gil")
    print("=" * 50)

    # Тест 1
    print("\n--- Упражнение 1: SafeCounter ---")
    counter = SafeCounter()
    threads = []
    for _ in range(10):
        t = threading.Thread(target=lambda: [counter.increment() for _ in range(1000)])
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    assert counter.value == 10000, f"Ожидалось 10000, получено {counter.value}"
    print("✅ Все тесты пройдены!")

    # Тест 3
    print("\n--- Упражнение 3: ManagedResource ---")
    with ManagedResource("test_db") as res:
        assert res.name == "test_db"
        assert res.is_open is True
    assert res.is_open is False
    print("✅ Все тесты пройдены!")

    # Тест 5
    print("\n--- Упражнение 5: producer_consumer ---")
    result = producer_consumer(10)
    assert result == 45, f"Ожидалось 45, получено {result}"
    print("✅ Все тесты пройдены!")

    print("\n" + "=" * 50)
    print("🎉 Все упражнения выполнены верно!")
    print("=" * 50)
