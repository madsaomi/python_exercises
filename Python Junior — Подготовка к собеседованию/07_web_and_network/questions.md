# 07 — Веб и сети: Теоретические вопросы

---

## Вопрос 1: Какие HTTP-методы существуют и для чего?

<details>
<summary>💡 Ответ</summary>

| Метод | Назначение | Идемпотентный | Тело запроса |
|-------|-----------|---------------|-------------|
| `GET` | Получить ресурс | Да | Нет |
| `POST` | Создать ресурс | Нет | Да |
| `PUT` | Заменить ресурс целиком | Да | Да |
| `PATCH` | Частично обновить | Нет* | Да |
| `DELETE` | Удалить ресурс | Да | Нет |
| `HEAD` | Как GET, но без тела ответа | Да | Нет |
| `OPTIONS` | Узнать поддерживаемые методы | Да | Нет |

**Идемпотентный** — повторный вызов даёт тот же результат.
</details>

---

## Вопрос 2: Что означают коды статусов HTTP?

<details>
<summary>💡 Ответ</summary>

| Диапазон | Категория | Примеры |
|----------|-----------|---------|
| 1xx | Информационные | 100 Continue |
| 2xx | Успех | 200 OK, 201 Created, 204 No Content |
| 3xx | Перенаправление | 301 Moved Permanently, 302 Found, 304 Not Modified |
| 4xx | Ошибка клиента | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 422 Unprocessable Entity, 429 Too Many Requests |
| 5xx | Ошибка сервера | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable |

**Ключевые для собеседования:**
- **401 vs 403:** 401 — не авторизован (нет токена). 403 — нет прав (токен есть, но доступ запрещён).
- **PUT vs PATCH:** PUT заменяет целиком, PATCH — частично.
</details>

---

## Вопрос 3: Что такое REST API?

<details>
<summary>💡 Ответ</summary>

**REST** (Representational State Transfer) — архитектурный стиль для API:

1. **Клиент-сервер** — разделение ответственности
2. **Stateless** — сервер не хранит состояние клиента
3. **Кэширование** — ответы могут кэшироваться
4. **Единообразный интерфейс** — стандартные методы HTTP
5. **Многоуровневость** — клиент не знает, с каким слоем работает

```
GET    /api/users          — список пользователей
GET    /api/users/1        — один пользователь
POST   /api/users          — создать пользователя
PUT    /api/users/1        — обновить пользователя
DELETE /api/users/1        — удалить пользователя
```
</details>

---

## Вопрос 4: В чём разница между авторизацией и аутентификацией?

<details>
<summary>💡 Ответ</summary>

- **Аутентификация (Authentication)** — «Кто ты?» Проверка личности (логин/пароль, токен).
- **Авторизация (Authorization)** — «Что тебе можно?» Проверка прав доступа.

```
1. Пользователь вводит логин/пароль → Аутентификация
2. Сервер проверяет, может ли user делать DELETE → Авторизация
```

**Порядок:** Сначала аутентификация, потом авторизация.
</details>

---

## Вопрос 5: Что такое JWT?

<details>
<summary>💡 Ответ</summary>

**JWT (JSON Web Token)** — стандарт токенов для аутентификации. Состоит из трёх частей, разделённых точками:

```
Header.Payload.Signature
```

- **Header:** алгоритм и тип (`{"alg": "HS256", "typ": "JWT"}`)
- **Payload:** данные (user_id, роль, срок действия)
- **Signature:** подпись для проверки целостности

```
eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.signature
```

**Плюсы:** Stateless (не нужна сессия на сервере), масштабируемость.  
**Минусы:** Нельзя отозвать до истечения срока, размер больше session ID.
</details>

---

## Вопрос 6: Что такое CORS?

<details>
<summary>💡 Ответ</summary>

**CORS (Cross-Origin Resource Sharing)** — механизм, позволяющий веб-странице делать запросы к другому домену.

По умолчанию браузер **блокирует** кросс-доменные запросы (same-origin policy). CORS — способ разрешить их через заголовки:

```
Access-Control-Allow-Origin: https://frontend.com
Access-Control-Allow-Methods: GET, POST
Access-Control-Allow-Headers: Content-Type, Authorization
```

**Важно:** CORS — ограничение **браузера**, а не сервера. Postman и curl не блокируют кросс-доменные запросы.
</details>

---

## Вопрос 7: Что такое cookies и sessions?

<details>
<summary>💡 Ответ</summary>

| | Cookies | Sessions |
|--|---------|----------|
| Где хранятся | На клиенте (браузер) | На сервере |
| Размер | До ~4KB | Не ограничен |
| Безопасность | Видны клиенту | Скрыты на сервере |
| Срок жизни | Настраивается | До закрытия браузера / timeout |

**Как связаны:** Сессия хранится на сервере, а клиент получает session_id в cookie для идентификации.
</details>

---

## Вопрос 8: Что такое WebSocket?

<details>
<summary>💡 Ответ</summary>

**WebSocket** — протокол для двунаправленной связи в реальном времени. В отличие от HTTP (запрос-ответ), WebSocket держит **постоянное соединение**.

```
HTTP:      клиент → запрос → сервер → ответ (соединение закрыто)
WebSocket: клиент ↔ сервер (постоянное соединение, обмен сообщениями)
```

**Когда:** Чаты, уведомления в реальном времени, онлайн-игры, котировки.
</details>

---

## Вопрос 9: В чём разница между HTTP и HTTPS?

<details>
<summary>💡 Ответ</summary>

**HTTPS = HTTP + TLS/SSL** (шифрование).

| | HTTP | HTTPS |
|--|------|-------|
| Порт | 80 | 443 |
| Шифрование | Нет | TLS/SSL |
| Данные | Открытым текстом | Зашифрованы |
| Сертификат | Не нужен | Нужен SSL-сертификат |

**Зачем:** Защита данных (пароли, платежи) от перехвата (man-in-the-middle).
</details>

---

## Вопрос 10: Что такое API Rate Limiting?

<details>
<summary>💡 Ответ</summary>

**Rate Limiting** — ограничение количества запросов к API за период времени.

```
Заголовки ответа:
X-RateLimit-Limit: 100      — максимум запросов
X-RateLimit-Remaining: 42   — осталось запросов
X-RateLimit-Reset: 1619000  — когда сбросится лимит
```

При превышении — код **429 Too Many Requests**.

**Алгоритмы:** Token Bucket, Sliding Window, Fixed Window.
</details>

---

## Вопрос 11: Что такое идемпотентность?

<details>
<summary>💡 Ответ</summary>

**Идемпотентный** запрос — повторный вызов даёт тот же результат:

- `GET /users/1` — идемпотентный (всегда возвращает того же пользователя)
- `DELETE /users/1` — идемпотентный (первый вызов удаляет, второй — 404, но состояние не меняется)
- `POST /users` — **НЕ** идемпотентный (каждый вызов создаёт нового пользователя)
</details>

---

## Вопрос 12: Что такое JSON и XML?

<details>
<summary>💡 Ответ</summary>

Оба — форматы обмена данными:

```json
{"name": "Alice", "age": 30, "hobbies": ["python", "chess"]}
```

```xml
<user>
  <name>Alice</name>
  <age>30</age>
  <hobbies>
    <hobby>python</hobby>
    <hobby>chess</hobby>
  </hobbies>
</user>
```

**JSON** — легче, проще парсить, стандарт для REST API.  
**XML** — больше возможностей (атрибуты, схемы), используется в SOAP.
</details>

---

## Вопрос 13: Как работает DNS?

<details>
<summary>💡 Ответ</summary>

**DNS (Domain Name System)** — переводит доменное имя в IP-адрес.

```
google.com → 142.250.74.78
```

Цепочка: Браузер кэш → ОС кэш → Роутер → DNS-рекурсор → Root → TLD (.com) → Авторитативный сервер.
</details>

---

## Вопрос 14: Что такое GraphQL и чем отличается от REST?

<details>
<summary>💡 Ответ</summary>

| | REST | GraphQL |
|--|------|---------|
| Endpoint'ы | Множество (`/users`, `/posts`) | Один (`/graphql`) |
| Данные | Фиксированная структура | Клиент запрашивает нужные поля |
| Over-fetching | Часто | Нет |
| Кэширование | Простое (HTTP) | Сложнее |

```graphql
# GraphQL — клиент указывает, что нужно
query {
  user(id: 1) {
    name
    email
  }
}
```
</details>

---

## Вопрос 15: Что такое middleware?

<details>
<summary>💡 Ответ</summary>

**Middleware** — промежуточный слой, обрабатывающий запросы/ответы. Цепочка обработчиков:

```
Запрос → [Auth] → [Logging] → [CORS] → Handler → [Logging] → Ответ
```

Примеры: логирование, аутентификация, сжатие, обработка ошибок, CORS.

```python
# Django middleware
class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Request: {request.path}")
        response = self.get_response(request)
        print(f"Response: {response.status_code}")
        return response
```
</details>
