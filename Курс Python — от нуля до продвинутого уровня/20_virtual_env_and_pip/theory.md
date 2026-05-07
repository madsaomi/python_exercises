# 📘 Тема 20: Виртуальные окружения и pip

## Зачем нужны виртуальные окружения?

- Изоляция зависимостей между проектами
- Разные версии библиотек для разных проектов
- Чистый системный Python
- Воспроизводимость окружения

## Создание виртуального окружения

```bash
# Создать
python -m venv myenv

# Активировать (Windows)
myenv\Scripts\activate

# Активировать (Linux/Mac)
source myenv/bin/activate

# Деактивировать
deactivate
```

## pip — менеджер пакетов

```bash
# Установить пакет
pip install requests

# Конкретная версия
pip install requests==2.31.0

# Обновить
pip install --upgrade requests

# Удалить
pip uninstall requests

# Список установленных
pip list

# Информация о пакете
pip show requests

# Поиск пакетов
pip search requests  # (может быть отключён)
```

## requirements.txt

```bash
# Создать файл зависимостей
pip freeze > requirements.txt

# Установить из файла
pip install -r requirements.txt
```

Пример `requirements.txt`:
```
requests==2.31.0
flask>=3.0.0
pytest~=7.4.0
numpy
```

## Операторы версий

| Оператор | Значение |
|----------|----------|
| `==2.31.0` | Точная версия |
| `>=2.31.0` | Не ниже |
| `<=2.31.0` | Не выше |
| `~=2.31.0` | Совместимая (2.31.x) |
| `!=2.0.0` | Исключить версию |

## Популярные библиотеки Python

| Библиотека | Назначение |
|-----------|-----------|
| `requests` | HTTP-запросы |
| `flask` | Веб-фреймворк (лёгкий) |
| `fastapi` | Современный API-фреймворк |
| `sqlalchemy` | ORM для баз данных |
| `pytest` | Тестирование |
| `black` | Форматирование кода |
| `pylint` | Линтер |
| `numpy` | Математика/массивы |
| `pandas` | Анализ данных |
| `matplotlib` | Графики |
| `pillow` | Работа с изображениями |
| `beautifulsoup4` | Парсинг HTML |

## pyproject.toml (современный подход)

```toml
[project]
name = "my-project"
version = "1.0.0"
requires-python = ">=3.8"
dependencies = [
    "requests>=2.31.0",
    "flask>=3.0.0",
]

[project.optional-dependencies]
dev = ["pytest", "black"]
```

## Рекомендации

1. **Всегда** используйте виртуальное окружение
2. **Никогда** не устанавливайте пакеты в системный Python
3. Фиксируйте версии в `requirements.txt`
4. Добавляйте `venv/` в `.gitignore`
5. Документируйте зависимости
