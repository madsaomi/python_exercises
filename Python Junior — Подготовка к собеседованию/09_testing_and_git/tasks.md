# 09 — Тестирование и Git: Задачи-ловушки

> ⚠️ Попробуйте предсказать результат **БЕЗ запуска**.

---

## Задача 1: assert без скобок

```python
# Какие тесты пройдут?
assert (1 == 2, "Numbers are not equal")
assert 1 == 2, "Numbers are not equal"
```

<details>
<summary>🔍 Что произойдёт?</summary>

Первый `assert` **пройдёт** (с warning), второй — **упадёт**.

**Объяснение:** `assert (1 == 2, "message")` — это `assert tuple`, а непустой кортеж всегда `True`! Скобки создают кортеж, а не группируют выражение. Правильно: `assert 1 == 2, "message"` (без скобок).
</details>

---

## Задача 2: mock side_effect

```python
from unittest.mock import MagicMock

mock_func = MagicMock(side_effect=[1, 2, ValueError("boom")])

print(mock_func())
print(mock_func())
try:
    print(mock_func())
except ValueError as e:
    print(f"Error: {e}")
```

<details>
<summary>🔍 Что выведет код?</summary>

```
1
2
Error: boom
```

**Объяснение:** `side_effect` со списком возвращает значения по порядку. Если значение — исключение, оно бросается.
</details>

---

## Задача 3: Порядок setUp/tearDown

```python
import unittest

class TestExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print("setUp")

    def test_one(self):
        print("test_one")

    def test_two(self):
        print("test_two")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
```

<details>
<summary>🔍 В каком порядке вызовутся методы?</summary>

```
setUpClass
setUp
test_one
tearDown
setUp
test_two
tearDown
tearDownClass
```

**Объяснение:** `setUpClass/tearDownClass` — один раз. `setUp/tearDown` — перед/после КАЖДОГО теста.
</details>

---

## Задача 4: patch — где мокать?

```python
# module_a.py
import requests

def fetch_data(url):
    return requests.get(url).json()

# test_module_a.py
from unittest.mock import patch

# Какой вариант правильный?
@patch('requests.get')           # Вариант A
@patch('module_a.requests.get')  # Вариант B
def test_fetch(mock_get):
    pass
```

<details>
<summary>🔍 Какой правильный?</summary>

**Вариант B: `@patch('module_a.requests.get')`**

**Правило:** Мокайте там, где объект **используется** (lookup), а не там, где он **определён**. `module_a` импортировал `requests`, поэтому мокаем в `module_a`.
</details>

---

## Задача 5: Git — detached HEAD

```bash
git checkout abc123  # checkout конкретного коммита
git commit -m "New change"
git checkout main
```

<details>
<summary>🔍 Что произойдёт с "New change"?</summary>

Коммит "New change" станет **"потерянным"** (orphaned). Он не привязан к ветке.

**Объяснение:** `git checkout <commit>` переводит в "detached HEAD" — вы не на ветке. Коммит будет удалён при `git gc`, если не создать ветку: `git branch save-my-work`.
</details>

---

## Задача 6: pytest фикстура — scope

```python
import pytest

@pytest.fixture(scope="module")
def db():
    print("CONNECT")
    yield "db_connection"
    print("DISCONNECT")

def test_one(db):
    print(f"test_one: {db}")

def test_two(db):
    print(f"test_two: {db}")
```

<details>
<summary>🔍 Сколько раз будет CONNECT/DISCONNECT?</summary>

```
CONNECT
test_one: db_connection
test_two: db_connection
DISCONNECT
```

**Объяснение:** `scope="module"` — фикстура создаётся один раз на модуль (файл). `scope="function"` (default) — для каждого теста.
</details>

---

## Задача 7: assert vs assertEqual

```python
# Что будет при падении?
# Вариант A (pytest style)
assert [1, 2, 3] == [1, 2, 4]

# Вариант B (unittest style)
self.assertEqual([1, 2, 3], [1, 2, 4])
```

<details>
<summary>🔍 Разница?</summary>

**pytest** покажет подробный diff:
```
E       assert [1, 2, 3] == [1, 2, 4]
E         At index 2 diff: 3 != 4
```

**unittest** покажет оба списка без детального diff.

Это одно из преимуществ pytest — более информативные ошибки.
</details>

---

## Задача 8: Git — force push

```bash
git push origin main --force
```

<details>
<summary>🔍 Чем это опасно?</summary>

**`--force` перезаписывает удалённую ветку!** Если коллеги уже получили предыдущие коммиты — их история разойдётся.

**Безопаснее:** `git push --force-with-lease` — отклонит push, если кто-то уже изменил remote.
</details>

---

## Задача 9: Что тестировать — входы или выходы?

```python
def calculate_discount(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid discount")
    return price * (1 - discount_percent / 100)

# Какие тесты нужны?
```

<details>
<summary>🔍 Ответ</summary>

```python
def test_normal_discount():
    assert calculate_discount(100, 20) == 80.0

def test_zero_discount():
    assert calculate_discount(100, 0) == 100.0

def test_full_discount():
    assert calculate_discount(100, 100) == 0.0

def test_negative_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, -10)

def test_over_100_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, 150)

def test_zero_price():
    assert calculate_discount(0, 50) == 0.0
```

**Паттерн:** Нормальные сценарии + граничные значения + ошибки.
</details>

---

## Задача 10: Git flow — типичный рабочий процесс

Расположите команды Git в правильном порядке для типичного workflow:

```
A) git push origin feature/login
B) git add .
C) git checkout -b feature/login
D) git commit -m "Add login form"
E) git pull origin main
F) # Написать код
```

<details>
<summary>🔍 Правильный порядок</summary>

```
E) git pull origin main             # обновить main
C) git checkout -b feature/login    # создать ветку
F) # Написать код                   # разработка
B) git add .                        # добавить в staging
D) git commit -m "Add login form"   # зафиксировать
A) git push origin feature/login    # отправить на remote
```

Далее: создать Pull Request → Code Review → Merge в main.
</details>
