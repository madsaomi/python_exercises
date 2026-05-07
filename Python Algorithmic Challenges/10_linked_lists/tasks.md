# 🧩 Linked Lists — Задачи

---

## 1. Reverse Linked List
**Difficulty:** 🟢 Easy  
**Паттерн:** Iterative Pointer Reversal

### Problem
Дан односвязный список. Разверните его и верните новый head.

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
Три указателя: prev = None, curr = head. На каждом шаге: next_node = curr.next, curr.next = prev, prev = curr, curr = next_node.
</details>

<details>
<summary>Подсказка 2</summary>
Рекурсивный вариант: дойти до конца, на обратном пути развернуть указатели.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Iterative** | **O(n)** | **O(1)** |
| Recursive | O(n) | O(n) |

---

## 2. Merge Two Sorted Lists
**Difficulty:** 🟢 Easy  
**Паттерн:** Dummy Node + Two Pointers

### Problem
Даны два отсортированных односвязных списка. Объедините их в один отсортированный список, используя узлы исходных списков.

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
- Оба списка отсортированы по неубыванию

### Hints
<details>
<summary>Подсказка 1</summary>
Dummy node: создайте фиктивный узел. Сравнивайте головы списков, присоединяйте меньший.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Iterative (dummy)** | **O(m+n)** | **O(1)** |
| Recursive | O(m+n) | O(m+n) |

---

## 3. Linked List Cycle
**Difficulty:** 🟢 Easy  
**Паттерн:** Floyd's Cycle Detection (Fast & Slow)

### Problem
Определите, есть ли **цикл** в связном списке. Используйте **O(1)** дополнительной памяти.

Цикл: хвост списка указывает на один из предыдущих узлов.

### Example 1
```
Input: head = [3, 2, 0, -4], pos = 1
Output: True
Explanation: Хвост (-4) соединён с узлом индекса 1 (значение 2).
```

### Example 2
```
Input: head = [1, 2], pos = 0
Output: True
```

### Example 3
```
Input: head = [1], pos = -1
Output: False
Explanation: Нет цикла.
```

### Constraints
- `0 <= количество узлов <= 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Floyd's algorithm: slow двигается на 1 шаг, fast на 2. Если есть цикл — они встретятся. Если fast дойдёт до None — цикла нет.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Hash Set | O(n) | O(n) |
| **Fast & Slow Pointers** | **O(n)** | **O(1)** |

---

## 4. Middle of the Linked List
**Difficulty:** 🟢 Easy  
**Паттерн:** Fast & Slow Pointers

### Problem
Найдите **средний** узел списка. Если два средних (чётная длина) — верните **второй**.

### Example 1
```
Input: head = [1, 2, 3, 4, 5]
Output: [3, 4, 5]
Explanation: Средний узел — 3.
```

### Example 2
```
Input: head = [1, 2, 3, 4, 5, 6]
Output: [4, 5, 6]
Explanation: Два средних: 3 и 4. Возвращаем второй (4).
```

### Constraints
- `1 <= количество узлов <= 100`

### Hints
<details>
<summary>Подсказка 1</summary>
slow на 1 шаг, fast на 2. Когда fast дойдёт до конца, slow будет в середине.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Count + find | O(n) два прохода | O(1) |
| **Fast & Slow** | **O(n)** один проход | **O(1)** |

---

## 5. Remove Nth Node From End
**Difficulty:** 🟡 Medium  
**Паттерн:** Two Pointers (Gap)

### Problem
Удалите `n`-й узел с **конца** списка и верните head. Сделайте за **один проход**.

### Example 1
```
Input: head = [1, 2, 3, 4, 5], n = 2
Output: [1, 2, 3, 5]
Explanation: Удалён 2-й с конца (узел 4).
```

### Example 2
```
Input: head = [1], n = 1
Output: []
```

### Example 3
```
Input: head = [1, 2], n = 1
Output: [1]
```

### Constraints
- `1 <= sz <= 30`
- `1 <= n <= sz`

### Hints
<details>
<summary>Подсказка 1</summary>
Два указателя с разрывом n: fast уходит вперёд на n шагов, затем оба двигаются вместе. Когда fast дойдёт до конца — slow на нужной позиции.
</details>

<details>
<summary>Подсказка 2</summary>
Используйте dummy node перед head, чтобы обработать случай удаления первого узла.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Two passes | O(n) | O(1) |
| **One pass (gap pointers)** | **O(n)** | **O(1)** |

---

## 6. Add Two Numbers
**Difficulty:** 🟡 Medium  
**Паттерн:** Elementary Math + Linked List

### Problem
Даны два неотрицательных числа как связные списки (цифры в **обратном** порядке). Каждый узел — одна цифра. Верните сумму как связный список.

### Example 1
```
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]
Explanation: 342 + 465 = 807
```

### Example 2
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

### Example 3
```
Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
Output: [8, 9, 9, 9, 0, 0, 0, 1]
Explanation: 9999999 + 9999 = 10009998
```

### Constraints
- `1 <= количество узлов <= 100`
- `0 <= Node.val <= 9`
- Числа без ведущих нулей (кроме самого 0)

### Hints
<details>
<summary>Подсказка 1</summary>
Поразрядное сложение с carry. Создавайте новые узлы для результата.
</details>

<details>
<summary>Подсказка 2</summary>
Продолжайте, пока l1, l2 или carry не пуст/не равен нулю.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Iterative with carry** | **O(max(m,n))** | **O(max(m,n))** |

---

## 7. Palindrome Linked List
**Difficulty:** 🟢 Easy  
**Паттерн:** Fast & Slow + Reverse

### Problem
Определите, является ли связный список **палиндромом**.

Бонус: решите за O(n) время и **O(1)** память.

### Example 1
```
Input: head = [1, 2, 2, 1]
Output: True
```

### Example 2
```
Input: head = [1, 2]
Output: False
```

### Constraints
- `1 <= количество узлов <= 10^5`
- `0 <= Node.val <= 9`

### Hints
<details>
<summary>Подсказка 1</summary>
1) Найдите середину (fast & slow). 2) Разверните вторую половину. 3) Сравните обе половины.
</details>

<details>
<summary>Подсказка 2</summary>
Не забудьте восстановить список, если это требуется.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Copy to array | O(n) | O(n) |
| **Reverse half + compare** | **O(n)** | **O(1)** |

---

## 8. Intersection of Two Linked Lists
**Difficulty:** 🟢 Easy  
**Паттерн:** Two Pointers (Length Alignment)

### Problem
Найдите узел, в котором два односвязных списка **пересекаются** (сходятся). Если не пересекаются — верните `None`.

### Example 1
```
Input: 
  listA: 4 → 1 ↘
                  8 → 4 → 5
  listB: 5 → 6 → 1 ↗
Output: Node(8)
Explanation: Списки пересекаются в узле со значением 8.
```

### Example 2
```
Input: listA = [2,6,4], listB = [1,5] (no intersection)
Output: None
```

### Constraints
- O(m + n) время, O(1) память

### Hints
<details>
<summary>Подсказка 1</summary>
Два указателя: pA идёт по listA, pB по listB. Когда один доходит до конца — перенаправляем на начало другого списка. Они встретятся в точке пересечения (или оба станут None).
</details>

<details>
<summary>Подсказка 2</summary>
Почему работает: после переключения оба проходят одинаковое расстояние (lenA + lenB).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Hash Set | O(m+n) | O(m) |
| **Two Pointers (switch)** | **O(m+n)** | **O(1)** |

---

## 9. Sort List
**Difficulty:** 🟡 Medium  
**Паттерн:** Merge Sort on Linked List

### Problem
Отсортируйте связный список за **O(n log n)** время. Бонус: O(1) память (не считая рекурсию).

### Example 1
```
Input: head = [4, 2, 1, 3]
Output: [1, 2, 3, 4]
```

### Example 2
```
Input: head = [-1, 5, 3, 4, 0]
Output: [-1, 0, 3, 4, 5]
```

### Example 3
```
Input: head = []
Output: []
```

### Constraints
- `0 <= количество узлов <= 5 * 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Merge Sort идеален для списков: 1) Найти середину (fast & slow). 2) Разделить на два списка. 3) Рекурсивно отсортировать. 4) Merge.
</details>

<details>
<summary>Подсказка 2</summary>
Для O(1) памяти: Bottom-up merge sort (итеративный) — объединяем пары подсписков длины 1, 2, 4, 8, ...
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Top-down Merge Sort** | **O(n log n)** | **O(log n)** стек |
| Bottom-up Merge Sort | O(n log n) | O(1) |

---

## 10. Reorder List
**Difficulty:** 🟡 Medium  
**Паттерн:** Find Middle + Reverse + Merge

### Problem
Дан список `L0 → L1 → ... → Ln-1 → Ln`.  
Перестройте в: `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...`

Нельзя изменять значения — только переставлять узлы.

### Example 1
```
Input: head = [1, 2, 3, 4]
Output: [1, 4, 2, 3]
```

### Example 2
```
Input: head = [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]
```

### Constraints
- `1 <= количество узлов <= 5 * 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Три шага: 1) Найти середину (fast & slow). 2) Развернуть вторую половину. 3) Объединить (merge/interleave) обе половины.
</details>

<details>
<summary>Подсказка 2</summary>
Пример [1,2,3,4,5]: середина=3. Вторая половина [4,5] → reversed [5,4]. Merge: 1→5→2→4→3.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Copy to array | O(n) | O(n) |
| **Middle + Reverse + Merge** | **O(n)** | **O(1)** |
