# 📘 Тема 19: Тестирование

## Зачем тестировать?

- Находить баги до продакшена
- Безопасно рефакторить код
- Документировать ожидаемое поведение

## unittest (встроенный)

```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
```

## Основные assert-методы

| Метод | Проверяет |
|-------|-----------|
| `assertEqual(a, b)` | a == b |
| `assertNotEqual(a, b)` | a != b |
| `assertTrue(x)` | x is True |
| `assertFalse(x)` | x is False |
| `assertIs(a, b)` | a is b |
| `assertIsNone(x)` | x is None |
| `assertIn(a, b)` | a in b |
| `assertRaises(Error)` | вызывает ошибку |
| `assertAlmostEqual(a, b)` | a ≈ b |

## setUp и tearDown

```python
class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")

    def tearDown(self):
        self.db.close()

    def test_insert(self):
        self.db.insert("test")
        self.assertEqual(self.db.count(), 1)
```

## pytest (рекомендуется)

```bash
pip install pytest
```

```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2
```

```bash
pytest test_math.py -v
```

## Фикстуры pytest

```python
import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_sum(sample_list):
    assert sum(sample_list) == 15

def test_len(sample_list):
    assert len(sample_list) == 5
```

## Параметризация

```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

## Запуск тестов

```bash
pytest                    # все тесты
pytest test_file.py       # конкретный файл
pytest -v                 # подробно
pytest -k "test_add"      # по имени
pytest --tb=short         # короткий traceback
```
