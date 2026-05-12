"""
08 — Асинхронность (asyncio): Практические упражнения

Запустите для проверки: python exercises.py
"""
import asyncio


# ============================================================
# Упражнение 1: Параллельные "загрузки"
# ============================================================
# Напишите async-функцию, которая "загружает" список URL
# параллельно и возвращает результаты.
# Имитация: каждая загрузка = asyncio.sleep(0.1)
#
# Пример:
#   results = await parallel_fetch(["url1", "url2", "url3"])
#   → [("url1", "OK"), ("url2", "OK"), ("url3", "OK")]

async def parallel_fetch(urls):
    # Ваш код здесь
    pass


# ============================================================
# Упражнение 2: Таймаут для задачи
# ============================================================
# Напишите функцию, которая выполняет корутину с таймаутом.
# Если корутина не завершилась за timeout — вернуть default.
#
# Пример:
#   result = await with_timeout(slow_task(), timeout=1.0, default="TIMEOUT")

async def with_timeout(coro, timeout, default=None):
    # Ваш код здесь
    pass


# ============================================================
# Упражнение 3: Producer-Consumer (async)
# ============================================================
# Реализуйте асинхронный Producer-Consumer с asyncio.Queue.
# Producer создаёт числа 0..n-1, Consumer считает их сумму.
#
# Пример:
#   result = await async_producer_consumer(5)
#   → 10  (0 + 1 + 2 + 3 + 4)

async def async_producer_consumer(n):
    # Ваш код здесь
    pass


# ============================================================
# Упражнение 4: Ограничитель параллелизма
# ============================================================
# Напишите функцию, которая запускает список корутин
# с ограничением: не более max_concurrent одновременно.
#
# Пример:
#   tasks = [fetch(url) for url in urls]  # 100 задач
#   results = await limited_gather(tasks, max_concurrent=5)

async def limited_gather(coros, max_concurrent=5):
    # Ваш код здесь
    pass


# ============================================================
# Упражнение 5: Async контекстный менеджер
# ============================================================
# Создайте асинхронный контекстный менеджер AsyncTimer,
# который замеряет время выполнения async-блока.
#
# Пример:
#   async with AsyncTimer() as t:
#       await asyncio.sleep(1)
#   print(f"Elapsed: {t.elapsed:.2f}s")  → ~1.00s

import time

class AsyncTimer:
    # Ваш код здесь
    pass


# ============================================================
# Тесты
# ============================================================
async def run_tests():
    print("=" * 50)
    print("Тестирование упражнений 08_asyncio")
    print("=" * 50)

    # Тест 1
    print("\n--- Упражнение 1: parallel_fetch ---")
    results = await parallel_fetch(["url1", "url2", "url3"])
    assert len(results) == 3
    assert all(r[1] == "OK" for r in results)
    print("✅ Все тесты пройдены!")

    # Тест 2
    print("\n--- Упражнение 2: with_timeout ---")
    async def quick():
        await asyncio.sleep(0.01)
        return "done"

    async def slow():
        await asyncio.sleep(10)
        return "done"

    r1 = await with_timeout(quick(), timeout=1.0, default="TIMEOUT")
    assert r1 == "done", f"Expected 'done', got {r1}"
    r2 = await with_timeout(slow(), timeout=0.1, default="TIMEOUT")
    assert r2 == "TIMEOUT", f"Expected 'TIMEOUT', got {r2}"
    print("✅ Все тесты пройдены!")

    # Тест 3
    print("\n--- Упражнение 3: async_producer_consumer ---")
    result = await async_producer_consumer(5)
    assert result == 10, f"Expected 10, got {result}"
    result = await async_producer_consumer(10)
    assert result == 45, f"Expected 45, got {result}"
    print("✅ Все тесты пройдены!")

    print("\n" + "=" * 50)
    print("🎉 Все упражнения выполнены верно!")
    print("=" * 50)


if __name__ == "__main__":
    asyncio.run(run_tests())
