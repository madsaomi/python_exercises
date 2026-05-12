# 06 — Базы данных и SQL: Теоретические вопросы

---

## Вопрос 1: Какие типы JOIN существуют?

<details>
<summary>💡 Ответ</summary>

| JOIN | Описание |
|------|----------|
| `INNER JOIN` | Только совпадающие строки из обеих таблиц |
| `LEFT JOIN` | Все строки из левой + совпадения из правой (NULL если нет) |
| `RIGHT JOIN` | Все строки из правой + совпадения из левой |
| `FULL OUTER JOIN` | Все строки из обеих таблиц |
| `CROSS JOIN` | Декартово произведение (каждая строка с каждой) |

```sql
-- Все заказы с именами клиентов (только у кого есть заказы)
SELECT * FROM orders INNER JOIN customers ON orders.customer_id = customers.id;

-- Все клиенты, даже без заказов
SELECT * FROM customers LEFT JOIN orders ON customers.id = orders.customer_id;
```
</details>

---

## Вопрос 2: В чём разница между WHERE и HAVING?

<details>
<summary>💡 Ответ</summary>

- `WHERE` — фильтрует **строки** до группировки
- `HAVING` — фильтрует **группы** после `GROUP BY`

```sql
-- WHERE: фильтрация до группировки
SELECT department, COUNT(*) 
FROM employees 
WHERE salary > 50000        -- фильтрует отдельные строки
GROUP BY department;

-- HAVING: фильтрация после группировки
SELECT department, COUNT(*) as cnt
FROM employees 
GROUP BY department
HAVING COUNT(*) > 5;         -- фильтрует группы
```
</details>

---

## Вопрос 3: Что такое индексы и зачем они нужны?

<details>
<summary>💡 Ответ</summary>

**Индекс** — структура данных (обычно B-tree), ускоряющая поиск. Аналогия — оглавление в книге.

**Плюсы:** Ускоряет SELECT, WHERE, JOIN, ORDER BY.  
**Минусы:** Замедляет INSERT/UPDATE/DELETE, занимает место.

```sql
CREATE INDEX idx_email ON users(email);

-- Этот запрос теперь быстрый:
SELECT * FROM users WHERE email = 'user@mail.com';
```

**Когда НЕ нужен индекс:**
- Маленькая таблица (< 1000 строк)
- Столбец с низкой кардинальностью (пол: M/F)
- Таблица с частыми INSERT/UPDATE
</details>

---

## Вопрос 4: Что такое ACID?

<details>
<summary>💡 Ответ</summary>

**ACID** — свойства транзакций:

| Свойство | Описание |
|----------|----------|
| **A**tomicity (атомарность) | Всё или ничего — транзакция полностью выполняется или полностью откатывается |
| **C**onsistency (согласованность) | БД переходит из одного корректного состояния в другое |
| **I**solation (изоляция) | Параллельные транзакции не влияют друг на друга |
| **D**urability (долговечность) | Результат подтверждённой транзакции сохраняется даже при сбое |

```sql
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;  -- обе операции или ни одной
```
</details>

---

## Вопрос 5: Что такое нормализация?

<details>
<summary>💡 Ответ</summary>

**Нормализация** — процесс организации данных для уменьшения дублирования.

- **1NF:** Атомарные значения (нет списков в ячейках)
- **2NF:** 1NF + нет частичных зависимостей (каждый столбец зависит от ВСЕГО ключа)
- **3NF:** 2NF + нет транзитивных зависимостей (столбцы не зависят друг от друга)

**Денормализация** — осознанное добавление дублирования для ускорения чтения.
</details>

---

## Вопрос 6: Что такое N+1 проблема?

<details>
<summary>💡 Ответ</summary>

**N+1** — проблема ORM, когда для N объектов выполняется N+1 SQL-запросов.

```python
# ❌ N+1: 1 запрос для авторов + N запросов для книг
authors = Author.objects.all()          # 1 запрос
for author in authors:
    print(author.books.all())           # N запросов!

# ✅ Решение: select_related / prefetch_related (Django)
authors = Author.objects.prefetch_related('books').all()  # 2 запроса
```
</details>

---

## Вопрос 7: В чём разница между SQL и NoSQL?

<details>
<summary>💡 Ответ</summary>

| | SQL (реляционные) | NoSQL |
|--|-------------------|-------|
| Структура | Таблицы, строки, столбцы | Документы, ключ-значение, графы |
| Схема | Строгая (schema) | Гибкая (schemaless) |
| Масштабирование | Вертикальное | Горизонтальное |
| Транзакции | ACID | BASE (eventual consistency) |
| Примеры | PostgreSQL, MySQL, SQLite | MongoDB, Redis, Cassandra |

**SQL** — для структурированных данных, сложных запросов, транзакций.  
**NoSQL** — для высокой нагрузки, гибкой схемы, простых запросов.
</details>

---

## Вопрос 8: Что делает `EXPLAIN` в SQL?

<details>
<summary>💡 Ответ</summary>

`EXPLAIN` показывает план выполнения запроса — как БД будет искать данные.

```sql
EXPLAIN SELECT * FROM users WHERE email = 'test@mail.com';

-- Покажет:
-- - Используется ли индекс (INDEX SCAN vs FULL TABLE SCAN)
-- - Сколько строк будет просмотрено
-- - Стоимость операции
```

**Зачем:** Оптимизация медленных запросов. Если видите `Seq Scan` (Full Table Scan) — нужен индекс.
</details>

---

## Вопрос 9: Что такое SQL-инъекция и как защититься?

<details>
<summary>💡 Ответ</summary>

**SQL-инъекция** — атака через подстановку вредоносного SQL в пользовательский ввод.

```python
# ❌ Уязвимо!
query = f"SELECT * FROM users WHERE name = '{user_input}'"
# user_input = "'; DROP TABLE users; --"

# ✅ Параметризованные запросы
cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))

# ✅ ORM (Django)
User.objects.filter(name=user_input)
```

**Правило:** НИКОГДА не подставляйте пользовательский ввод в SQL через f-string!
</details>

---

## Вопрос 10: В чём разница между `DELETE`, `TRUNCATE` и `DROP`?

<details>
<summary>💡 Ответ</summary>

| Команда | Действие | Откат | Триггеры |
|---------|----------|-------|----------|
| `DELETE` | Удаляет строки (можно с WHERE) | Да | Да |
| `TRUNCATE` | Удаляет ВСЕ строки | Нет* | Нет |
| `DROP` | Удаляет таблицу целиком | Нет | Нет |

```sql
DELETE FROM users WHERE id = 1;  -- одну строку
TRUNCATE TABLE users;            -- все строки, таблица остаётся
DROP TABLE users;                -- таблица удалена полностью
```
</details>

---

## Вопрос 11: Что такое PRIMARY KEY и FOREIGN KEY?

<details>
<summary>💡 Ответ</summary>

- **PRIMARY KEY** — уникальный идентификатор строки. Не может быть NULL.
- **FOREIGN KEY** — ссылка на PRIMARY KEY другой таблицы. Обеспечивает целостность данных.

```sql
CREATE TABLE authors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);
```
</details>

---

## Вопрос 12: Что такое транзакция?

<details>
<summary>💡 Ответ</summary>

**Транзакция** — набор операций, который выполняется как единое целое.

```python
import sqlite3

conn = sqlite3.connect("bank.db")
try:
    conn.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
    conn.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
    conn.commit()    # всё прошло — сохраняем
except Exception:
    conn.rollback()  # ошибка — откатываем ВСЁ
```
</details>

---

## Вопрос 13: Что такое `GROUP BY`?

<details>
<summary>💡 Ответ</summary>

`GROUP BY` группирует строки с одинаковыми значениями для применения агрегатных функций:

```sql
SELECT department, COUNT(*) as count, AVG(salary) as avg_salary
FROM employees
GROUP BY department;
```

| department | count | avg_salary |
|------------|-------|------------|
| IT | 5 | 80000 |
| HR | 3 | 60000 |
</details>

---

## Вопрос 14: Что такое ORM?

<details>
<summary>💡 Ответ</summary>

**ORM (Object-Relational Mapping)** — технология, позволяющая работать с БД через объекты вместо SQL.

```python
# Чистый SQL
cursor.execute("SELECT * FROM users WHERE age > 18")

# ORM (Django)
users = User.objects.filter(age__gt=18)

# ORM (SQLAlchemy)
users = session.query(User).filter(User.age > 18).all()
```

**Плюсы:** Читаемость, безопасность (нет SQL-инъекций), миграции.  
**Минусы:** Производительность (сложные запросы), абстракция «протекает».
</details>

---

## Вопрос 15: В чём разница между `UNION` и `UNION ALL`?

<details>
<summary>💡 Ответ</summary>

- `UNION` — объединяет результаты и **удаляет дубликаты** (медленнее)
- `UNION ALL` — объединяет результаты **с дубликатами** (быстрее)

```sql
SELECT name FROM employees
UNION
SELECT name FROM contractors;     -- без дубликатов

SELECT name FROM employees
UNION ALL
SELECT name FROM contractors;     -- с дубликатами
```
</details>
