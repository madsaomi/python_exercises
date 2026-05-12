# 07 — Веб и сети: Задачи-ловушки

> ⚠️ Ответьте на вопросы **до** раскрытия ответов.

---

## Задача 1: HTTP-метод для формы

Вы создаёте форму регистрации пользователя. Какой HTTP-метод использовать?

```
GET  /api/register?name=Alice&password=12345
POST /api/register  {name: Alice, password: 12345}
```

<details>
<summary>🔍 Ответ</summary>

**POST**

- GET передаёт данные в URL — пароль будет виден в адресной строке, логах сервера, истории браузера!
- POST передаёт данные в теле запроса — безопаснее
- GET идемпотентный — не подходит для создания ресурса
</details>

---

## Задача 2: Код ответа

Какой код ответа вернуть, если пользователь отправляет запрос на удаление чужого ресурса (авторизован, но нет прав)?

<details>
<summary>🔍 Ответ</summary>

**403 Forbidden** (не 401!)

- **401 Unauthorized** — не аутентифицирован (нет токена)
- **403 Forbidden** — аутентифицирован, но нет прав
</details>

---

## Задача 3: REST URL

Какой URL правильный для получения комментариев к посту #42?

```
A) GET /api/getCommentsByPostId?postId=42
B) GET /api/posts/42/comments
C) POST /api/comments  {post_id: 42}
```

<details>
<summary>🔍 Ответ</summary>

**B) `GET /api/posts/42/comments`**

- A — не REST-стиль (глаголы в URL, camelCase)
- C — POST для чтения данных — неправильный метод
- B — ресурс-ориентированный URL, GET для чтения
</details>

---

## Задача 4: requests и статус

```python
import requests

response = requests.get("https://httpbin.org/status/404")
print(response.status_code)
print(response.ok)
print(bool(response))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
404
False
False
```

**Объяснение:** `response.ok` — True для 2xx. `bool(response)` — тоже зависит от статуса (True для 2xx-3xx, False для 4xx-5xx в библиотеке requests).
</details>

---

## Задача 5: JSON парсинг

```python
import json

data = '{"name": "Alice", "age": 30, "active": true, "address": null}'
parsed = json.loads(data)

print(type(parsed["active"]))
print(type(parsed["address"]))
print(parsed["address"])
```

<details>
<summary>🔍 Что выведет код?</summary>

```
<class 'bool'>
<class 'NoneType'>
None
```

**Объяснение:** JSON → Python маппинг: `true` → `True`, `false` → `False`, `null` → `None`.
</details>

---

## Задача 6: URL-кодирование

```python
from urllib.parse import quote, urlencode

print(quote("hello world"))
print(quote("привет"))
print(urlencode({"name": "Alice Bob", "age": 30}))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
hello%20world
%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82
name=Alice+Bob&age=30
```

**Объяснение:** `quote` кодирует спецсимволы в URL (%20 для пробела). `urlencode` формирует query string (+ для пробела в параметрах).
</details>

---

## Задача 7: Заголовки и Content-Type

Что будет, если отправить JSON без правильного заголовка?

```python
import requests

# ❌ Без Content-Type
requests.post("/api/users", data='{"name": "Alice"}')

# ✅ С правильным заголовком
requests.post("/api/users", json={"name": "Alice"})
```

<details>
<summary>🔍 Ответ</summary>

Первый запрос отправит `Content-Type: application/x-www-form-urlencoded` — сервер может не распарсить JSON.

Параметр `json=` автоматически:
1. Устанавливает `Content-Type: application/json`
2. Сериализует словарь в JSON
</details>

---

## Задача 8: Redirect

```python
import requests

response = requests.get("https://httpbin.org/redirect/3")
print(response.status_code)
print(len(response.history))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
200
3
```

**Объяснение:** `requests` по умолчанию следует редиректам. Финальный ответ — 200. `history` содержит промежуточные ответы (3 редиректа).
</details>

---

## Задача 9: Timeout

```python
import requests

try:
    response = requests.get("https://httpbin.org/delay/10", timeout=2)
except requests.Timeout:
    print("Timeout!")
except requests.ConnectionError:
    print("Connection Error!")
```

<details>
<summary>🔍 Что выведет код?</summary>

```
Timeout!
```

**Объяснение:** Сервер ждёт 10 секунд перед ответом, но timeout=2 прерывает ожидание через 2 секунды. **Всегда устанавливайте timeout!**
</details>

---

## Задача 10: Pagination

Как правильно реализовать пагинацию в REST API?

```
A) GET /api/users?page=2&size=10
B) GET /api/users?offset=10&limit=10
C) GET /api/users?cursor=abc123&limit=10
```

<details>
<summary>🔍 Ответ</summary>

**Все три — правильные**, но для разных случаев:

- **A (Page-based):** Простой, но «плывёт» при добавлении данных
- **B (Offset-based):** Гибкий, но медленный при большом offset
- **C (Cursor-based):** Оптимальный для больших датасетов (Twitter, Facebook). Стабилен при изменениях.
</details>
