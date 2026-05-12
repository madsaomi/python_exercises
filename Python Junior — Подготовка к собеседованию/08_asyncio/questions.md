# 08 — Асинхронность (asyncio): Теоретические вопросы

---

## Вопрос 1: Что такое асинхронное программирование?

<details>
<summary>💡 Ответ</summary>

**Асинхронное программирование** — подход, при котором задачи не блокируют выполнение друг друга. Пока одна задача ждёт (I/O, сеть, БД), другие могут выполняться.

```
Синхронно:    [Задача 1 ████████] [Задача 2 ████████] — 16 сек
Асинхронно:   [Задача 1 ██--██--] — 8 сек
              [Задача 2 --██--██]
              (-- = ожидание I/O)
```

**Ключевое отличие от многопоточности:** Асинхронность работает в **одном потоке** через кооперативную многозадачность.
</details>

---

## Вопрос 2: Что такое Event Loop?

<details>
<summary>💡 Ответ</summary>

**Event Loop** — бесконечный цикл, который управляет выполнением корутин. Он решает, какую корутину запустить, когда одна «приостановилась» (await).

```python
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(1)
    print("End")

asyncio.run(main())  # создаёт event loop, запускает корутину
```

Event Loop: `main()` → встретил `await sleep(1)` → переключился на другие задачи → через 1 сек вернулся → `print("End")`.
</details>

---

## Вопрос 3: Что такое корутина (coroutine)?

<details>
<summary>💡 Ответ</summary>

**Корутина** — функция, определённая через `async def`. Вызов корутины **не выполняет** её — создаёт корутинный объект.

```python
async def hello():
    return "Hello!"

# Просто вызов — НЕ выполняет!
coro = hello()  # <coroutine object hello at 0x...>

# Для выполнения нужен await или event loop
result = await coro  # "Hello!"
```
</details>

---

## Вопрос 4: `asyncio.gather` vs `asyncio.create_task`

<details>
<summary>💡 Ответ</summary>

```python
import asyncio

async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name}: done"

# gather — запускает все корутины и ждёт ВСЕ результаты
async def with_gather():
    results = await asyncio.gather(
        fetch("A", 1),
        fetch("B", 2),
        fetch("C", 1)
    )
    print(results)  # ["A: done", "B: done", "C: done"]

# create_task — создаёт задачу, которая начинает выполняться
async def with_tasks():
    task1 = asyncio.create_task(fetch("A", 1))
    task2 = asyncio.create_task(fetch("B", 2))
    # задачи уже выполняются!
    result1 = await task1
    result2 = await task2
```

`gather` — проще, для группового запуска. `create_task` — для более гибкого управления.
</details>

---

## Вопрос 5: Когда asyncio НЕ поможет?

<details>
<summary>💡 Ответ</summary>

**asyncio не ускоряет CPU-bound задачи!**

```python
# ❌ asyncio НЕ поможет — CPU-bound
async def compute():
    total = sum(range(100_000_000))  # блокирует event loop!

# ✅ Для CPU-bound — multiprocessing
from concurrent.futures import ProcessPoolExecutor

# ✅ Или запуск в отдельном потоке
result = await asyncio.to_thread(cpu_bound_function, args)
```

asyncio полезен для **I/O-bound**: HTTP-запросы, БД, файлы, WebSocket.
</details>

---

## Вопрос 6: Что такое `async with` и `async for`?

<details>
<summary>💡 Ответ</summary>

```python
# Асинхронный контекстный менеджер
async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.json()

# Асинхронный итератор
async for message in websocket:
    print(message)
```

Для реализации нужны магические методы:
- `async with`: `__aenter__`, `__aexit__`
- `async for`: `__aiter__`, `__anext__`
</details>

---

## Вопрос 7: `asyncio.sleep` vs `time.sleep`

<details>
<summary>💡 Ответ</summary>

```python
# ❌ time.sleep — БЛОКИРУЕТ event loop!
async def bad():
    time.sleep(5)  # Весь event loop замёр на 5 секунд

# ✅ asyncio.sleep — НЕ блокирует
async def good():
    await asyncio.sleep(5)  # Event loop может делать другие задачи
```

**Правило:** В async-коде НИКОГДА не используйте блокирующие операции: `time.sleep`, `requests.get`, `open()` для больших файлов.
</details>

---

## Вопрос 8: Что такое `asyncio.Queue`?

<details>
<summary>💡 Ответ</summary>

Асинхронная очередь для обмена данными между корутинами:

```python
import asyncio

async def producer(queue):
    for i in range(5):
        await queue.put(i)
    await queue.put(None)  # сигнал завершения

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Got: {item}")

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())
```
</details>

---

## Вопрос 9: Как обработать исключения в `asyncio.gather`?

<details>
<summary>💡 Ответ</summary>

```python
# По умолчанию — первое исключение остановит всё
try:
    results = await asyncio.gather(task1(), task2(), task3())
except Exception as e:
    print(f"Error: {e}")

# С return_exceptions=True — исключения возвращаются как результаты
results = await asyncio.gather(task1(), task2(), task3(), return_exceptions=True)
for r in results:
    if isinstance(r, Exception):
        print(f"Error: {r}")
    else:
        print(f"OK: {r}")
```
</details>

---

## Вопрос 10: Что такое `asyncio.Semaphore`?

<details>
<summary>💡 Ответ</summary>

**Semaphore** — ограничивает количество одновременно выполняющихся корутин:

```python
sem = asyncio.Semaphore(10)  # максимум 10 одновременно

async def fetch(url):
    async with sem:
        async with aiohttp.ClientSession() as session:
            return await session.get(url)

# Запустит 1000 задач, но одновременно не более 10
await asyncio.gather(*[fetch(url) for url in urls])
```

**Зачем:** Не перегружать сервер/БД/файловую систему.
</details>

---

## Вопрос 11: `asyncio.run` vs `loop.run_until_complete`

<details>
<summary>💡 Ответ</summary>

```python
# Современный способ (Python 3.7+)
asyncio.run(main())  # создаёт event loop, запускает, закрывает

# Старый способ (до 3.7)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```

`asyncio.run()` — проще и безопаснее. Создаёт новый event loop каждый раз.
</details>

---

## Вопрос 12: Чем `asyncio` отличается от `threading`?

<details>
<summary>💡 Ответ</summary>

| | `asyncio` | `threading` |
|--|-----------|-------------|
| Потоки | 1 поток | Несколько потоков |
| Переключение | Кооперативное (await) | Принудительное (OS) |
| GIL | Не применим | Ограничивает CPU-bound |
| Масштабируемость | 10000+ задач | ~100-1000 потоков |
| Race conditions | Редко (один поток) | Часто |
| Подходит для | I/O-bound | I/O-bound |
</details>

---

## Вопрос 13: Что такое `asyncio.to_thread`?

<details>
<summary>💡 Ответ</summary>

Запускает синхронную (блокирующую) функцию в отдельном потоке, не блокируя event loop:

```python
import asyncio

def blocking_io():
    # Синхронная функция (например, requests)
    import time
    time.sleep(2)
    return "done"

async def main():
    result = await asyncio.to_thread(blocking_io)
    print(result)

asyncio.run(main())
```

Полезно для интеграции с синхронными библиотеками (requests, sqlite3).
</details>

---

## Вопрос 14: Что такое `asyncio.wait_for`?

<details>
<summary>💡 Ответ</summary>

Устанавливает таймаут для корутины:

```python
async def slow_task():
    await asyncio.sleep(10)
    return "done"

try:
    result = await asyncio.wait_for(slow_task(), timeout=2.0)
except asyncio.TimeoutError:
    print("Timeout!")
```
</details>

---

## Вопрос 15: Можно ли использовать `await` вне `async` функции?

<details>
<summary>💡 Ответ</summary>

**Нет!** `await` можно использовать только внутри `async def` функций.

```python
# ❌ SyntaxError
def regular():
    await asyncio.sleep(1)

# ✅ Правильно
async def async_func():
    await asyncio.sleep(1)

# В скрипте верхнего уровня:
asyncio.run(async_func())
```

Исключение: Python 3.10+ в интерактивном режиме (ipython, jupyter) поддерживает top-level `await`.
</details>
