# 🧩 Recursion — Задачи

---

## 1. Fibonacci Number
**Difficulty:** 🟢 Easy  
**Паттерн:** Basic Recursion / Memoization

### Problem
Вычислите `n`-е число Фибоначчи.

```
F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2) для n >= 2
```

### Example 1
```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1
```

### Example 2
```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3
```

### Example 3
```
Input: n = 0
Output: 0
```

### Constraints
- `0 <= n <= 30`

### Hints
<details>
<summary>Подсказка 1</summary>
Наивная рекурсия: прямая формула F(n) = F(n-1) + F(n-2). Но O(2^n) — экспоненциально!
</details>

<details>
<summary>Подсказка 2</summary>
Мемоизация: сохраняйте уже вычисленные значения в dict/массиве. Или используйте @functools.lru_cache.
</details>

<details>
<summary>Подсказка 3</summary>
Итеративный подход: два переменных a, b = 0, 1. Обновляйте n раз.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Naive Recursion | O(2ⁿ) | O(n) |
| **Recursion + Memoization** | **O(n)** | **O(n)** |
| Iterative | O(n) | O(1) |

---

## 2. Power of Two
**Difficulty:** 🟢 Easy  
**Паттерн:** Recursive Division

### Problem
Определите, является ли число `n` степенью двойки. Решите **рекурсивно**.

Число является степенью двойки, если существует целое `k >= 0`, такое что `n == 2^k`.

### Example 1
```
Input: n = 1
Output: True
Explanation: 2^0 = 1
```

### Example 2
```
Input: n = 16
Output: True
Explanation: 2^4 = 16
```

### Example 3
```
Input: n = 3
Output: False
```

### Example 4
```
Input: n = 0
Output: False
```

### Constraints
- `-2^31 <= n <= 2^31 - 1`

### Hints
<details>
<summary>Подсказка 1</summary>
Базовые случаи: n <= 0 → False. n == 1 → True.
Рекурсия: если n чётное → isPowerOfTwo(n // 2). Если нечётное → False.
</details>

<details>
<summary>Подсказка 2</summary>
Битовый трюк (не рекурсия): n > 0 and n & (n-1) == 0.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Recursive division** | **O(log n)** | **O(log n)** |
| Bit manipulation | O(1) | O(1) |

---

## 3. Reverse Linked List (Recursive)
**Difficulty:** 🟢 Easy  
**Паттерн:** Recursive Linked List

### Problem
Дан односвязный список. Разверните его **рекурсивно** и верните новый head.

### Example 1
```
Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

### Example 2
```
Input: head = [1, 2]
Output: [2, 1]
```

### Example 3
```
Input: head = []
Output: []
```

### Constraints
- `0 <= количество узлов <= 5000`
- `-5000 <= Node.val <= 5000`

### Hints
<details>
<summary>Подсказка 1</summary>
Базовый случай: head is None или head.next is None → return head.
</details>

<details>
<summary>Подсказка 2</summary>
Рекурсивно разверните остаток списка. Затем: head.next.next = head, head.next = None. Верните new_head.
</details>

<details>
<summary>Подсказка 3</summary>
Пример: 1→2→3→4→5. Рекурсия доходит до 5 (new_head). Обратный ход: 4.next.next = 4 (5→4), 4.next = None. И так далее.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Iterative | O(n) | O(1) |
| **Recursive** | **O(n)** | **O(n)** (стек вызовов) |

---

## 4. Merge Two Sorted Lists (Recursive)
**Difficulty:** 🟢 Easy  
**Паттерн:** Recursive Merge

### Problem
Даны два отсортированных односвязных списка. Объедините их в один отсортированный список **рекурсивно**.

Новый список должен быть составлен из узлов исходных списков (не создавайте новые узлы).

### Example 1
```
Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
```

### Example 2
```
Input: list1 = [], list2 = []
Output: []
```

### Example 3
```
Input: list1 = [], list2 = [0]
Output: [0]
```

### Constraints
- `0 <= количество узлов <= 50`
- `-100 <= Node.val <= 100`
- Оба списка отсортированы по неубыванию

### Hints
<details>
<summary>Подсказка 1</summary>
Базовый случай: если один список пуст — вернуть другой.
</details>

<details>
<summary>Подсказка 2</summary>
Если list1.val <= list2.val: list1.next = merge(list1.next, list2), return list1. Иначе наоборот.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Iterative | O(m + n) | O(1) |
| **Recursive** | **O(m + n)** | **O(m + n)** (стек) |

---

## 5. Climbing Stairs
**Difficulty:** 🟢 Easy  
**Паттерн:** Recursion + Memoization / DP

### Problem
Вы поднимаетесь на лестницу из `n` ступенек. Каждый раз можно подняться на **1 или 2** ступеньки.

Сколько **различных способов** добраться до вершины?

### Example 1
```
Input: n = 2
Output: 2
Explanation: 1+1 или 2. Два способа.
```

### Example 2
```
Input: n = 3
Output: 3
Explanation: 1+1+1, 1+2, 2+1. Три способа.
```

### Example 3
```
Input: n = 5
Output: 8
Explanation: Это числа Фибоначчи! F(6) = 8.
```

### Constraints
- `1 <= n <= 45`

### Hints
<details>
<summary>Подсказка 1</summary>
f(n) = f(n-1) + f(n-2). С n-1 ступеньки шагаем на 1, с n-2 — на 2. Это Фибоначчи!
</details>

<details>
<summary>Подсказка 2</summary>
Наивная рекурсия — O(2^n). Добавьте мемоизацию или решите итеративно.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Naive Recursion | O(2ⁿ) | O(n) |
| **Memoized Recursion** | **O(n)** | **O(n)** |
| Iterative (DP) | O(n) | O(1) |

---

## 6. Generate Parentheses
**Difficulty:** 🟡 Medium  
**Паттерн:** Backtracking

### Problem
Дано `n` пар скобок. Сгенерируйте **все комбинации** правильных (well-formed) скобочных последовательностей.

### Example 1
```
Input: n = 1
Output: ["()"]
```

### Example 2
```
Input: n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

### Example 3
```
Input: n = 2
Output: ["(())", "()()"]
```

### Constraints
- `1 <= n <= 8`

### Hints
<details>
<summary>Подсказка 1</summary>
Backtracking: поддерживайте счётчики open и close. Можно добавить '(' если open < n. Можно добавить ')' если close < open.
</details>

<details>
<summary>Подсказка 2</summary>
Базовый случай: len(current) == 2*n → добавить в результат.
</details>

<details>
<summary>Подсказка 3</summary>
Количество результатов = каталанове число C(n) = (2n)! / ((n+1)! * n!).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Backtracking** | **O(4ⁿ / √n)** | **O(n)** |

---

## 7. Subsets
**Difficulty:** 🟡 Medium  
**Паттерн:** Backtracking / Bit Manipulation

### Problem
Дан массив **уникальных** целых чисел `nums`. Верните **все возможные подмножества** (power set).

Результат не должен содержать дубликатов. Порядок не важен.

### Example 1
```
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
```

### Example 2
```
Input: nums = [0]
Output: [[], [0]]
```

### Constraints
- `1 <= len(nums) <= 10`
- `-10 <= nums[i] <= 10`
- Все элементы уникальны

### Hints
<details>
<summary>Подсказка 1</summary>
Backtracking: для каждого элемента — включить или не включить в текущее подмножество.
</details>

<details>
<summary>Подсказка 2</summary>
Итеративно: начать с [[]]. Для каждого числа добавить его ко всем существующим подмножествам.
</details>

<details>
<summary>Подсказка 3</summary>
Бит-маска: для n элементов — 2^n подмножеств. Маска от 0 до 2^n - 1, бит i означает включение nums[i].
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Backtracking** | **O(n × 2ⁿ)** | **O(n)** |
| Iterative | O(n × 2ⁿ) | O(n × 2ⁿ) |
| Bitmask | O(n × 2ⁿ) | O(n × 2ⁿ) |

---

## 8. Permutations
**Difficulty:** 🟡 Medium  
**Паттерн:** Backtracking

### Problem
Дан массив **различных** целых чисел `nums`. Верните **все возможные перестановки** в любом порядке.

### Example 1
```
Input: nums = [1, 2, 3]
Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

### Example 2
```
Input: nums = [0, 1]
Output: [[0,1], [1,0]]
```

### Example 3
```
Input: nums = [1]
Output: [[1]]
```

### Constraints
- `1 <= len(nums) <= 6`
- `-10 <= nums[i] <= 10`
- Все элементы уникальны

### Hints
<details>
<summary>Подсказка 1</summary>
Backtracking: на каждом уровне выбираем один из оставшихся элементов. Используйте used-set или swap-подход.
</details>

<details>
<summary>Подсказка 2</summary>
Swap-подход: для позиции i попробуйте поставить каждый элемент nums[i..n-1], затем рекурсия для i+1, затем swap обратно.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Backtracking** | **O(n × n!)** | **O(n)** |

---

## 9. Letter Combinations of a Phone Number
**Difficulty:** 🟡 Medium  
**Паттерн:** Backtracking / BFS

### Problem
Дана строка цифр `digits` (от 2 до 9). Верните все возможные комбинации букв, которые эти цифры могут представлять (как на телефонной клавиатуре).

```
2: abc,  3: def,  4: ghi,  5: jkl
6: mno,  7: pqrs, 8: tuv,  9: wxyz
```

### Example 1
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

### Example 2
```
Input: digits = ""
Output: []
```

### Example 3
```
Input: digits = "2"
Output: ["a", "b", "c"]
```

### Constraints
- `0 <= len(digits) <= 4`
- `digits[i]` — цифра от '2' до '9'

### Hints
<details>
<summary>Подсказка 1</summary>
Backtracking: для каждой цифры перебираем все её буквы, добавляя к текущей комбинации. Когда длина = len(digits) → результат.
</details>

<details>
<summary>Подсказка 2</summary>
Создайте словарь маппинга: {'2': 'abc', '3': 'def', ...}. Рекурсивно стройте комбинации.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Backtracking** | **O(4ⁿ)** | **O(n)** |
| BFS / Queue | O(4ⁿ) | O(4ⁿ) |

*n = len(digits), 4 — максимум букв на цифру (7, 9)*

---

## 10. N-Queens
**Difficulty:** 🔴 Hard  
**Паттерн:** Backtracking with Constraints

### Problem
Задача **N ферзей**: расставьте `n` ферзей на шахматной доске `n × n` так, чтобы ни один ферзь **не атаковал** другого (не стоял на одной горизонтали, вертикали или диагонали).

Верните **все различные решения**. Каждое решение — список из `n` строк, где `'Q'` — ферзь, `'.'` — пустая клетка.

### Example 1
```
Input: n = 4
Output: [
  [".Q..","...Q","Q...","..Q."],
  ["..Q.","Q...","...Q",".Q.."]
]
Explanation: Существует ровно 2 различных решения для 4-ферзей.
```

### Example 2
```
Input: n = 1
Output: [["Q"]]
```

### Constraints
- `1 <= n <= 9`

### Hints
<details>
<summary>Подсказка 1</summary>
Размещайте ферзей по одному в каждой строке. Для строки i попробуйте каждый столбец j.
</details>

<details>
<summary>Подсказка 2</summary>
Проверка атак: храните множества занятых столбцов, диагоналей (row-col) и антидиагоналей (row+col).
</details>

<details>
<summary>Подсказка 3</summary>
Если столбец, диагональ и антидиагональ свободны → ставим ферзя, рекурсия для следующей строки, убираем ферзя (backtrack).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Backtracking** | **O(n!)** | **O(n²)** |

### Fun Facts
| n | Решения |
|---|---------|
| 1 | 1 |
| 4 | 2 |
| 5 | 10 |
| 8 | 92 |
| 9 | 352 |
