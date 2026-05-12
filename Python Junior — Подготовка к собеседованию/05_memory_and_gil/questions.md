# 05 — Память, GIL и многопоточность: Теоретические вопросы

---

## Вопрос 1: Как Python управляет памятью?

<details>
<summary>💡 Ответ</summary>

Python использует два механизма:

1. **Reference counting** — у каждого объекта есть счётчик ссылок. Когда он достигает 0 — объект удаляется.
2. **Garbage collector** (модуль `gc`) — находит и удаляет **циклические ссылки**, которые reference counting не может обнаружить.

```python
import sys

a = [1, 2, 3]
print(sys.getrefcount(a))  # 2 (a + аргумент функции)

b = a
print(sys.getrefcount(a))  # 3

del b
print(sys.getrefcount(a))  # 2
```
</details>

---

## Вопрос 2: Что такое циклические ссылки?

<details>
<summary>💡 Ответ</summary>

Циклическая ссылка — когда объекты ссылаются друг на друга. Reference counting не может их удалить.

```python
a = []
b = []
a.append(b)  # a → b
b.append(a)  # b → a (цикл!)
del a, b     # счётчик ссылок не достигнет 0!
```

Garbage collector (GC) обнаруживает такие циклы и освобождает память. GC работает периодически и использует поколенческий алгоритм (3 поколения).
</details>

---

## Вопрос 3: Что такое GIL?

<details>
<summary>💡 Ответ</summary>

**GIL (Global Interpreter Lock)** — мьютекс в CPython, который позволяет только **одному потоку** выполнять Python-байткод в каждый момент времени.

**Зачем нужен:** Защищает reference counting от race conditions.

**Последствия:**
- CPU-bound задачи НЕ ускоряются многопоточностью
- I/O-bound задачи — ускоряются (GIL освобождается при ожидании I/O)

**Решения для CPU-bound:**
- `multiprocessing` — отдельные процессы, каждый со своим GIL
- C-расширения, которые освобождают GIL (NumPy)
- Альтернативные интерпретаторы (PyPy, Jython)
</details>

---

## Вопрос 4: `threading` vs `multiprocessing` — когда что?

<details>
<summary>💡 Ответ</summary>

| | `threading` | `multiprocessing` |
|--|-------------|-------------------|
| GIL | Ограничивает | Каждый процесс — свой GIL |
| Память | Общая | Изолированная |
| Подходит для | I/O-bound (сеть, файлы) | CPU-bound (вычисления) |
| Накладные расходы | Малые | Большие (создание процесса) |
| Обмен данными | Просто (общие переменные) | Сложнее (Queue, Pipe, shared memory) |

```python
# I/O-bound → threading
import threading
t = threading.Thread(target=download_file, args=(url,))

# CPU-bound → multiprocessing
from multiprocessing import Process
p = Process(target=heavy_computation, args=(data,))
```
</details>

---

## Вопрос 5: Что такое `concurrent.futures`?

<details>
<summary>💡 Ответ</summary>

Высокоуровневый API для параллельного выполнения:

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Для I/O-bound
with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(download, urls)

# Для CPU-bound
with ProcessPoolExecutor(max_workers=4) as executor:
    results = executor.map(compute, data_chunks)
```

Преимущества: единый интерфейс, пулы потоков/процессов, обработка исключений.
</details>

---

## Вопрос 6: Что такое race condition?

<details>
<summary>💡 Ответ</summary>

**Race condition** — ошибка, когда результат зависит от порядка выполнения потоков.

```python
import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # НЕ атомарная операция!

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start(); t2.start()
t1.join(); t2.join()

print(counter)  # Не 200000! Каждый раз разный результат
```

**Решение:** Lock, RLock, Semaphore:
```python
lock = threading.Lock()
with lock:
    counter += 1
```
</details>

---

## Вопрос 7: Что такое deadlock?

<details>
<summary>💡 Ответ</summary>

**Deadlock** — взаимная блокировка: два потока ждут друг друга и не могут продолжить.

```python
lock_a = threading.Lock()
lock_b = threading.Lock()

# Поток 1: lock_a → lock_b
# Поток 2: lock_b → lock_a
# → Deadlock!
```

**Как избежать:** Всегда захватывайте блокировки в одном и том же порядке.
</details>

---

## Вопрос 8: Что такое `__del__` и финализатор?

<details>
<summary>💡 Ответ</summary>

`__del__` — вызывается перед удалением объекта (финализатор). **Не рекомендуется использовать:**

- Нет гарантии, когда он будет вызван
- Может помешать GC при циклических ссылках
- Исключения в `__del__` игнорируются

```python
class Resource:
    def __del__(self):
        print("Resource deleted")  # когда? неизвестно!

# Лучше: контекстный менеджер
class Resource:
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.cleanup()  # гарантированный вызов
```
</details>

---

## Вопрос 9: Как измерить потребление памяти?

<details>
<summary>💡 Ответ</summary>

```python
import sys

# Размер объекта
print(sys.getsizeof([]))         # 56 байт
print(sys.getsizeof([1,2,3]))    # 88 байт
print(sys.getsizeof({}))         # 64 байт

# Сравнение структур
print(sys.getsizeof((1,2,3)))    # 64 байт (tuple < list)
print(sys.getsizeof([1,2,3]))    # 88 байт
```

**Важно:** `sys.getsizeof()` не учитывает вложенные объекты!
</details>

---

## Вопрос 10: Что такое пул потоков и зачем он нужен?

<details>
<summary>💡 Ответ</summary>

**Пул потоков** — заранее созданный набор потоков для выполнения задач. Экономит время на создании/уничтожении потоков.

```python
from concurrent.futures import ThreadPoolExecutor

def fetch(url):
    # ...
    return response

urls = ["url1", "url2", "url3", "url4"]

with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(fetch, urls))
```

**Преимущества:** переиспользование потоков, контроль максимального количества, удобный API.
</details>

---

## Вопрос 11: Как передать данные между процессами?

<details>
<summary>💡 Ответ</summary>

```python
from multiprocessing import Process, Queue

def worker(q):
    q.put("result")

q = Queue()
p = Process(target=worker, args=(q,))
p.start()
print(q.get())  # "result"
p.join()
```

Другие способы: `Pipe`, `Value`, `Array`, `Manager`.
</details>

---

## Вопрос 12: Что такое `daemon` поток?

<details>
<summary>💡 Ответ</summary>

**Daemon-поток** — фоновый поток, который автоматически завершается при завершении основной программы.

```python
import threading

t = threading.Thread(target=background_task, daemon=True)
t.start()
# Программа завершится, даже если t ещё работает
```

Обычные (не-daemon) потоки не дают программе завершиться, пока они работают.
</details>

---

## Вопрос 13: Можно ли удалить GIL?

<details>
<summary>💡 Ответ</summary>

- **PEP 703** (Python 3.13+) — экспериментальный режим **free-threaded** Python (без GIL)
- Включается флагом `--disable-gil` при компиляции
- Jython и IronPython не имеют GIL
- PyPy использует другой подход к управлению памятью

GIL — это деталь реализации **CPython**, а не языка Python.
</details>

---

## Вопрос 14: Что такое слабые ссылки (`weakref`)?

<details>
<summary>💡 Ответ</summary>

**Слабая ссылка** не увеличивает счётчик ссылок. Объект может быть удалён, даже если на него есть слабые ссылки.

```python
import weakref

class MyClass:
    pass

obj = MyClass()
ref = weakref.ref(obj)

print(ref())   # <__main__.MyClass object>
del obj
print(ref())   # None — объект удалён
```

**Применение:** кэши, обратные ссылки, избежание циклических ссылок.
</details>

---

## Вопрос 15: Чем `threading.Lock` отличается от `threading.RLock`?

<details>
<summary>💡 Ответ</summary>

- `Lock` — может быть захвачен только один раз. Повторный `acquire()` из того же потока → **deadlock**.
- `RLock` (Reentrant Lock) — может быть захвачен **несколько раз** одним потоком. Нужно столько же `release()`.

```python
lock = threading.Lock()
lock.acquire()
# lock.acquire()  # DEADLOCK!

rlock = threading.RLock()
rlock.acquire()
rlock.acquire()   # OK
rlock.release()
rlock.release()
```
</details>
