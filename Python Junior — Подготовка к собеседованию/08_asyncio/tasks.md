# 08 — Асинхронность (asyncio): Задачи-ловушки

> ⚠️ Попробуйте предсказать вывод **БЕЗ запуска**.

---

## Задача 1: Порядок выполнения

```python
import asyncio

async def task(name, delay):
    print(f"{name} start")
    await asyncio.sleep(delay)
    print(f"{name} end")

async def main():
    await task("A", 2)
    await task("B", 1)

asyncio.run(main())
```

<details>
<summary>🔍 Что выведет код?</summary>

```
A start
A end
B start
B end
```

**Объяснение:** `await` ждёт завершения каждой задачи **последовательно**. Нет параллелизма! Для параллельного запуска нужен `gather` или `create_task`.
</details>

---

## Задача 2: `gather` — параллельность

```python
import asyncio

async def task(name, delay):
    print(f"{name} start")
    await asyncio.sleep(delay)
    print(f"{name} end")
    return name

async def main():
    results = await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3)
    )
    print(results)

asyncio.run(main())
```

<details>
<summary>🔍 Что выведет код?</summary>

```
A start
B start
C start
B end
A end
C end
['A', 'B', 'C']
```

**Объяснение:** Все три задачи стартуют почти одновременно. B завершается первой (1 сек), потом A (2 сек), потом C (3 сек). Но `results` — в порядке передачи, не завершения!
</details>

---

## Задача 3: Блокирующий код

```python
import asyncio
import time

async def task_a():
    print("A start")
    time.sleep(2)  # БЛОКИРУЮЩИЙ!
    print("A end")

async def task_b():
    print("B start")
    await asyncio.sleep(1)
    print("B end")

async def main():
    await asyncio.gather(task_a(), task_b())

asyncio.run(main())
```

<details>
<summary>🔍 Что выведет код?</summary>

```
A start
A end
B start
B end
```

**Объяснение:** `time.sleep(2)` **блокирует** весь event loop! B не может начаться, пока A спит. Нужно заменить на `await asyncio.sleep(2)`.
</details>

---

## Задача 4: Корутина без await

```python
import asyncio

async def hello():
    print("Hello!")
    return 42

async def main():
    result = hello()  # Забыли await!
    print(f"Type: {type(result)}")
    print(f"Result: {result}")

asyncio.run(main())
```

<details>
<summary>🔍 Что выведет код?</summary>

```
Type: <class 'coroutine'>
Result: <coroutine object hello at 0x...>
```

+ RuntimeWarning: coroutine 'hello' was never awaited

**Объяснение:** Без `await` корутина не выполняется! "Hello!" не будет напечатано. Вернётся корутинный объект, а не 42.
</details>

---

## Задача 5: `create_task` — когда стартует?

```python
import asyncio

async def say(msg, delay):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    task = asyncio.create_task(say("Task!", 1))
    print("Before await")
    await asyncio.sleep(2)
    print("After sleep")

asyncio.run(main())
```

<details>
<summary>🔍 Что выведет код?</summary>

```
Before await
Task!
After sleep
```

**Объяснение:** `create_task` планирует задачу. Она начинает выполняться, когда event loop получает управление (при `await`). "Task!" печатается через 1 сек, пока main спит 2 сек.
</details>

---

## Задача 6: Исключения в gather

```python
import asyncio

async def ok():
    return "OK"

async def fail():
    raise ValueError("Boom!")

async def main():
    results = await asyncio.gather(ok(), fail(), return_exceptions=True)
    for r in results:
        print(type(r).__name__, r)

asyncio.run(main())
```

<details>
<summary>🔍 Что выведет код?</summary>

```
str OK
ValueError Boom!
```

**Объяснение:** С `return_exceptions=True` исключения не бросаются, а возвращаются как результаты. Без этого флага — `ValueError` прервал бы `gather`.
</details>

---

## Задача 7: Таймаут

```python
import asyncio

async def slow():
    await asyncio.sleep(10)
    return "done"

async def main():
    try:
        result = await asyncio.wait_for(slow(), timeout=1.0)
        print(result)
    except asyncio.TimeoutError:
        print("Timeout!")

asyncio.run(main())
```

<details>
<summary>🔍 Что выведет код?</summary>

```
Timeout!
```

**Объяснение:** `slow()` спит 10 секунд, но timeout — 1 секунда. Задача отменяется и бросается `TimeoutError`.
</details>

---

## Задача 8: Семафор

```python
import asyncio

async def worker(sem, name):
    async with sem:
        print(f"{name} acquired")
        await asyncio.sleep(0.1)
    print(f"{name} released")

async def main():
    sem = asyncio.Semaphore(2)  # макс. 2 одновременно
    await asyncio.gather(
        worker(sem, "A"),
        worker(sem, "B"),
        worker(sem, "C"),
    )

asyncio.run(main())
```

<details>
<summary>🔍 Что выведет код?</summary>

```
A acquired
B acquired
A released
B released
C acquired
C released
```

**Объяснение:** Семафор с лимитом 2. A и B стартуют одновременно. C ждёт освобождения и стартует после.
</details>

---

## Задача 9: Async генератор

```python
import asyncio

async def countdown(n):
    while n > 0:
        yield n
        n -= 1
        await asyncio.sleep(0.01)

async def main():
    result = []
    async for num in countdown(3):
        result.append(num)
    print(result)

asyncio.run(main())
```

<details>
<summary>🔍 Что выведет код?</summary>

```
[3, 2, 1]
```

**Объяснение:** `async for` итерирует по асинхронному генератору. `yield` + `await` — стандартный паттерн для асинхронных итераторов.
</details>

---

## Задача 10: asyncio.Queue

```python
import asyncio

async def producer(q):
    for i in range(3):
        await q.put(i)
        print(f"Put: {i}")

async def consumer(q):
    for _ in range(3):
        item = await q.get()
        print(f"Got: {item}")

async def main():
    q = asyncio.Queue(maxsize=1)
    await asyncio.gather(producer(q), consumer(q))

asyncio.run(main())
```

<details>
<summary>🔍 Что выведет код?</summary>

```
Put: 0
Got: 0
Put: 1
Got: 1
Put: 2
Got: 2
```

**Объяснение:** Очередь с `maxsize=1`. Producer может положить только 1 элемент и ждёт, пока consumer заберёт. Получается чередование.
</details>
