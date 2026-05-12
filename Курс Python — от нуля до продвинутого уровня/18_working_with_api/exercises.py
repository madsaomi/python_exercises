"""
============================================================
  ТЕМА 18: Работа с API — Упражнения
============================================================
  Каждое задание содержит подробное описание, примеры
  ожидаемого результата и подсказки.
  Для выполнения нужен модуль requests: pip install requests
============================================================
"""

# ============================================================
# Задание 1: Первый GET-запрос
# ============================================================
# Сделайте GET-запрос к https://httpbin.org/get
# Выведите: статус-код, заголовки, тело ответа (JSON).
#
# Ожидаемый результат:
#   Статус: 200
#   Content-Type: application/json
#   IP: 123.45.67.89
#   User-Agent: python-requests/2.31.0
#
# Подсказка:
#   import requests
#   response = requests.get("https://httpbin.org/get")
#   print(response.status_code)
#   data = response.json()

# Ваш код здесь:


# ============================================================
# Задание 2: Параметры запроса
# ============================================================
# Сделайте GET-запрос к https://httpbin.org/get с параметрами:
#   name="Алиса", age=25, city="Москва"
# Проверьте, что параметры отображаются в ответе.
#
# Ожидаемый результат:
#   data = response.json()
#   print(data["args"])
#   → {"name": "Алиса", "age": "25", "city": "Москва"}
#
# Подсказка:
#   params = {"name": "Алиса", "age": 25, "city": "Москва"}
#   response = requests.get(url, params=params)

# Ваш код здесь:


# ============================================================
# Задание 3: POST-запрос
# ============================================================
# Отправьте POST-запрос на https://httpbin.org/post
# с JSON-телом: {"username": "admin", "password": "secret"}
# Выведите отправленные данные из ответа.
#
# Ожидаемый результат:
#   data = response.json()
#   print(data["json"])
#   → {"username": "admin", "password": "secret"}
#   print(response.status_code)  → 200
#
# Подсказка:
#   response = requests.post(url, json=payload)
#   # json= автоматически устанавливает Content-Type

# Ваш код здесь:


# ============================================================
# Задание 4: Погода через API
# ============================================================
# Используя бесплатный API wttr.in, получите погоду.
# Напишите функцию get_weather(city), которая
# возвращает словарь с температурой и описанием.
#
# Ожидаемый результат:
#   weather = get_weather("Moscow")
#   print(weather)
#   → {"city": "Moscow", "temp_c": "15", "description": "Partly cloudy"}
#
# Подсказка:
#   url = f"https://wttr.in/{city}?format=j1"
#   response = requests.get(url)
#   data = response.json()
#   temp = data["current_condition"][0]["temp_C"]

# Ваш код здесь:


# ============================================================
# Задание 5: Работа с JSONPlaceholder
# ============================================================
# Используя https://jsonplaceholder.typicode.com:
# 1. Получите все посты (GET /posts)
# 2. Получите пост по ID (GET /posts/1)
# 3. Создайте новый пост (POST /posts)
# 4. Выведите заголовки первых 5 постов
#
# Ожидаемый результат:
#   posts = get_posts()
#   print(len(posts))  → 100
#
#   post = get_post(1)
#   print(post["title"])  → "sunt aut facere..."
#
#   new = create_post("Мой заголовок", "Текст поста", user_id=1)
#   print(new["id"])  → 101
#
# Подсказка:
#   BASE_URL = "https://jsonplaceholder.typicode.com"

# Ваш код здесь:


# ============================================================
# Задание 6: Обработка ошибок HTTP
# ============================================================
# Напишите функцию safe_request(url, method="GET", **kwargs),
# которая обрабатывает все возможные ошибки:
#   - ConnectionError → нет соединения
#   - Timeout → таймаут
#   - HTTPError → код 4xx/5xx
#   - JSONDecodeError → ответ не JSON
#
# Ожидаемый результат:
#   r = safe_request("https://httpbin.org/get")
#   print(r["status"])  → "success"
#
#   r = safe_request("https://httpbin.org/status/404")
#   print(r["status"])  → "error"
#   print(r["error"])   → "HTTP 404"
#
#   r = safe_request("https://invalid.domain.xyz")
#   print(r["error"])   → "Нет соединения"
#
# Подсказка:
#   try:
#       response = requests.get(url, timeout=5)
#       response.raise_for_status()
#   except requests.ConnectionError: ...
#   except requests.Timeout: ...
#   except requests.HTTPError as e: ...

# Ваш код здесь:


# ============================================================
# Задание 7: Пагинация
# ============================================================
# Напишите функцию get_all_pages(base_url), которая
# автоматически загружает все страницы API.
# Используйте JSONPlaceholder: /posts?_page=1&_limit=10
#
# Ожидаемый результат:
#   all_posts = get_all_pages(
#       "https://jsonplaceholder.typicode.com/posts",
#       per_page=10
#   )
#   print(f"Загружено {len(all_posts)} постов за N запросов")
#   → "Загружено 100 постов за 10 запросов"
#
# Подсказка:
#   page = 1
#   while True:
#       r = requests.get(url, params={"_page": page, "_limit": per_page})
#       data = r.json()
#       if not data: break
#       all_data.extend(data)
#       page += 1

# Ваш код здесь:


# ============================================================
# Задание 8: Скачивание файла
# ============================================================
# Напишите функцию download_file(url, save_path), которая
# скачивает файл с прогресс-баром (простой, в консоли).
#
# Ожидаемый результат:
#   download_file(
#       "https://httpbin.org/image/png",
#       "image.png"
#   )
#   # Скачивание: [████████████████████] 100% (8.5 KB)
#   # Файл сохранён: image.png
#
# Подсказка:
#   response = requests.get(url, stream=True)
#   total = int(response.headers.get("content-length", 0))
#   with open(save_path, "wb") as f:
#       for chunk in response.iter_content(chunk_size=1024):
#           f.write(chunk)

# Ваш код здесь:


# ============================================================
# Задание 9: Кэширование запросов
# ============================================================
# Напишите класс CachedAPI, который кэширует GET-запросы
# в JSON-файл. Если данные уже запрашивались менее N минут
# назад, возвращает кэш вместо нового запроса.
#
# Ожидаемый результат:
#   api = CachedAPI(cache_file="cache.json", ttl_minutes=5)
#   data = api.get("https://jsonplaceholder.typicode.com/posts/1")
#   print(data["title"])  → "sunt aut facere..."  (запрос к API)
#
#   data = api.get("https://jsonplaceholder.typicode.com/posts/1")
#   print(data["title"])  → "sunt aut facere..."  (из кэша!)
#
# Подсказка:
#   import json, time
#   cache = {"url": {"data": ..., "timestamp": time.time()}}
#   if time.time() - cached["timestamp"] < ttl_seconds: return cached

import json
import time

# Ваш код здесь:


# ============================================================
# Задание 10: Мини-клиент API
# ============================================================
# Создайте класс APIClient с методами:
#   get(endpoint, params=None) → GET-запрос
#   post(endpoint, data=None) → POST-запрос
#   put(endpoint, data=None) → PUT-запрос
#   delete(endpoint) → DELETE-запрос
# Базовый URL задаётся при инициализации.
# Все методы возвращают JSON и обрабатывают ошибки.
#
# Ожидаемый результат:
#   client = APIClient("https://jsonplaceholder.typicode.com")
#
#   posts = client.get("/posts", params={"_limit": 3})
#   print(len(posts))  → 3
#
#   new_post = client.post("/posts", {"title": "Test", "body": "Hello"})
#   print(new_post["id"])  → 101
#
#   client.delete("/posts/1")
#   # Удалено: /posts/1
#
# Подсказка:
#   def __init__(self, base_url):
#       self.base_url = base_url.rstrip("/")
#       self.session = requests.Session()

# Ваш код здесь:
