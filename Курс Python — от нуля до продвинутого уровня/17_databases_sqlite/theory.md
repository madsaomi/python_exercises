# 📘 Тема 17: Базы данных (SQLite)

## Подключение

```python
import sqlite3

conn = sqlite3.connect("database.db")  # создаст файл
cursor = conn.cursor()
```

## Создание таблицы

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
""")
conn.commit()
```

## CRUD-операции

```python
# CREATE — вставка
cursor.execute(
    "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
    ("Алиса", 25, "alice@mail.com")
)
conn.commit()

# Множественная вставка
users = [("Борис", 30, "boris@mail.com"), ("Виктор", 22, "vik@mail.com")]
cursor.executemany(
    "INSERT INTO users (name, age, email) VALUES (?, ?, ?)", users
)

# READ — чтение
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()       # все строки

cursor.execute("SELECT * FROM users WHERE age > ?", (25,))
row = cursor.fetchone()             # одна строка

# UPDATE — обновление
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Алиса"))

# DELETE — удаление
cursor.execute("DELETE FROM users WHERE name = ?", ("Борис",))
conn.commit()
```

## Context Manager

```python
with sqlite3.connect("database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())
# автоматический commit/rollback
```

## Row Factory

```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
row = cursor.fetchone()
print(row["name"])    # доступ по имени столбца
```

## Типы данных SQLite

| SQLite | Python |
|--------|--------|
| NULL | None |
| INTEGER | int |
| REAL | float |
| TEXT | str |
| BLOB | bytes |

## Важно!

- Всегда используйте `?` (параметризованные запросы) — защита от SQL-инъекций!
- Не забывайте `conn.commit()` после изменений
- Закрывайте соединение: `conn.close()` или используйте `with`
