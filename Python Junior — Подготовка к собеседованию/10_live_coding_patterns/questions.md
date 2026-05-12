# 10 — Live Coding: Теоретические вопросы

---

## Вопрос 1: Как подходить к задачам на live coding?

<details>
<summary>💡 Ответ</summary>

**Алгоритм UMPIRE:**

1. **U**nderstand — Поймите задачу. Задайте уточняющие вопросы.
2. **M**atch — Сопоставьте с известными паттернами (two pointers, hash map, sliding window).
3. **P**lan — Опишите план решения словами/псевдокодом.
4. **I**mplement — Напишите код.
5. **R**eview — Проверьте на тестах и edge cases.
6. **E**valuate — Оцените сложность (time/space Big O).

**Уточняющие вопросы:**
- Какие типы данных на входе?
- Могут ли быть дубликаты / отрицательные / пустой ввод?
- Нужно ли решение in-place?
- Какие ограничения по памяти/времени?
</details>

---

## Вопрос 2: Какие паттерны чаще всего встречаются?

<details>
<summary>💡 Ответ</summary>

| Паттерн | Когда | Пример задач |
|---------|-------|-------------|
| Hash Map | Подсчёт, поиск пар | Two Sum, Anagram |
| Two Pointers | Отсортированный массив | Palindrome, Container with Water |
| Sliding Window | Подстрока, подмассив | Max sum subarray |
| Stack | Скобки, вложенность | Valid Parentheses |
| Рекурсия | Деревья, перестановки | Fibonacci, Permutations |
| Сортировка | Упорядочивание | Merge intervals |
</details>

---

## Вопрос 3: Как оценить сложность по времени?

<details>
<summary>💡 Ответ</summary>

```python
# O(1) — фиксированное время
return arr[0]

# O(n) — один проход
for x in arr: ...

# O(n²) — вложенные циклы
for i in arr:
    for j in arr: ...

# O(n log n) — сортировка
arr.sort()

# O(log n) — бинарный поиск
while left < right:
    mid = (left + right) // 2
```
</details>

---

## Вопрос 4: Как проверить edge cases?

<details>
<summary>💡 Ответ</summary>

**Всегда проверяйте:**
- Пустой ввод: `[]`, `""`, `None`
- Один элемент: `[1]`, `"a"`
- Все одинаковые: `[5, 5, 5]`
- Отрицательные числа: `[-1, -2, -3]`
- Уже отсортировано / отсортировано наоборот
- Очень большой ввод (для оценки сложности)
- Дубликаты
</details>

---

## Вопрос 5: Что делать, если не знаешь решение?

<details>
<summary>💡 Ответ</summary>

1. **Начните с brute force** — наивное решение лучше, чем ничего
2. **Думайте вслух** — интервьюер хочет видеть ход мыслей
3. **Пробуйте примеры** — разберите 2-3 примера вручную
4. **Ищите паттерн** — в примерах часто видно закономерность
5. **Спросите подсказку** — это нормально! Лучше спросить, чем молчать

**Что оценивают:**
- Умение декомпозировать задачу
- Коммуникацию и ход мыслей
- Обработку edge cases
- Чистоту кода
</details>

---

## Вопрос 6: Как писать чистый код на собеседовании?

<details>
<summary>💡 Ответ</summary>

```python
# ❌ Плохо
def f(a):
    r = {}
    for i in a:
        if i in r: r[i] += 1
        else: r[i] = 1
    return max(r, key=r.get)

# ✅ Хорошо
def most_frequent(items):
    """Находит самый частый элемент."""
    from collections import Counter
    counts = Counter(items)
    return counts.most_common(1)[0][0]
```

**Советы:**
- Понятные имена переменных
- Разбивайте на функции
- Используйте стандартную библиотеку
- Комментируйте сложные места
</details>

---

## Вопрос 7-15: Классические задачи (краткие решения)

<details>
<summary>💡 FizzBuzz</summary>

```python
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0: print("FizzBuzz")
        elif i % 3 == 0: print("Fizz")
        elif i % 5 == 0: print("Buzz")
        else: print(i)
```
</details>

<details>
<summary>💡 Two Sum</summary>

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```
</details>

<details>
<summary>💡 Valid Parentheses</summary>

```python
def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif not stack or stack.pop() != pairs[char]:
            return False
    return len(stack) == 0
```
</details>

<details>
<summary>💡 Reverse String</summary>

```python
def reverse_string(s):
    return s[::-1]

# Без встроенных средств
def reverse_string_manual(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)
```
</details>

<details>
<summary>💡 Palindrome</summary>

```python
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
```
</details>

<details>
<summary>💡 Find Duplicates</summary>

```python
def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)
```
</details>

<details>
<summary>💡 Fibonacci</summary>

```python
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```
</details>

<details>
<summary>💡 Anagram Check</summary>

```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1.lower()) == Counter(s2.lower())
```
</details>

<details>
<summary>💡 Merge Two Sorted Lists</summary>

```python
def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
```
</details>
