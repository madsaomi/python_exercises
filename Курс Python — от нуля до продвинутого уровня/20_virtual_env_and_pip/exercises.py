"""
============================================================
  ТЕМА 20: Виртуальные окружения и pip — Упражнения
============================================================
  Каждое задание содержит подробное описание, примеры
  ожидаемого результата и подсказки.
  Эти задания выполняются преимущественно в ТЕРМИНАЛЕ.
============================================================
"""

# ============================================================
# Задание 1: Создание виртуального окружения
# ============================================================
# Создайте виртуальное окружение "myenv" и активируйте его.
# Проверьте, что Python запускается из окружения.
#
# Команды в терминале:
#   python -m venv myenv
#
#   # Активация (Windows):
#   myenv\Scripts\activate
#
#   # Активация (Linux/Mac):
#   source myenv/bin/activate
#
#   # Проверка:
#   which python   (Linux/Mac)
#   where python   (Windows)
#   → .../myenv/bin/python  или  ...\myenv\Scripts\python.exe
#
#   python --version  → Python 3.12.x
#
#   # Деактивация:
#   deactivate
#
# Задание: напишите функцию, которая выводит путь к Python:

import sys

def show_python_info():
    """Выводит информацию о текущем интерпретаторе Python."""
    print(f"Версия Python: {sys.version}")
    print(f"Путь к Python: {sys.executable}")
    print(f"Путь поиска модулей:")
    for p in sys.path[:5]:
        print(f"  - {p}")

# show_python_info()


# ============================================================
# Задание 2: Установка пакетов с pip
# ============================================================
# Установите несколько пакетов и проверьте их.
#
# Команды в терминале:
#   pip install requests
#   pip install colorama
#   pip install python-dotenv
#
#   # Проверка установленных пакетов:
#   pip list
#   pip show requests
#
# Ожидаемый результат:
#   pip show requests
#   # Name: requests
#   # Version: 2.31.0
#   # Summary: Python HTTP for Humans.
#   # ...
#
# Задание: напишите функцию, проверяющую наличие пакета:

import importlib

def check_package(name):
    """Проверяет, установлен ли пакет."""
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "N/A")
        print(f"✅ {name} установлен (версия: {version})")
        return True
    except ImportError:
        print(f"❌ {name} НЕ установлен")
        return False

# Тесты:
# check_package("requests")    → ✅ requests (2.31.0)
# check_package("numpy")       → ❌ numpy НЕ установлен
# check_package("colorama")    → ✅ colorama (0.4.6)


# ============================================================
# Задание 3: requirements.txt
# ============================================================
# Создайте requirements.txt и научитесь управлять зависимостями.
#
# Команды:
#   # Сохранить текущие зависимости:
#   pip freeze > requirements.txt
#
#   # Установить из файла:
#   pip install -r requirements.txt
#
#   # Обновить пакет:
#   pip install --upgrade requests
#
# Задание: напишите функцию, которая генерирует
# requirements.txt программно:

import subprocess

def generate_requirements(output_path="requirements.txt"):
    """Генерирует requirements.txt из текущего окружения."""
    result = subprocess.run(
        [sys.executable, "-m", "pip", "freeze"],
        capture_output=True, text=True
    )
    packages = result.stdout.strip().split("\n")
    
    with open(output_path, "w") as f:
        f.write(result.stdout)
    
    print(f"Сохранено {len(packages)} пакетов в {output_path}")
    for pkg in packages[:5]:
        print(f"  {pkg}")
    if len(packages) > 5:
        print(f"  ... и ещё {len(packages) - 5}")
    
    return packages

# generate_requirements()


# ============================================================
# Задание 4: Версионирование пакетов
# ============================================================
# Изучите синтаксис указания версий в requirements.txt:
#   requests==2.31.0     — точная версия
#   requests>=2.28.0     — минимальная версия
#   requests~=2.31       — совместимая (2.31.x)
#   requests>=2.28,<3.0  — диапазон
#
# Задание: напишите функцию, парсящую requirements.txt:

def parse_requirements(path="requirements.txt"):
    """Парсит requirements.txt и возвращает список словарей."""
    requirements = []
    try:
        with open(path, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                # Разделяем имя и версию
                for op in ["==", ">=", "<=", "~=", "!="]:
                    if op in line:
                        name, version = line.split(op, 1)
                        requirements.append({
                            "name": name.strip(),
                            "operator": op,
                            "version": version.strip()
                        })
                        break
                else:
                    requirements.append({
                        "name": line, "operator": None, "version": None
                    })
    except FileNotFoundError:
        print(f"Файл {path} не найден")
    return requirements

# Ожидаемый результат:
#   reqs = parse_requirements()
#   print(reqs[0])
#   → {"name": "requests", "operator": "==", "version": "2.31.0"}


# ============================================================
# Задание 5: Работа с .env файлами
# ============================================================
# Создайте файл .env с секретными данными.
# Используйте python-dotenv для загрузки.
#
# Содержимое .env:
#   API_KEY=sk-1234567890
#   DATABASE_URL=sqlite:///mydb.db
#   DEBUG=true
#   SECRET_KEY=super_secret_key
#
# Задание: напишите свой простой загрузчик .env:

import os

def load_env(path=".env"):
    """Загружает переменные из .env файла в os.environ."""
    loaded = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    os.environ[key] = value
                    loaded[key] = value
        print(f"Загружено {len(loaded)} переменных из {path}")
    except FileNotFoundError:
        print(f"Файл {path} не найден")
    return loaded

# Ожидаемый результат:
#   load_env()
#   # Загружено 4 переменных из .env
#   print(os.environ.get("API_KEY"))  → "sk-1234567890"
#   print(os.environ.get("DEBUG"))    → "true"


# ============================================================
# Задание 6: Структура проекта
# ============================================================
# Создайте правильную структуру Python-проекта:
#
#   my_project/
#   ├── README.md
#   ├── requirements.txt
#   ├── .env
#   ├── .gitignore
#   ├── setup.py (или pyproject.toml)
#   ├── src/
#   │   └── my_package/
#   │       ├── __init__.py
#   │       ├── main.py
#   │       └── utils.py
#   ├── tests/
#   │   ├── __init__.py
#   │   └── test_main.py
#   └── docs/
#
# Задание: напишите функцию, создающую эту структуру:

from pathlib import Path

def create_project(name, base_path="."):
    """Создаёт структуру Python-проекта."""
    root = Path(base_path) / name
    
    # Директории
    dirs = [
        root / "src" / name.replace("-", "_"),
        root / "tests",
        root / "docs",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    
    # Файлы
    files = {
        root / "README.md": f"# {name}\n\nОписание проекта.\n",
        root / "requirements.txt": "# Зависимости проекта\n",
        root / ".gitignore": "myenv/\n__pycache__/\n*.pyc\n.env\n*.egg-info/\n",
        root / ".env": "# Секретные переменные\nDEBUG=true\n",
        root / "src" / name.replace("-", "_") / "__init__.py": "",
        root / "src" / name.replace("-", "_") / "main.py":
            'def main():\n    print("Hello, World!")\n\n'
            'if __name__ == "__main__":\n    main()\n',
        root / "tests" / "__init__.py": "",
        root / "tests" / "test_main.py":
            "import unittest\n\nclass TestMain(unittest.TestCase):\n"
            "    def test_placeholder(self):\n"
            "        self.assertTrue(True)\n",
    }
    for path, content in files.items():
        path.write_text(content, encoding="utf-8")
    
    print(f"Проект '{name}' создан в {root.resolve()}")
    return root

# Ожидаемый результат:
#   create_project("my-awesome-app")
#   # Проект 'my-awesome-app' создан в /path/to/my-awesome-app


# ============================================================
# Задание 7: .gitignore для Python
# ============================================================
# Напишите функцию generate_gitignore(), которая создаёт
# полноценный .gitignore для Python-проекта.
#
# Ожидаемый результат:
#   generate_gitignore()
#   # Файл .gitignore создан (15 правил)
#
# Подсказка: основные исключения для Python:

def generate_gitignore(path=".gitignore"):
    """Генерирует .gitignore для Python-проекта."""
    rules = [
        "# Виртуальные окружения",
        "venv/", "myenv/", ".env/", "env/",
        "",
        "# Python",
        "__pycache__/", "*.py[cod]", "*.pyo",
        "*.egg-info/", "dist/", "build/",
        "",
        "# IDE",
        ".idea/", ".vscode/", "*.swp",
        "",
        "# Секреты",
        ".env",
        "",
        "# ОС",
        ".DS_Store", "Thumbs.db",
        "",
        "# Тестирование",
        ".coverage", "htmlcov/", ".pytest_cache/",
    ]
    with open(path, "w") as f:
        f.write("\n".join(rules) + "\n")
    actual_rules = [r for r in rules if r and not r.startswith("#")]
    print(f"Файл {path} создан ({len(actual_rules)} правил)")

# generate_gitignore()


# ============================================================
# Задание 8: Проверка устаревших пакетов
# ============================================================
# Напишите функцию check_outdated(), которая проверяет,
# есть ли обновления для установленных пакетов.
#
# Ожидаемый результат:
#   check_outdated()
#   # Устаревшие пакеты:
#   # requests   2.28.0 → 2.31.0
#   # colorama   0.4.5  → 0.4.6
#   # Всё актуально: 15 из 17
#
# Подсказка: pip list --outdated --format=json

def check_outdated():
    """Проверяет устаревшие пакеты."""
    result = subprocess.run(
        [sys.executable, "-m", "pip", "list",
         "--outdated", "--format=json"],
        capture_output=True, text=True
    )
    try:
        import json
        packages = json.loads(result.stdout)
        if not packages:
            print("✅ Все пакеты актуальны!")
        else:
            print(f"⚠️  Устаревшие пакеты ({len(packages)}):")
            for pkg in packages:
                print(f"  {pkg['name']:20s} "
                      f"{pkg['version']:10s} → {pkg['latest_version']}")
    except Exception as e:
        print(f"Ошибка: {e}")

# check_outdated()


# ============================================================
# Задание 9: pyproject.toml
# ============================================================
# Создайте pyproject.toml — современную замену setup.py.
# Напишите функцию, генерирующую его.
#
# Ожидаемый результат (содержимое pyproject.toml):
#   [build-system]
#   requires = ["setuptools>=68.0"]
#   build-backend = "setuptools.backends._legacy:_Backend"
#
#   [project]
#   name = "my-package"
#   version = "1.0.0"
#   ...

def generate_pyproject(name, version="0.1.0", author="Developer",
                       description="My Python package"):
    """Генерирует pyproject.toml."""
    content = f'''[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{name}"
version = "{version}"
description = "{description}"
authors = [{{name = "{author}"}}]
readme = "README.md"
requires-python = ">=3.10"
license = {{text = "MIT"}}

dependencies = [
    "requests>=2.28.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "coverage>=7.0",
]
'''
    with open("pyproject.toml", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"pyproject.toml создан для '{name}' v{version}")

# generate_pyproject("my-awesome-app", author="Алиса")


# ============================================================
# Задание 10: Скрипт автоматизации проекта
# ============================================================
# Напишите полный скрипт, который:
# 1. Создаёт виртуальное окружение
# 2. Устанавливает зависимости из requirements.txt
# 3. Запускает тесты
# 4. Генерирует отчёт
#
# Ожидаемый результат:
#   python setup_project.py
#   # [1/4] Создание виртуального окружения...  ✅
#   # [2/4] Установка зависимостей...           ✅ (12 пакетов)
#   # [3/4] Запуск тестов...                    ✅ (5 passed)
#   # [4/4] Генерация отчёта...                 ✅
#   # Проект готов к работе!
#
# Подсказка: subprocess.run() для выполнения команд

def setup_project(project_dir="."):
    """Автоматическая настройка Python-проекта."""
    import subprocess
    
    steps = [
        ("Создание виртуального окружения",
         [sys.executable, "-m", "venv", "myenv"]),
        ("Установка зависимостей",
         [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]),
        ("Запуск тестов",
         [sys.executable, "-m", "pytest", "tests/", "-v"]),
    ]
    
    for i, (name, cmd) in enumerate(steps, 1):
        print(f"[{i}/{len(steps)}] {name}...", end=" ")
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True,
                cwd=project_dir, timeout=120
            )
            if result.returncode == 0:
                print("✅")
            else:
                print(f"❌\n  Ошибка: {result.stderr[:200]}")
        except FileNotFoundError:
            print("⏭️  Пропущено (файл не найден)")
        except subprocess.TimeoutExpired:
            print("⏱️  Таймаут!")
    
    print("\n🎉 Настройка завершена!")

# setup_project()
