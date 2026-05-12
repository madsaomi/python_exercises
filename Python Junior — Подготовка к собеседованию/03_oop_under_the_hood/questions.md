# 03 — ООП под капотом: Теоретические вопросы

---

## Вопрос 1: В чём разница между `__new__` и `__init__`?

<details>
<summary>💡 Ответ</summary>

- `__new__` — **создаёт** экземпляр класса (вызывается до `__init__`). Это статический метод.
- `__init__` — **инициализирует** уже созданный экземпляр (настраивает атрибуты).

```python
class MyClass:
    def __new__(cls, *args):
        print("__new__: создание объекта")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("__init__: инициализация")
        self.value = value

obj = MyClass(42)
# __new__: создание объекта
# __init__: инициализация
```

`__new__` используется редко: для Singleton, наследования от неизменяемых типов (`str`, `int`, `tuple`), метаклассов.
</details>

---

## Вопрос 2: Что такое MRO (Method Resolution Order)?

<details>
<summary>💡 Ответ</summary>

**MRO** — порядок, в котором Python ищет методы при множественном наследовании. Используется алгоритм **C3-линеаризации**.

```python
class A:
    def who(self): return "A"

class B(A):
    def who(self): return "B"

class C(A):
    def who(self): return "C"

class D(B, C):
    pass

print(D.mro())  # [D, B, C, A, object]
print(D().who())  # "B" — найден первым в MRO
```

Проверить MRO: `Class.mro()` или `Class.__mro__`.
</details>

---

## Вопрос 3: Как работает `super()`?

<details>
<summary>💡 Ответ</summary>

`super()` возвращает прокси-объект, который делегирует вызов **следующему классу в MRO** (не обязательно прямому родителю!).

```python
class A:
    def greet(self):
        print("A")

class B(A):
    def greet(self):
        print("B")
        super().greet()  # вызовет A.greet()

class C(A):
    def greet(self):
        print("C")
        super().greet()

class D(B, C):
    def greet(self):
        print("D")
        super().greet()  # вызовет B.greet() (следующий в MRO)

D().greet()
# D → B → C → A (по MRO)
```
</details>

---

## Вопрос 4: Что такое `@property` и зачем он нужен?

<details>
<summary>💡 Ответ</summary>

`@property` позволяет обращаться к методу как к атрибуту, добавляя контроль при чтении/записи:

```python
class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = value

user = User("Анна", 25)
print(user.age)     # 25 (вызов getter)
user.age = 30       # вызов setter
# user.age = -1     # ValueError!
```
</details>

---

## Вопрос 5: В чём разница между `@staticmethod` и `@classmethod`?

<details>
<summary>💡 Ответ</summary>

| | `@staticmethod` | `@classmethod` |
|--|-----------------|----------------|
| Первый аргумент | Нет | `cls` (класс) |
| Доступ к классу | Нет | Да |
| Доступ к экземпляру | Нет | Нет |
| Использование | Утилитарные функции | Фабричные методы, альтернативные конструкторы |

```python
class Date:
    def __init__(self, day, month, year):
        self.day, self.month, self.year = day, month, year

    @classmethod
    def from_string(cls, date_str):
        d, m, y = map(int, date_str.split("-"))
        return cls(d, m, y)  # создаёт экземпляр класса

    @staticmethod
    def is_valid(date_str):
        parts = date_str.split("-")
        return len(parts) == 3

Date.from_string("25-12-2024")  # альтернативный конструктор
Date.is_valid("25-12-2024")     # утилита, не зависит от класса
```
</details>

---

## Вопрос 6: Что такое `__slots__`?

<details>
<summary>💡 Ответ</summary>

`__slots__` — ограничивает набор атрибутов экземпляра. Экономит память (не создаётся `__dict__`).

```python
class WithSlots:
    __slots__ = ['x', 'y']

class WithoutSlots:
    pass

a = WithSlots()
a.x = 1
# a.z = 3  # AttributeError!

b = WithoutSlots()
b.x = 1
b.z = 3  # Работает — есть __dict__
```

**Когда использовать:** Миллионы экземпляров (data-intensive), экономия ~40% памяти.
</details>

---

## Вопрос 7: Что такое абстрактный класс и зачем он нужен?

<details>
<summary>💡 Ответ</summary>

Абстрактный класс определяет интерфейс — набор методов, которые **обязаны** реализовать наследники. Нельзя создать экземпляр абстрактного класса.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# shape = Shape()  # TypeError: Can't instantiate abstract class
circle = Circle(5)
print(circle.area())  # 78.5
```
</details>

---

## Вопрос 8: Чем отличается `__str__` от `__repr__`?

<details>
<summary>💡 Ответ</summary>

- `__str__` — для пользователя. Вызывается `print()` и `str()`. Читаемый формат.
- `__repr__` — для разработчика. Вызывается в консоли. Однозначный, в идеале — `eval(repr(obj)) == obj`.

Если `__str__` не определён — вызывается `__repr__`.

```python
import datetime
d = datetime.date(2024, 1, 15)
print(str(d))   # 2024-01-15 (для пользователя)
print(repr(d))  # datetime.date(2024, 1, 15) (для разработчика)
```
</details>

---

## Вопрос 9: Что такое миксин (mixin)?

<details>
<summary>💡 Ответ</summary>

**Миксин** — небольшой класс, который добавляет одну конкретную функциональность через множественное наследование. Миксин не предназначен для самостоятельного использования.

```python
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class LogMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class User(JsonMixin, LogMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Alice", 30)
print(user.to_json())  # {"name": "Alice", "age": 30}
user.log("Created")     # [User] Created
```
</details>

---

## Вопрос 10: Что такое `__hash__` и `__eq__`? Как они связаны?

<details>
<summary>💡 Ответ</summary>

- `__eq__` — определяет, когда объекты считаются **равными** (`==`)
- `__hash__` — возвращает хеш объекта (нужен для `dict`, `set`)

**Правило:** Если `a == b`, то `hash(a) == hash(b)` (обратное не обязательно).

Если вы определили `__eq__`, Python **автоматически делает** `__hash__ = None` (объект становится нехешируемым). Нужно определить `__hash__` явно.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p1, p2 = Point(1, 2), Point(1, 2)
print(p1 == p2)                # True
print({p1, p2})                # один элемент
print({p1: "point"})           # можно использовать как ключ
```
</details>

---

## Вопрос 11: Что такое Singleton и как его реализовать?

<details>
<summary>💡 Ответ</summary>

**Singleton** — паттерн, гарантирующий один экземпляр класса.

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)  # True — один и тот же объект
```
</details>

---

## Вопрос 12: Что такое дескриптор?

<details>
<summary>💡 Ответ</summary>

**Дескриптор** — объект, определяющий поведение при доступе к атрибуту. Должен реализовать `__get__`, `__set__` или `__delete__`.

```python
class Positive:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.name} должен быть >= 0")
        obj.__dict__[self.name] = value

    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name, 0)

class Product:
    price = Positive()
    quantity = Positive()

p = Product()
p.price = 100       # OK
# p.price = -10     # ValueError!
```

`@property` — это встроенный дескриптор!
</details>

---

## Вопрос 13: Что такое `__dict__` у объекта?

<details>
<summary>💡 Ответ</summary>

`__dict__` — словарь, содержащий атрибуты экземпляра:

```python
class User:
    role = "user"  # атрибут класса

    def __init__(self, name):
        self.name = name  # атрибут экземпляра

u = User("Alice")
print(u.__dict__)           # {'name': 'Alice'}
print(User.__dict__.keys()) # включает 'role', '__init__', ...
```

Атрибуты класса не попадают в `__dict__` экземпляра, но доступны через цепочку поиска.
</details>

---

## Вопрос 14: Что такое наследование и полиморфизм?

<details>
<summary>💡 Ответ</summary>

**Наследование** — класс получает атрибуты и методы от родителя.  
**Полиморфизм** — один интерфейс, разная реализация.

```python
class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"

# Полиморфизм — одна функция, разное поведение
for animal in [Dog(), Cat()]:
    print(animal.speak())  # Гав! / Мяу!
```
</details>

---

## Вопрос 15: В чём разница между атрибутом класса и атрибутом экземпляра?

<details>
<summary>💡 Ответ</summary>

- **Атрибут класса** — общий для всех экземпляров. Определяется в теле класса.
- **Атрибут экземпляра** — уникален для каждого. Определяется в `__init__` через `self`.

```python
class Dog:
    species = "Canis familiaris"  # атрибут класса

    def __init__(self, name):
        self.name = name  # атрибут экземпляра

d1 = Dog("Рекс")
d2 = Dog("Бобик")
print(d1.species)  # Canis familiaris (общий)
print(d1.name)     # Рекс (уникальный)
```

**Ловушка:** Если атрибут класса мутабельный (список, словарь), изменение через экземпляр затронет все!
</details>
