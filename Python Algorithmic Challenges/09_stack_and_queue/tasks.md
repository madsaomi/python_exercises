# 🧩 Stack & Queue — Задачи

---

## 1. Valid Parentheses
**Difficulty:** 🟢 Easy

### Problem
Дана строка, содержащая `(`, `)`, `{`, `}`, `[`, `]`. Определите, является ли строка **валидной** скобочной последовательностью.

### Example 1
```
Input: s = "()[]{}"
Output: True
```

### Example 2
```
Input: s = "(]"
Output: False
```

### Constraints
- `1 <= len(s) <= 10^4`

---

## 2. Min Stack
**Difficulty:** 🟡 Medium

### Problem
Реализуйте стек, поддерживающий `push`, `pop`, `top` и `getMin` — все за **O(1)**.

### Example 1
```
MinStack minStack = new MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()  → -3
minStack.pop()
minStack.top()     → 0
minStack.getMin()  → -2
```

### Constraints
- `-2^31 <= val <= 2^31 - 1`

---

## 3. Implement Queue using Stacks
**Difficulty:** 🟢 Easy

### Problem
Реализуйте очередь (FIFO), используя **только два стека**.

### Example 1
```
queue.push(1)
queue.push(2)
queue.peek()  → 1
queue.pop()   → 1
queue.empty() → False
```

### Constraints
- `1 <= x <= 9`

---

## 4. Implement Stack using Queues
**Difficulty:** 🟢 Easy

### Problem
Реализуйте стек (LIFO), используя **только очереди**.

### Example 1
```
stack.push(1)
stack.push(2)
stack.top()   → 2
stack.pop()   → 2
stack.empty() → False
```

### Constraints
- `1 <= x <= 9`

---

## 5. Evaluate Reverse Polish Notation
**Difficulty:** 🟡 Medium

### Problem
Вычислите выражение в **обратной польской нотации** (постфиксной).

### Example 1
```
Input: tokens = ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

### Constraints
- `1 <= len(tokens) <= 10^4`
- Токен — число или оператор (+, -, *, /)

---

## 6. Daily Temperatures
**Difficulty:** 🟡 Medium

### Problem
Дан массив температур. Для каждого дня найдите, **через сколько дней** будет теплее. Если не будет — `0`.

### Example 1
```
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

### Constraints
- `1 <= len(temperatures) <= 10^5`

---

## 7. Next Greater Element I
**Difficulty:** 🟢 Easy

### Problem
Даны массивы `nums1` (подмножество `nums2`). Для каждого элемента `nums1` найдите **следующий больший** в `nums2`. Если нет — `-1`.

### Example 1
```
Input: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
Output: [-1, 3, -1]
```

### Constraints
- `1 <= len(nums1) <= len(nums2) <= 1000`

---

## 8. Sliding Window Maximum
**Difficulty:** 🔴 Hard

### Problem
Дан массив `nums` и размер окна `k`. Верните **максимум** в каждом окне размера `k`.

### Example 1
```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
```

### Constraints
- `1 <= len(nums) <= 10^5`

---

## 9. Simplify Path
**Difficulty:** 🟡 Medium

### Problem
Дан абсолютный путь Unix. Упростите его (каноническая форма).

### Example 1
```
Input: path = "/home//foo/"
Output: "/home/foo"
```

### Example 2
```
Input: path = "/../"
Output: "/"
```

### Constraints
- `1 <= len(path) <= 3000`

---

## 10. Largest Rectangle in Histogram
**Difficulty:** 🔴 Hard

### Problem
Дан массив `heights` — высоты столбцов гистограммы (ширина 1). Найдите **площадь наибольшего** прямоугольника.

### Example 1
```
Input: heights = [2, 1, 5, 6, 2, 3]
Output: 10
Explanation: Прямоугольник высотой 5, шириной 2 (столбцы 2-3)
```

### Constraints
- `1 <= len(heights) <= 10^5`
