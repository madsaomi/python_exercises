# 🧩 Stack & Queue — Задачи

---

## 1. Valid Parentheses
**Difficulty:** 🟢 Easy  
**Паттерн:** Stack

### Problem
Дана строка `s`, содержащая только символы `(`, `)`, `{`, `}`, `[`, `]`. Определите, является ли строка **валидной** скобочной последовательностью.

Правила: каждая открывающая скобка должна быть закрыта соответствующей закрывающей, в правильном порядке.

### Example 1
```
Input: s = "()"
Output: True
```

### Example 2
```
Input: s = "()[]{}"
Output: True
```

### Example 3
```
Input: s = "(]"
Output: False
```

### Example 4
```
Input: s = "([)]"
Output: False
Explanation: Скобки закрыты в неправильном порядке.
```

### Constraints
- `1 <= len(s) <= 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Стек: для каждой открывающей скобки — push. Для закрывающей — pop и проверить соответствие.
</details>

<details>
<summary>Подсказка 2</summary>
Используйте dict для маппинга: {')': '(', ']': '[', '}': '{'}. В конце стек должен быть пуст.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Stack** | **O(n)** | **O(n)** |

---

## 2. Min Stack
**Difficulty:** 🟡 Medium  
**Паттерн:** Auxiliary Stack

### Problem
Реализуйте стек, поддерживающий операции `push`, `pop`, `top` и получение **минимального элемента** — все за **O(1)**.

### Example 1
```
MinStack()
push(-2)  → stack: [-2]
push(0)   → stack: [-2, 0]
push(-3)  → stack: [-2, 0, -3]
getMin()  → -3
pop()     → stack: [-2, 0]
top()     → 0
getMin()  → -2
```

### Constraints
- `-2^31 <= val <= 2^31 - 1`
- `pop`, `top`, `getMin` вызываются только на непустом стеке

### Hints
<details>
<summary>Подсказка 1</summary>
Дополнительный стек min_stack: хранит текущий минимум. push/pop синхронно с основным.
</details>

<details>
<summary>Подсказка 2</summary>
Альтернатива: хранить в основном стеке пары (value, current_min).
</details>

### Approach
| Подход | Время (все операции) | Память |
|--------|---------------------|--------|
| **Two Stacks** | **O(1)** | **O(n)** |

---

## 3. Implement Queue using Stacks
**Difficulty:** 🟢 Easy  
**Паттерн:** Two Stacks (Amortized)

### Problem
Реализуйте очередь (FIFO), используя **только два стека**. Поддерживайте `push`, `pop`, `peek`, `empty`.

### Example 1
```
MyQueue()
push(1)
push(2)
peek()  → 1
pop()   → 1
empty() → False
```

### Constraints
- `1 <= x <= 9`
- Все операции валидны

### Hints
<details>
<summary>Подсказка 1</summary>
in_stack для push, out_stack для pop/peek. Когда out_stack пуст — перекидываем из in_stack.
</details>

<details>
<summary>Подсказка 2</summary>
Amortized O(1): каждый элемент перемещается между стеками максимум 1 раз.
</details>

### Approach
| Подход | Время (amortized) | Память |
|--------|-------------------|--------|
| **Two Stacks** | **O(1)** | **O(n)** |

---

## 4. Implement Stack using Queues
**Difficulty:** 🟢 Easy  
**Паттерн:** Queue Rotation

### Problem
Реализуйте стек (LIFO), используя **только очереди**. Поддерживайте `push`, `pop`, `top`, `empty`.

### Example 1
```
MyStack()
push(1)
push(2)
top()   → 2
pop()   → 2
empty() → False
```

### Constraints
- `1 <= x <= 9`

### Hints
<details>
<summary>Подсказка 1</summary>
При push: добавьте элемент, затем ротируйте очередь n-1 раз (переместите все предыдущие в конец).
</details>

<details>
<summary>Подсказка 2</summary>
После ротации: последний добавленный элемент стоит первым в очереди → pop и peek за O(1).
</details>

### Approach
| Подход | Время (push/pop) | Память |
|--------|------------------|--------|
| **One Queue + Rotation** | **O(n) / O(1)** | **O(n)** |

---

## 5. Evaluate Reverse Polish Notation
**Difficulty:** 🟡 Medium  
**Паттерн:** Stack

### Problem
Вычислите выражение в **обратной польской нотации** (постфиксной).

Операторы: `+`, `-`, `*`, `/`. Деление — целочисленное с округлением к нулю.

### Example 1
```
Input: tokens = ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

### Example 2
```
Input: tokens = ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 4 + 2 = 6
```

### Example 3
```
Input: tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
```

### Constraints
- `1 <= len(tokens) <= 10^4`
- Токен — число или оператор (+, -, *, /)
- Выражение всегда валидно

### Hints
<details>
<summary>Подсказка 1</summary>
Стек: если число → push. Если оператор → pop два числа, применить оператор, push результат.
</details>

<details>
<summary>Подсказка 2</summary>
Осторожно с делением: int(a / b) в Python для округления к нулю (не //!). 6 // -132 = -1, но int(6 / -132) = 0.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Stack** | **O(n)** | **O(n)** |

---

## 6. Daily Temperatures
**Difficulty:** 🟡 Medium  
**Паттерн:** Monotonic Stack (Decreasing)

### Problem
Дан массив `temperatures`, где `temperatures[i]` — температура в i-й день. Верните массив `answer`, где `answer[i]` — через сколько дней будет **теплее**. Если не будет — `0`.

### Example 1
```
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
Explanation: 
  День 0 (73°): следующий теплее → день 1 (74°). Ответ: 1.
  День 2 (75°): следующий теплее → день 6 (76°). Ответ: 4.
```

### Example 2
```
Input: temperatures = [30, 40, 50, 60]
Output: [1, 1, 1, 0]
```

### Example 3
```
Input: temperatures = [30, 60, 90]
Output: [1, 1, 0]
```

### Constraints
- `1 <= len(temperatures) <= 10^5`
- `30 <= temperatures[i] <= 100`

### Hints
<details>
<summary>Подсказка 1</summary>
Монотонный убывающий стек: храните индексы. Когда текущая температура > вершины стека — pop и записать разницу индексов.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n²) | O(1) |
| **Monotonic Stack** | **O(n)** | **O(n)** |

---

## 7. Next Greater Element I
**Difficulty:** 🟢 Easy  
**Паттерн:** Monotonic Stack + Hash Map

### Problem
Даны массивы `nums1` (подмножество `nums2`, без дубликатов). Для каждого элемента `nums1[i]` найдите **следующий больший элемент** в `nums2` (справа от его позиции). Если нет — `-1`.

### Example 1
```
Input: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
Output: [-1, 3, -1]
Explanation:
  4 → в nums2 после 4 нет бо́льших → -1
  1 → в nums2 после 1 идёт 3 (больше) → 3
  2 → в nums2 после 2 ничего нет → -1
```

### Example 2
```
Input: nums1 = [2, 4], nums2 = [1, 2, 3, 4]
Output: [3, -1]
```

### Constraints
- `1 <= len(nums1) <= len(nums2) <= 1000`
- Все элементы уникальны

### Hints
<details>
<summary>Подсказка 1</summary>
Сначала найдите next greater для всех элементов nums2 (monotonic stack). Сохраните в dict. Затем для nums1 — просто lookup.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(m × n) | O(1) |
| **Monotonic Stack + HashMap** | **O(m + n)** | **O(n)** |

---

## 8. Sliding Window Maximum
**Difficulty:** 🔴 Hard  
**Паттерн:** Monotonic Deque

### Problem
Дан массив `nums` и размер окна `k`. Окно скользит слева направо. Верните **максимум** в каждом окне.

### Example 1
```
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]
Explanation:
  Окно [1,3,-1]  → max=3
  Окно [3,-1,-3] → max=3
  Окно [-1,-3,5] → max=5
  Окно [-3,5,3]  → max=5
  Окно [5,3,6]   → max=6
  Окно [3,6,7]   → max=7
```

### Constraints
- `1 <= len(nums) <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= len(nums)`

### Hints
<details>
<summary>Подсказка 1</summary>
Brute force O(nk) — слишком медленно. Используйте deque (двустороннюю очередь).
</details>

<details>
<summary>Подсказка 2</summary>
Monotonic deque: храните индексы в убывающем порядке значений. Вершина deque — максимум текущего окна. Удаляйте элементы, выпавшие из окна.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n × k) | O(1) |
| **Monotonic Deque** | **O(n)** | **O(k)** |

---

## 9. Simplify Path
**Difficulty:** 🟡 Medium  
**Паттерн:** Stack + String Parsing

### Problem
Дан абсолютный Unix-путь. Упростите его до **канонической формы**.

Правила: `..` — вверх, `.` — текущая, множественные `/` → один, убрать trailing `/`.

### Example 1
```
Input: path = "/home/"
Output: "/home"
```

### Example 2
```
Input: path = "/home//foo/"
Output: "/home/foo"
```

### Example 3
```
Input: path = "/a/./b/../../c/"
Output: "/c"
Explanation: /a → /a/b → /a → / → /c
```

### Example 4
```
Input: path = "/../"
Output: "/"
Explanation: Нельзя подняться выше корня.
```

### Constraints
- `1 <= len(path) <= 3000`
- path содержит латинские буквы, цифры, `.`, `/`, `_`

### Hints
<details>
<summary>Подсказка 1</summary>
Split по '/'. Для каждого компонента: '..' → pop из стека, '.' или '' → пропустить, иначе → push.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Stack** | **O(n)** | **O(n)** |

---

## 10. Largest Rectangle in Histogram
**Difficulty:** 🔴 Hard  
**Паттерн:** Monotonic Stack

### Problem
Дан массив `heights` — высоты столбцов гистограммы (ширина каждого = 1). Найдите **площадь наибольшего прямоугольника**, который можно вписать в гистограмму.

### Example 1
```
Input: heights = [2, 1, 5, 6, 2, 3]
Output: 10
Explanation: Прямоугольник высотой 5, шириной 2 (столбцы с индексами 2 и 3). 5 × 2 = 10.
```

### Example 2
```
Input: heights = [2, 4]
Output: 4
```

### Constraints
- `1 <= len(heights) <= 10^5`
- `0 <= heights[i] <= 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Для каждого столбца нужно знать: насколько далеко влево и вправо он может «расшириться» (пока высота >= его высоты).
</details>

<details>
<summary>Подсказка 2</summary>
Monotonic stack (возрастающий): когда встречаем столбец ниже вершины стека — pop, вычисляем площадь для вытолкнутого столбца. Ширина = текущий индекс - новая вершина - 1.
</details>

<details>
<summary>Подсказка 3</summary>
Добавьте sentinel (0) в конец heights, чтобы вытолкнуть все оставшиеся элементы.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n²) | O(1) |
| **Monotonic Stack** | **O(n)** | **O(n)** |
