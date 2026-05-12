# 03 — ООП под капотом: Задачи-ловушки

> ⚠️ Попробуйте предсказать вывод **БЕЗ запуска**.

---

## Задача 1: Мутабельный атрибут класса

```python
class Team:
    members = []

    def add(self, name):
        self.members.append(name)

a = Team()
b = Team()
a.add("Alice")
b.add("Bob")

print(a.members)
print(b.members)
print(a.members is b.members)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
['Alice', 'Bob']
['Alice', 'Bob']
True
```

**Объяснение:** `members = []` — атрибут **класса**, общий для всех экземпляров. `a.members` и `b.members` ссылаются на один и тот же список.
</details>

---

## Задача 2: MRO и `super()`

```python
class A:
    def say(self):
        print("A", end=" ")

class B(A):
    def say(self):
        print("B", end=" ")
        super().say()

class C(A):
    def say(self):
        print("C", end=" ")
        super().say()

class D(B, C):
    def say(self):
        print("D", end=" ")
        super().say()

D().say()
```

<details>
<summary>🔍 Что выведет код?</summary>

```
D B C A
```

**Объяснение:** MRO для D: [D, B, C, A, object]. `super()` следует MRO, поэтому: D→B→C→A. Метод `A.say()` вызывается только один раз (не дважды!).
</details>

---

## Задача 3: `__init__` и наследование

```python
class Parent:
    def __init__(self):
        self.x = 1
        print("Parent init")

class Child(Parent):
    def __init__(self):
        self.y = 2
        print("Child init")

c = Child()
print(c.y)
print(c.x)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
Child init
2
AttributeError: 'Child' object has no attribute 'x'
```

**Объяснение:** `Child.__init__` не вызывает `super().__init__()`, поэтому `self.x` не создаётся. Всегда вызывайте `super().__init__()` в наследниках!
</details>

---

## Задача 4: `@property` ловушка

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.radius)
print(c.area)
c.radius = 10
```

<details>
<summary>🔍 Что выведет код?</summary>

```
5
78.5
AttributeError: property 'radius' has no setter
```

**Объяснение:** `@property` без `@radius.setter` делает атрибут **только для чтения**. Попытка присвоить значение — ошибка.
</details>

---

## Задача 5: `isinstance` и `bool`

```python
print(isinstance(True, int))
print(isinstance(True, bool))
print(issubclass(bool, int))

class MyBool(int):
    pass

print(isinstance(MyBool(), int))
```

<details>
<summary>🔍 Что выведет код?</summary>

```
True
True
True
True
```

**Объяснение:** `bool` — подкласс `int`. `isinstance` проверяет всю цепочку наследования. `True` является экземпляром и `bool`, и `int`.
</details>

---

## Задача 6: `__str__` vs `__repr__` приоритет

```python
class Item:
    def __repr__(self):
        return "Item.__repr__"

class ItemWithStr:
    def __repr__(self):
        return "ItemWithStr.__repr__"

    def __str__(self):
        return "ItemWithStr.__str__"

a = Item()
b = ItemWithStr()

print(a)
print(b)
print([a, b])
```

<details>
<summary>🔍 Что выведет код?</summary>

```
Item.__repr__
ItemWithStr.__str__
[Item.__repr__, ItemWithStr.__repr__]
```

**Объяснение:** `print()` вызывает `__str__`, если он определён, иначе — `__repr__`. Но внутри контейнеров (список, словарь) **всегда** используется `__repr__` для элементов.
</details>

---

## Задача 7: Переопределение атрибута класса

```python
class Base:
    x = 10

class Child(Base):
    pass

c = Child()
c.x = 20

print(Base.x)
print(Child.x)
print(c.x)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
10
10
20
```

**Объяснение:** `c.x = 20` создаёт **атрибут экземпляра**, который «затеняет» атрибут класса. Атрибуты `Base.x` и `Child.x` не изменились.
</details>

---

## Задача 8: `__new__` и Singleton

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = 0

a = Singleton()
a.value = 42
b = Singleton()

print(a is b)
print(b.value)
```

<details>
<summary>🔍 Что выведет код?</summary>

```
True
0
```

**Объяснение:** `a is b` — True, это один объект. Но `__init__` вызывается при **каждом** создании! `b = Singleton()` вызывает `__init__`, сбрасывая `value` в 0.
</details>

---

## Задача 9: Множественное наследование

```python
class A:
    def method(self):
        return "A"

class B(A):
    pass

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

print(D().method())
```

<details>
<summary>🔍 Что выведет код?</summary>

```
C
```

**Объяснение:** MRO: D → B → C → A. `B` не переопределяет `method`, Python продолжает по MRO и находит в `C`.
</details>

---

## Задача 10: `__slots__` и `__dict__`

```python
class Compact:
    __slots__ = ['x', 'y']

obj = Compact()
obj.x = 1
obj.y = 2

try:
    obj.z = 3
except AttributeError as e:
    print(f"Ошибка: {e}")

try:
    print(obj.__dict__)
except AttributeError as e:
    print(f"Ошибка: {e}")
```

<details>
<summary>🔍 Что выведет код?</summary>

```
Ошибка: 'Compact' object has no attribute 'z'
Ошибка: 'Compact' object has no attribute '__dict__'
```

**Объяснение:** `__slots__` запрещает создание `__dict__` и ограничивает набор атрибутов. Нельзя добавить `z`, нельзя обратиться к `__dict__`.
</details>
