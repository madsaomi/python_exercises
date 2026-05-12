"""
06 — Базы данных и SQL: Практические упражнения

Все упражнения используют SQLite (встроенный в Python).
Запустите для проверки: python exercises.py
"""
import sqlite3


def setup_db():
    """Создаёт тестовую БД в памяти."""
    conn = sqlite3.connect(":memory:")
    conn.execute("""
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT,
            salary INTEGER,
            manager_id INTEGER
        )
    """)
    employees = [
        (1, "Alice", "IT", 80000, None),
        (2, "Bob", "IT", 90000, 1),
        (3, "Carol", "HR", 60000, 1),
        (4, "Dave", "IT", 75000, 2),
        (5, "Eve", "HR", 65000, 3),
        (6, "Frank", "Sales", 70000, 1),
        (7, "Grace", "Sales", 55000, 6),
        (8, "Hank", "IT", 95000, 2),
    ]
    conn.executemany("INSERT INTO employees VALUES (?,?,?,?,?)", employees)
    conn.commit()
    return conn


# ============================================================
# Упражнение 1: Средняя зарплата по отделам
# ============================================================
# Напишите SQL-запрос, который возвращает среднюю зарплату
# по каждому отделу, отсортированную по убыванию.
#
# Ожидаемый результат:
#   [('IT', 85000.0), ('Sales', 62500.0), ('HR', 62500.0)]

def avg_salary_by_dept(conn):
    query = """
    -- Ваш SQL здесь
    """
    return conn.execute(query).fetchall()


# ============================================================
# Упражнение 2: Топ-3 по зарплате
# ============================================================
# Найдите 3 сотрудников с наибольшей зарплатой.
# Верните имя и зарплату.
#
# Ожидаемый результат:
#   [('Hank', 95000), ('Bob', 90000), ('Alice', 80000)]

def top_3_salaries(conn):
    query = """
    -- Ваш SQL здесь
    """
    return conn.execute(query).fetchall()


# ============================================================
# Упражнение 3: Сотрудники с зарплатой выше средней по отделу
# ============================================================
# Найдите сотрудников, чья зарплата выше средней по их отделу.
#
# Ожидаемый результат (имя, отдел, зарплата):
#   [('Bob', 'IT', 90000), ('Hank', 'IT', 95000),
#    ('Eve', 'HR', 65000), ('Frank', 'Sales', 70000)]

def above_avg_in_dept(conn):
    query = """
    -- Ваш SQL здесь
    """
    return conn.execute(query).fetchall()


# ============================================================
# Упражнение 4: Количество подчинённых
# ============================================================
# Для каждого сотрудника найдите количество прямых подчинённых.
# Покажите только тех, у кого есть хотя бы 1 подчинённый.
#
# Ожидаемый результат:
#   [('Alice', 3), ('Bob', 2), ('Carol', 1), ('Frank', 1)]

def count_subordinates(conn):
    query = """
    -- Ваш SQL здесь
    """
    return conn.execute(query).fetchall()


# ============================================================
# Упражнение 5: CRUD-операции через Python
# ============================================================
# Реализуйте класс EmployeeDB с методами:
# - add(name, dept, salary) → id
# - get(id) → dict или None
# - update_salary(id, new_salary) → bool
# - delete(id) → bool
# - list_all() → list[dict]

class EmployeeDB:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute("""
            CREATE TABLE employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT,
                salary INTEGER
            )
        """)

    # Ваш код здесь


# ============================================================
# Тесты
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("Тестирование упражнений 06_databases_and_sql")
    print("=" * 50)

    conn = setup_db()

    # Тест 2
    print("\n--- Упражнение 2: top_3_salaries ---")
    result = top_3_salaries(conn)
    assert result == [("Hank", 95000), ("Bob", 90000), ("Alice", 80000)], f"Got: {result}"
    print("✅ Все тесты пройдены!")

    conn.close()

    print("\n" + "=" * 50)
    print("🎉 Все упражнения выполнены верно!")
    print("=" * 50)
