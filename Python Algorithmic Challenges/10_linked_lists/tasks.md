# 🧩 Linked Lists — Задачи

---

## 1. Reverse Linked List
**Difficulty:** 🟢 Easy

### Problem
Дан связный список. Разверните его и верните новый head.

### Example 1
```
Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
```

### Constraints
- `0 <= количество узлов <= 5000`

---

## 2. Merge Two Sorted Lists
**Difficulty:** 🟢 Easy

### Problem
Даны два отсортированных связных списка. Объедините в один отсортированный.

### Example 1
```
Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
```

### Constraints
- `0 <= количество узлов <= 50`

---

## 3. Linked List Cycle
**Difficulty:** 🟢 Easy

### Problem
Определите, есть ли **цикл** в связном списке. Используйте **O(1)** памяти.

### Example 1
```
Input: head = [3, 2, 0, -4], pos = 1
Output: True
Explanation: Хвост соединён с узлом индекса 1
```

### Constraints
- `0 <= количество узлов <= 10^4`

---

## 4. Middle of the Linked List
**Difficulty:** 🟢 Easy

### Problem
Найдите **средний** узел. Если два средних — верните второй.

### Example 1
```
Input: head = [1, 2, 3, 4, 5]
Output: [3, 4, 5]
```

### Constraints
- `1 <= количество узлов <= 100`

---

## 5. Remove Nth Node From End
**Difficulty:** 🟡 Medium

### Problem
Удалите `n`-й узел с **конца** списка. Сделайте за **один проход**.

### Example 1
```
Input: head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]
```

### Constraints
- `1 <= sz <= 30`
- `1 <= n <= sz`

---

## 6. Add Two Numbers
**Difficulty:** 🟡 Medium

### Problem
Даны два числа как связные списки (цифры в обратном порядке). Верните их сумму как связный список.

### Example 1
```
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]
Explanation: 342 + 465 = 807
```

### Constraints
- `1 <= количество узлов <= 100`

---

## 7. Palindrome Linked List
**Difficulty:** 🟢 Easy

### Problem
Определите, является ли связный список **палиндромом** за O(n) время и O(1) память.

### Example 1
```
Input: head = [1, 2, 2, 1]
Output: True
```

### Constraints
- `1 <= количество узлов <= 10^5`

---

## 8. Intersection of Two Linked Lists
**Difficulty:** 🟢 Easy

### Problem
Найдите узел, в котором два списка **пересекаются**. Если нет — верните `None`.

### Example 1
```
Input: listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Узел со значением 8
```

### Constraints
- `O(m + n)` время, `O(1)` память

---

## 9. Sort List
**Difficulty:** 🟡 Medium

### Problem
Отсортируйте связный список за **O(n log n)** время и **O(1)** память.

### Example 1
```
Input: head = [4, 2, 1, 3]
Output: [1, 2, 3, 4]
```

### Constraints
- `0 <= количество узлов <= 5 * 10^4`

---

## 10. Reorder List
**Difficulty:** 🟡 Medium

### Problem
Дан список `L0 → L1 → ... → Ln`. Перестройте: `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...`

### Example 1
```
Input: head = [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]
```

### Constraints
- `1 <= количество узлов <= 5 * 10^4`
