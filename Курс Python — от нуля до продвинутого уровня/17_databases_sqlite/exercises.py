"""
============================================================
  ТЕМА 17: Базы данных SQLite — Упражнения
============================================================
  Каждое задание содержит подробное описание, примеры
  ожидаемого результата и подсказки.
============================================================
"""
import sqlite3

# ============================================================
# Задание 1: Создание базы данных и таблицы
# ============================================================
# Создайте БД "school.db" с таблицей students:
#   id (INTEGER PRIMARY KEY AUTOINCREMENT)
#   name (TEXT NOT NULL)
#   age (INTEGER)
#   grade (REAL)
# Вставьте 5 студентов.
#
# Ожидаемый результат:
#   create_db()
#   # Таблица students создана.
#   # Добавлено 5 студентов.
#
# Подсказка:
#   conn = sqlite3.connect("school.db")
#   cursor = conn.cursor()
#   cursor.execute("""CREATE TABLE IF NOT EXISTS students (...)""")
#   cursor.executemany("INSERT INTO students ...", data)
#   conn.commit()
#   conn.close()

# Ваш код здесь:


# ============================================================
# Задание 2: CRUD-операции
# ============================================================
# Напишите функции для работы с таблицей students:
#   add_student(name, age, grade)
#   get_all_students() → список кортежей
#   get_student(student_id) → один кортеж или None
#   update_grade(student_id, new_grade)
#   delete_student(student_id)
#
# Ожидаемый результат:
#   add_student("Глеб", 19, 4.2)
#   print(get_all_students())
#   → [(1, "Алиса", 20, 4.8), (2, "Борис", 22, 3.5), ...]
#
#   update_grade(2, 4.0)
#   print(get_student(2))  → (2, "Борис", 22, 4.0)
#
#   delete_student(3)
#   print(len(get_all_students()))  → на 1 меньше
#
# Подсказка: используйте параметризованные запросы (?, ?)

# Ваш код здесь:


# ============================================================
# Задание 3: Выборка с условиями
# ============================================================
# Напишите функции:
#   get_excellent(min_grade=4.5) → отличники
#   get_by_age_range(min_age, max_age) → по диапазону
#   get_sorted(field="name", desc=False) → отсортированные
#   count_students() → количество студентов
#
# Ожидаемый результат:
#   print(get_excellent())
#   → [(1, "Алиса", 20, 4.8), (4, "Дана", 21, 5.0)]
#
#   print(get_by_age_range(19, 21))
#   → [(1, "Алиса", 20, ...), ...]
#
#   print(count_students())  → 5
#
# Подсказка:
#   cursor.execute("SELECT * FROM students WHERE grade >= ?", (min_grade,))
#   ORDER BY {field} {"DESC" if desc else "ASC"}

# Ваш код здесь:


# ============================================================
# Задание 4: Агрегатные функции
# ============================================================
# Напишите функцию student_stats(), которая возвращает
# словарь со статистикой:
#   count, avg_grade, min_grade, max_grade, avg_age
#
# Ожидаемый результат:
#   stats = student_stats()
#   print(stats)
#   → {"count": 5, "avg_grade": 4.1, "min_grade": 3.2,
#      "max_grade": 5.0, "avg_age": 20.6}
#
# Подсказка:
#   SELECT COUNT(*), AVG(grade), MIN(grade), MAX(grade), AVG(age)
#   FROM students

# Ваш код здесь:


# ============================================================
# Задание 5: Несколько таблиц и JOIN
# ============================================================
# Создайте таблицу courses (id, title, teacher).
# Создайте связующую таблицу enrollments (student_id, course_id).
# Напишите функцию get_student_courses(student_id),
# которая возвращает список курсов студента.
#
# Ожидаемый результат:
#   # Алиса записана на Python и Математику
#   courses = get_student_courses(1)
#   print(courses)  → [("Python", "Иванов"), ("Математика", "Петрова")]
#
# Подсказка:
#   SELECT c.title, c.teacher
#   FROM courses c
#   JOIN enrollments e ON c.id = e.course_id
#   WHERE e.student_id = ?

# Ваш код здесь:


# ============================================================
# Задание 6: Контекстный менеджер для БД
# ============================================================
# Создайте класс Database, который:
#   - В __enter__ открывает соединение
#   - В __exit__ делает commit (или rollback при ошибке)
#   - Метод execute(sql, params) — выполняет запрос
#   - Метод fetchall(sql, params) — возвращает результат
#
# Ожидаемый результат:
#   with Database("school.db") as db:
#       db.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
#                  (None, "Ева", 18, 4.9))
#       students = db.fetchall("SELECT * FROM students")
#       print(len(students))
#   # Автоматически commit + close
#
# Подсказка:
#   def __exit__(self, exc_type, exc_val, exc_tb):
#       if exc_type: self.conn.rollback()
#       else: self.conn.commit()
#       self.conn.close()

# Ваш код здесь:


# ============================================================
# Задание 7: Поиск и фильтрация
# ============================================================
# Напишите функцию search_students(query), которая ищет
# студентов по имени (частичное совпадение, LIKE).
# Функция format_table(rows) — выводит данные как таблицу.
#
# Ожидаемый результат:
#   results = search_students("ал")
#   format_table(results)
#   # +----+--------+-----+-------+
#   # | ID | Имя    | Возр| Оценка|
#   # +----+--------+-----+-------+
#   # |  1 | Алиса  |  20 |  4.80 |
#   # +----+--------+-----+-------+
#
# Подсказка:
#   WHERE name LIKE ?    с параметром f"%{query}%"

# Ваш код здесь:


# ============================================================
# Задание 8: Миграция и изменение схемы
# ============================================================
# Напишите функцию add_column_if_not_exists(table, column, type_),
# которая добавляет столбец, если его ещё нет.
# Добавьте столбец email TEXT в таблицу students.
#
# Ожидаемый результат:
#   add_column_if_not_exists("students", "email", "TEXT")
#   # Столбец 'email' добавлен в таблицу 'students'
#
#   add_column_if_not_exists("students", "email", "TEXT")
#   # Столбец 'email' уже существует
#
# Подсказка:
#   PRAGMA table_info(students) — информация о столбцах
#   ALTER TABLE students ADD COLUMN email TEXT

# Ваш код здесь:


# ============================================================
# Задание 9: Импорт/экспорт CSV ↔ SQLite
# ============================================================
# Напишите функции:
#   csv_to_sqlite(csv_path, db_path, table_name)
#   sqlite_to_csv(db_path, table_name, csv_path)
#
# Ожидаемый результат:
#   csv_to_sqlite("students.csv", "school.db", "students_import")
#   # Импортировано 10 записей из CSV в таблицу students_import
#
#   sqlite_to_csv("school.db", "students", "export.csv")
#   # Экспортировано 5 записей в export.csv
#
# Подсказка:
#   import csv
#   reader = csv.DictReader(f)
#   columns = reader.fieldnames

import csv

# Ваш код здесь:


# ============================================================
# Задание 10: Мини-приложение — Телефонная книга
# ============================================================
# Создайте класс PhoneBook, работающий с SQLite:
#   add(name, phone, email=None) → добавить контакт
#   search(query) → найти по имени или телефону
#   update(contact_id, **kwargs) → обновить поля
#   delete(contact_id) → удалить
#   show_all() → вывести все контакты
#   export_csv(path) → экспорт в CSV
#
# Ожидаемый результат:
#   pb = PhoneBook("contacts.db")
#   pb.add("Алиса", "+79991234567", "alice@mail.ru")
#   pb.add("Борис", "+79997654321")
#   pb.show_all()
#   # 1. Алиса | +79991234567 | alice@mail.ru
#   # 2. Борис | +79997654321 | —
#
#   pb.search("Алиса")
#   # 1. Алиса | +79991234567 | alice@mail.ru
#
# Подсказка: CREATE TABLE contacts (id, name, phone, email)

# Ваш код здесь:
