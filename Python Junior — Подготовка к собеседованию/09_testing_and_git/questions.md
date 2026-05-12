# 09 — Тестирование и Git: Теоретические вопросы

---

## Вопрос 1: Зачем нужны тесты?

<details>
<summary>💡 Ответ</summary>

- **Предотвращение регрессий** — изменения не ломают существующий код
- **Документация** — тесты показывают, как использовать код
- **Рефакторинг** — можно безопасно менять внутреннюю реализацию
- **Уверенность** — деплой с проверенным кодом

**Виды тестов:**
- **Unit** — тестируют отдельную функцию/класс (быстрые, изолированные)
- **Integration** — тестируют взаимодействие компонентов
- **E2E (End-to-End)** — тестируют весь поток от начала до конца

Пирамида тестирования: много Unit → меньше Integration → мало E2E.
</details>

---

## Вопрос 2: `unittest` vs `pytest`?

<details>
<summary>💡 Ответ</summary>

| | `unittest` | `pytest` |
|--|-----------|---------|
| Стиль | Классы, `self.assert*` | Функции, `assert` |
| Встроенный | Да (стандартная библиотека) | Нет (pip install) |
| Фикстуры | `setUp`/`tearDown` | `@pytest.fixture` (мощнее) |
| Параметризация | Сложно | `@pytest.mark.parametrize` |
| Вывод ошибок | Базовый | Детальный diff |

```python
# unittest
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# pytest
def test_add():
    assert add(2, 3) == 5
```

**На практике:** pytest более популярен и удобен.
</details>

---

## Вопрос 3: Что такое mock и зачем он нужен?

<details>
<summary>💡 Ответ</summary>

**Mock** — подменяет реальный объект поддельным для изоляции теста.

```python
from unittest.mock import patch, MagicMock

# Подмена HTTP-запроса (не делаем реальный запрос в тестах!)
@patch('module.requests.get')
def test_fetch_data(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"name": "Alice"}
    
    result = fetch_data("https://api.example.com")
    
    assert result == {"name": "Alice"}
    mock_get.assert_called_once()
```

**Когда мокать:** внешние API, базы данных, файловую систему, текущее время.
</details>

---

## Вопрос 4: Что такое фикстуры в pytest?

<details>
<summary>💡 Ответ</summary>

**Фикстура** — функция подготовки данных/состояния для теста:

```python
import pytest

@pytest.fixture
def user():
    return {"name": "Alice", "age": 30}

@pytest.fixture
def db():
    conn = create_connection()
    yield conn       # код ДО yield — setUp, ПОСЛЕ — tearDown
    conn.close()

def test_user_name(user):
    assert user["name"] == "Alice"

def test_db_query(db):
    result = db.execute("SELECT 1")
    assert result is not None
```

Фикстуры передаются как аргументы тестовой функции (dependency injection).
</details>

---

## Вопрос 5: Что такое `parametrize` в pytest?

<details>
<summary>💡 Ответ</summary>

Запуск одного теста с разными наборами данных:

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 4),
    (3, 9),
    (-1, 1),
    (0, 0),
])
def test_square(input, expected):
    assert input ** 2 == expected
```

Создаёт 5 отдельных тестов. Если один падает — остальные продолжают.
</details>

---

## Вопрос 6: Как тестировать исключения?

<details>
<summary>💡 Ответ</summary>

```python
# pytest
import pytest

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_value_error_message():
    with pytest.raises(ValueError, match="invalid"):
        raise ValueError("invalid input")

# unittest
class TestExceptions(unittest.TestCase):
    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0
```
</details>

---

## Вопрос 7: Что такое TDD?

<details>
<summary>💡 Ответ</summary>

**TDD (Test-Driven Development)** — сначала тест, потом код:

1. **Red** — напишите тест, который падает
2. **Green** — напишите минимальный код, чтобы тест прошёл
3. **Refactor** — улучшите код, сохраняя тесты зелёными

```python
# 1. Red — тест
def test_add():
    assert add(2, 3) == 5  # функции add ещё нет → FAIL

# 2. Green — минимальная реализация
def add(a, b):
    return a + b  # тест проходит → PASS

# 3. Refactor — если нужно
```
</details>

---

## Вопрос 8: Что такое code coverage?

<details>
<summary>💡 Ответ</summary>

**Coverage** — процент кода, покрытого тестами:

```bash
pip install pytest-cov
pytest --cov=myproject --cov-report=html
```

**Виды покрытия:**
- **Line coverage** — какие строки выполнились
- **Branch coverage** — все ветки if/else проверены

**Рекомендация:** 80%+ покрытие. 100% — не всегда нужно и не гарантирует отсутствие багов.
</details>

---

## Вопрос 9: В чём разница между `git merge` и `git rebase`?

<details>
<summary>💡 Ответ</summary>

| | `merge` | `rebase` |
|--|---------|---------|
| История | Сохраняет ветвление | Линейная (чистая) |
| Конфликты | Решаются один раз | Могут решаться для каждого коммита |
| Безопасность | Не переписывает историю | Переписывает (опасно для shared веток!) |

```
merge:  A-B-C---M (merge commit)
            \  /
             D-E

rebase: A-B-C-D'-E' (линейная история)
```

**Правило:** Не делайте `rebase` на публичных ветках (main/master)!
</details>

---

## Вопрос 10: Как разрешить конфликт в Git?

<details>
<summary>💡 Ответ</summary>

```bash
git merge feature-branch
# CONFLICT in file.py

# 1. Откройте файл — найдите маркеры конфликта:
<<<<<<< HEAD
current_code()
=======
incoming_code()
>>>>>>> feature-branch

# 2. Выберите нужный вариант (или объедините)
# 3. Удалите маркеры
# 4. Сохраните файл
git add file.py
git commit -m "Resolve merge conflict"
```
</details>

---

## Вопрос 11: Что такое `git stash`?

<details>
<summary>💡 Ответ</summary>

`git stash` — временно сохраняет незакоммиченные изменения:

```bash
git stash              # сохранить изменения
git checkout main      # переключиться на другую ветку
# ... сделать что-то ...
git checkout feature   # вернуться
git stash pop          # восстановить изменения
```

`git stash list` — список stash'ей, `git stash drop` — удалить.
</details>

---

## Вопрос 12: Что такое `git cherry-pick`?

<details>
<summary>💡 Ответ</summary>

Применяет **конкретный коммит** из другой ветки:

```bash
git cherry-pick abc123  # применить коммит abc123 в текущую ветку
```

**Когда:** Нужен один конкретный фикс из другой ветки, а не весь merge.
</details>

---

## Вопрос 13: Что такое `.gitignore`?

<details>
<summary>💡 Ответ</summary>

Файл со списком шаблонов, которые Git должен игнорировать:

```gitignore
# Виртуальное окружение
venv/
.env

# Python
__pycache__/
*.pyc
*.pyo

# IDE
.vscode/
.idea/

# ОС
.DS_Store
Thumbs.db
```
</details>

---

## Вопрос 14: Что такое `git reset` и какие режимы?

<details>
<summary>💡 Ответ</summary>

```bash
git reset --soft HEAD~1   # Откатить коммит, изменения в staging
git reset --mixed HEAD~1  # Откатить коммит, изменения в working dir (default)
git reset --hard HEAD~1   # Откатить коммит, УДАЛИТЬ изменения!
```

**Осторожно:** `--hard` безвозвратно удаляет изменения!
</details>

---

## Вопрос 15: Что тестировать, а что нет?

<details>
<summary>💡 Ответ</summary>

**Тестировать:**
- Бизнес-логику (основные сценарии + edge cases)
- Валидацию входных данных
- Обработку ошибок
- Граничные условия (пустой ввод, очень большие данные)

**НЕ тестировать:**
- Стандартную библиотеку Python
- Сторонние библиотеки (они уже протестированы)
- Геттеры/сеттеры без логики
- Приватные методы напрямую (тестируйте через публичный интерфейс)
</details>
