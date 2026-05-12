# 06 — Базы данных и SQL: Задачи-ловушки

> ⚠️ Попробуйте предсказать результат SQL-запросов **БЕЗ выполнения**.

---

## Задача 1: NULL в сравнениях

```sql
SELECT * FROM users WHERE age != 25;
```

Таблица `users`:
| id | name | age |
|----|------|-----|
| 1 | Alice | 25 |
| 2 | Bob | 30 |
| 3 | Carol | NULL |

<details>
<summary>🔍 Какие строки вернёт запрос?</summary>

Только **Bob** (id=2).

**Объяснение:** `NULL != 25` не возвращает TRUE — возвращает **NULL** (unknown). Для фильтрации NULL нужен `IS NOT NULL`:
```sql
SELECT * FROM users WHERE age != 25 OR age IS NULL;
```
</details>

---

## Задача 2: COUNT и NULL

```sql
SELECT COUNT(*), COUNT(age), COUNT(DISTINCT age)
FROM users;
```

Таблица: Alice(25), Bob(30), Carol(NULL), Dave(25).

<details>
<summary>🔍 Что вернёт запрос?</summary>

```
4, 3, 2
```

**Объяснение:** `COUNT(*)` считает все строки (включая NULL). `COUNT(age)` пропускает NULL. `COUNT(DISTINCT age)` — уникальные не-NULL значения (25, 30).
</details>

---

## Задача 3: GROUP BY ловушка

```sql
SELECT department, name, MAX(salary)
FROM employees
GROUP BY department;
```

<details>
<summary>🔍 Что произойдёт?</summary>

**Ошибка** (в строгом SQL-режиме) или **непредсказуемый `name`** (в MySQL).

**Объяснение:** `name` не в GROUP BY и не в агрегатной функции. SQL не знает, какое имя показать для группы. Правильно:
```sql
SELECT department, MAX(salary) FROM employees GROUP BY department;
```
</details>

---

## Задача 4: LEFT JOIN и WHERE

```sql
-- Вариант A
SELECT * FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.amount > 100;

-- Вариант B
SELECT * FROM users u
LEFT JOIN orders o ON u.id = o.user_id AND o.amount > 100;
```

<details>
<summary>🔍 В чём разница?</summary>

**Вариант A:** LEFT JOIN превращается в INNER JOIN! WHERE фильтрует NULL-строки (пользователи без заказов).

**Вариант B:** Сохраняет LEFT JOIN. Пользователи без заказов >100 остаются (с NULL в столбцах orders).

**Правило:** Фильтры по правой таблице в LEFT JOIN ставьте в ON, а не в WHERE.
</details>

---

## Задача 5: Порядок операций

```sql
SELECT department, AVG(salary) as avg_sal
FROM employees
WHERE avg_sal > 50000
GROUP BY department;
```

<details>
<summary>🔍 Что произойдёт?</summary>

**Ошибка!** `avg_sal` — алиас, созданный в SELECT. WHERE выполняется ДО SELECT.

**Правильно:**
```sql
SELECT department, AVG(salary) as avg_sal
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

Порядок выполнения: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
</details>

---

## Задача 6: DISTINCT и ORDER BY

```sql
SELECT DISTINCT department FROM employees ORDER BY salary;
```

<details>
<summary>🔍 Что произойдёт?</summary>

**Ошибка** (в PostgreSQL и строгом SQL). `salary` не в SELECT DISTINCT.

**Объяснение:** DISTINCT сворачивает строки — непонятно, по какому salary сортировать. Правильно:
```sql
SELECT DISTINCT department FROM employees ORDER BY department;
```
</details>

---

## Задача 7: UPDATE с подзапросом

```python
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t (id INT, val INT)")
conn.execute("INSERT INTO t VALUES (1, 10), (2, 20), (3, 30)")

conn.execute("UPDATE t SET val = val * 2 WHERE id IN (SELECT id FROM t WHERE val > 15)")
result = conn.execute("SELECT * FROM t").fetchall()
print(result)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
[(1, 10), (2, 40), (3, 60)]
```

**Объяснение:** Подзапрос находит id=2 (val=20) и id=3 (val=30). UPDATE удваивает их значения. id=1 не затронут.
</details>

---

## Задача 8: Python и SQLite — параметры

```python
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users (name TEXT, age INT)")
conn.execute("INSERT INTO users VALUES ('Alice', 25)")

# Способ 1
name = "Alice"
row = conn.execute(f"SELECT * FROM users WHERE name = '{name}'").fetchone()
print(row)

# Способ 2 (безопасный)
row = conn.execute("SELECT * FROM users WHERE name = ?", (name,)).fetchone()
print(row)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
('Alice', 25)
('Alice', 25)
```

**Объяснение:** Оба работают, но Способ 1 уязвим к SQL-инъекции! Если `name = "'; DROP TABLE users; --"` — таблица будет удалена. Всегда используйте Способ 2.
</details>

---

## Задача 9: COALESCE

```sql
SELECT COALESCE(NULL, NULL, 'default', 'other');
```

<details>
<summary>🔍 Что вернёт?</summary>

```
'default'
```

**Объяснение:** `COALESCE` возвращает первый не-NULL аргумент. Пропускает NULL, NULL и возвращает 'default'.
</details>

---

## Задача 10: Самосоединение (Self JOIN)

```sql
-- Найти сотрудников, чей руководитель тоже есть в таблице
SELECT e.name as employee, m.name as manager
FROM employees e
JOIN employees m ON e.manager_id = m.id;
```

Таблица:
| id | name | manager_id |
|----|------|-----------|
| 1 | CEO | NULL |
| 2 | Alice | 1 |
| 3 | Bob | 1 |
| 4 | Carol | 2 |

<details>
<summary>🔍 Какой результат?</summary>

```
Alice | CEO
Bob   | CEO
Carol | Alice
```

**Объяснение:** Self JOIN — таблица соединяется сама с собой. CEO (manager_id=NULL) не попадает в результат INNER JOIN.
</details>
