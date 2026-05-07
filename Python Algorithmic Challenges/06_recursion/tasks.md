# 🧩 Recursion — Задачи

---

## 1. Fibonacci Number
**Difficulty:** 🟢 Easy

### Problem
Вычислите `n`-е число Фибоначчи. `F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)`.

### Example 1
```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3
```

### Constraints
- `0 <= n <= 30`

---

## 2. Power of Two
**Difficulty:** 🟢 Easy

### Problem
Определите, является ли число `n` степенью двойки. Решите **рекурсивно**.

### Example 1
```
Input: n = 16
Output: True
```

### Constraints
- `-2^31 <= n <= 2^31 - 1`

---

## 3. Reverse Linked List (Recursive)
**Difficulty:** 🟢 Easy

### Problem
Дан связный список. Разверните его **рекурсивно**.

### Example 1
```
Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

### Constraints
- `0 <= количество узлов <= 5000`

---

## 4. Merge Two Sorted Lists (Recursive)
**Difficulty:** 🟢 Easy

### Problem
Даны два отсортированных связных списка. Объедините их в один рекурсивно.

### Example 1
```
Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
```

### Constraints
- `0 <= количество узлов <= 50`

---

## 5. Climbing Stairs
**Difficulty:** 🟢 Easy

### Problem
Вы поднимаетесь на `n` ступенек. Каждый раз можно подняться на 1 или 2 ступеньки. Сколько различных способов добраться до вершины?

### Example 1
```
Input: n = 3
Output: 3
Explanation: 1+1+1, 1+2, 2+1
```

### Constraints
- `1 <= n <= 45`

---

## 6. Generate Parentheses
**Difficulty:** 🟡 Medium

### Problem
Дано `n` пар скобок. Сгенерируйте **все комбинации** правильных скобочных последовательностей.

### Example 1
```
Input: n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

### Constraints
- `1 <= n <= 8`

---

## 7. Subsets
**Difficulty:** 🟡 Medium

### Problem
Дан массив **уникальных** целых чисел `nums`. Верните **все подмножества** (power set).

### Example 1
```
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
```

### Constraints
- `1 <= len(nums) <= 10`

---

## 8. Permutations
**Difficulty:** 🟡 Medium

### Problem
Дан массив **уникальных** чисел `nums`. Верните **все перестановки**.

### Example 1
```
Input: nums = [1, 2, 3]
Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

### Constraints
- `1 <= len(nums) <= 6`

---

## 9. Letter Combinations of a Phone Number
**Difficulty:** 🟡 Medium

### Problem
Дана строка цифр `digits` (2-9). Верните все возможные комбинации букв, которые эти цифры могут представлять (как на телефоне).

### Example 1
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

### Constraints
- `0 <= len(digits) <= 4`

---

## 10. N-Queens
**Difficulty:** 🔴 Hard

### Problem
Расставьте `n` ферзей на доске `n x n` так, чтобы ни один ферзь **не атаковал** другого. Верните все решения.

### Example 1
```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
```

### Constraints
- `1 <= n <= 9`
