# 📘 Тема 18: Работа с API (requests)

## Установка

```bash
pip install requests
```

## GET-запрос

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)    # 200
print(response.json())         # словарь из JSON
print(response.text)           # текст ответа
print(response.headers)        # заголовки
```

## Параметры запроса

```python
params = {"q": "python", "page": 1}
response = requests.get("https://api.example.com/search", params=params)
# URL: https://api.example.com/search?q=python&page=1
```

## POST-запрос

```python
data = {"username": "user", "password": "pass"}
response = requests.post("https://api.example.com/login", json=data)
```

## Заголовки и авторизация

```python
headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Content-Type": "application/json"
}
response = requests.get(url, headers=headers)
```

## Обработка ошибок

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # вызовет ошибку при 4xx/5xx
except requests.exceptions.Timeout:
    print("Таймаут!")
except requests.exceptions.HTTPError as e:
    print(f"HTTP ошибка: {e}")
except requests.exceptions.ConnectionError:
    print("Ошибка соединения!")
```

## Скачивание файлов

```python
response = requests.get("https://example.com/image.jpg")
with open("image.jpg", "wb") as f:
    f.write(response.content)
```

## Сессии

```python
session = requests.Session()
session.headers.update({"Authorization": "Bearer TOKEN"})
r1 = session.get("https://api.example.com/data")
r2 = session.get("https://api.example.com/more")
```

## REST API — основные методы

| Метод | Назначение |
|-------|-----------|
| GET | Получить данные |
| POST | Создать ресурс |
| PUT | Обновить ресурс (полностью) |
| PATCH | Обновить ресурс (частично) |
| DELETE | Удалить ресурс |
