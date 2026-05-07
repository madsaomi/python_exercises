# 📘 Тема 11: Продвинутое ООП

## Наследование

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return f"{self.name}: Гав!"

class Cat(Animal):
    def speak(self):
        return f"{self.name}: Мяу!"

dog = Dog("Рекс")
print(dog.speak())  # "Рекс: Гав!"
```

## `super()` — вызов родителя

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
```

## Множественное наследование

```python
class Flyable:
    def fly(self):
        return "Летаю!"

class Swimmable:
    def swim(self):
        return "Плаваю!"

class Duck(Flyable, Swimmable):
    pass

duck = Duck()
duck.fly()   # "Летаю!"
duck.swim()  # "Плаваю!"
```

## Абстрактные классы

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# shape = Shape()  # ❌ TypeError — нельзя создать
circle = Circle(5)  # ✅
```

## Полиморфизм

```python
shapes = [Circle(5), Rectangle(3, 4), Triangle(3, 4, 5)]

for shape in shapes:
    print(f"Площадь: {shape.area()}")  # каждый вычисляет по-своему
```

## Композиция vs Наследование

```python
# Композиция ("has-a") — предпочтительнее
class Engine:
    def start(self):
        return "Двигатель запущен"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car ИМЕЕТ Engine

    def start(self):
        return self.engine.start()
```

## Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5

p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1.distance(p2))  # 5.0
print(p1)  # Point(x=0, y=0) — автоматический __repr__
```

## isinstance и issubclass

```python
isinstance(dog, Dog)      # True
isinstance(dog, Animal)   # True
issubclass(Dog, Animal)   # True
```
