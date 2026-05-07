# 🧩 Binary Search — Задачи

---

## 1. Binary Search
**Difficulty:** 🟢 Easy  
**Паттерн:** Classic Binary Search

### Problem
Дан отсортированный массив `nums` (по возрастанию) и целое число `target`. Верните индекс `target` или `-1`, если не найден.

Решение должно работать за **O(log n)**.

### Example 1
```
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
```

### Example 2
```
Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
```

### Constraints
- `1 <= len(nums) <= 10^4`
- Все элементы уникальны
- `nums` отсортирован по возрастанию

### Hints
<details>
<summary>Подсказка 1</summary>
left = 0, right = len-1. mid = (left + right) // 2. Сравнивайте nums[mid] с target и сужайте поиск.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Linear Search | O(n) | O(1) |
| **Binary Search** | **O(log n)** | **O(1)** |

---

## 2. Search Insert Position
**Difficulty:** 🟢 Easy  
**Паттерн:** Binary Search (leftmost)

### Problem
Дан отсортированный массив уникальных чисел и `target`. Верните индекс `target`. Если не найден — верните индекс, куда его следует вставить, чтобы массив остался отсортированным.

Решение за **O(log n)**.

### Example 1
```
Input: nums = [1, 3, 5, 6], target = 5
Output: 2
```

### Example 2
```
Input: nums = [1, 3, 5, 6], target = 2
Output: 1
Explanation: 2 нужно вставить на позицию 1 (между 1 и 3).
```

### Example 3
```
Input: nums = [1, 3, 5, 6], target = 7
Output: 4
Explanation: Вставить в конец.
```

### Constraints
- `1 <= len(nums) <= 10^4`
- Все элементы уникальны
- `nums` отсортирован

### Hints
<details>
<summary>Подсказка 1</summary>
Это bisect_left: найти первый индекс, где nums[i] >= target.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Binary Search** | **O(log n)** | **O(1)** |

---

## 3. First Bad Version
**Difficulty:** 🟢 Easy  
**Паттерн:** Binary Search on Condition

### Problem
Вы менеджер продукта. Есть `n` версий `[1, 2, ..., n]`. Начиная с какой-то версии, все последующие — «плохие». Дана функция `isBadVersion(version)`.

Найдите **первую плохую версию**, минимизируя количество вызовов API.

### Example 1
```
Input: n = 5, bad = 4
Output: 4
Explanation: 
  isBadVersion(3) → False
  isBadVersion(5) → True
  isBadVersion(4) → True → ответ 4
```

### Example 2
```
Input: n = 1, bad = 1
Output: 1
```

### Constraints
- `1 <= bad <= n <= 2^31 - 1`

### Hints
<details>
<summary>Подсказка 1</summary>
Бинарный поиск: ищем leftmost True. Если isBadVersion(mid) → right = mid. Иначе left = mid + 1.
</details>

<details>
<summary>Подсказка 2</summary>
Осторожно с overflow: mid = left + (right - left) // 2 вместо (left + right) // 2.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Linear | O(n) | O(1) |
| **Binary Search** | **O(log n)** | **O(1)** |

---

## 4. Find Minimum in Rotated Sorted Array
**Difficulty:** 🟡 Medium  
**Паттерн:** Modified Binary Search

### Problem
Отсортированный массив уникальных элементов был **повёрнут** на `k` позиций (неизвестно сколько).

Например: `[0,1,2,4,5,6,7]` → повёрнут на 4 → `[4,5,6,7,0,1,2]`.

Найдите **минимальный элемент** за O(log n).

### Example 1
```
Input: nums = [3, 4, 5, 1, 2]
Output: 1
```

### Example 2
```
Input: nums = [4, 5, 6, 7, 0, 1, 2]
Output: 0
```

### Example 3
```
Input: nums = [11, 13, 15, 17]
Output: 11
Explanation: Массив не был повёрнут (или повёрнут на 0).
```

### Constraints
- `1 <= len(nums) <= 5000`
- Все элементы уникальны

### Hints
<details>
<summary>Подсказка 1</summary>
Если nums[mid] > nums[right] → минимум в правой половине. Иначе — в левой (включая mid).
</details>

<details>
<summary>Подсказка 2</summary>
Остановка: left == right → nums[left] — минимум.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Linear | O(n) | O(1) |
| **Binary Search** | **O(log n)** | **O(1)** |

---

## 5. Search in Rotated Sorted Array
**Difficulty:** 🟡 Medium  
**Паттерн:** Modified Binary Search

### Problem
Дан повёрнутый отсортированный массив уникальных элементов и `target`. Верните индекс `target` или `-1`.

Решение за **O(log n)**.

### Example 1
```
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
```

### Example 2
```
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
Output: -1
```

### Example 3
```
Input: nums = [1], target = 0
Output: -1
```

### Constraints
- `1 <= len(nums) <= 5000`
- Все элементы уникальны

### Hints
<details>
<summary>Подсказка 1</summary>
Определите, какая половина отсортирована: если nums[left] <= nums[mid] → левая отсортирована.
</details>

<details>
<summary>Подсказка 2</summary>
Если target в отсортированной половине → ищите там. Иначе → в другой половине.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Modified Binary Search** | **O(log n)** | **O(1)** |

---

## 6. Find Peak Element
**Difficulty:** 🟡 Medium  
**Паттерн:** Binary Search on Peaks

### Problem
Пиковый элемент — строго больше своих соседей. Найдите индекс **любого** пикового элемента за O(log n).

`nums[-1] = nums[n] = -∞` (за границами — минус бесконечность).

### Example 1
```
Input: nums = [1, 2, 3, 1]
Output: 2
Explanation: nums[2] = 3 > nums[1] = 2 и nums[3] = 1. Пик.
```

### Example 2
```
Input: nums = [1, 2, 1, 3, 5, 6, 4]
Output: 5 (или 1)
Explanation: nums[5] = 6 — пик. nums[1] = 2 тоже пик.
```

### Constraints
- `1 <= len(nums) <= 1000`
- `nums[i] != nums[i+1]` для всех i

### Hints
<details>
<summary>Подсказка 1</summary>
Если nums[mid] < nums[mid+1] → пик правее (двигаем left). Иначе → пик левее или mid сам пик (двигаем right).
</details>

<details>
<summary>Подсказка 2</summary>
Почему это работает? Если мы двигаемся в сторону бо́льшего соседа, мы гарантированно найдём пик (или упрёмся в край).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Linear | O(n) | O(1) |
| **Binary Search** | **O(log n)** | **O(1)** |

---

## 7. Search a 2D Matrix
**Difficulty:** 🟡 Medium  
**Паттерн:** Binary Search (2D → 1D)

### Problem
Дана матрица `m × n` с двумя свойствами:
1. Каждая строка отсортирована по возрастанию
2. Первый элемент каждой строки > последнего элемента предыдущей

Определите, содержит ли матрица `target`.

### Example 1
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: True
```

### Example 2
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: False
```

### Constraints
- `m, n >= 1`
- `m * n <= 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Представьте матрицу как плоский отсортированный массив длины m*n. index → row = index // n, col = index % n.
</details>

<details>
<summary>Подсказка 2</summary>
Или два бинарных поиска: сначала найдите нужную строку, потом элемент в строке.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Binary Search (flat)** | **O(log(m × n))** | **O(1)** |

---

## 8. Koko Eating Bananas
**Difficulty:** 🟡 Medium  
**Паттерн:** Binary Search on Answer

### Problem
Коко любит бананы. Есть `n` куч бананов, `piles[i]` — размер i-й кучи. Охранник вернётся через `h` часов.

Коко ест со скоростью `k` бананов/час. Каждый час выбирает кучу и ест k бананов (если в куче < k — доедает и ждёт).

Найдите **минимальную** скорость `k`, чтобы съесть все бананы за `h` часов.

### Example 1
```
Input: piles = [3, 6, 7, 11], h = 8
Output: 4
Explanation: При k=4: ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4) = 1+2+2+3 = 8 ≤ 8 ✓
```

### Example 2
```
Input: piles = [30, 11, 23, 4, 20], h = 5
Output: 30
```

### Example 3
```
Input: piles = [30, 11, 23, 4, 20], h = 6
Output: 23
```

### Constraints
- `1 <= len(piles) <= 10^4`
- `1 <= piles[i] <= 10^9`
- `len(piles) <= h <= 10^9`

### Hints
<details>
<summary>Подсказка 1</summary>
Бинарный поиск по ответу! left = 1, right = max(piles). Для данного k проверяем: успеет ли за h часов?
</details>

<details>
<summary>Подсказка 2</summary>
Часов для кучи: ceil(pile / k) = (pile + k - 1) // k. Если total_hours <= h → k достаточно, ищем меньше.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Binary Search on Answer** | **O(n × log(max_pile))** | **O(1)** |

---

## 9. Find First and Last Position
**Difficulty:** 🟡 Medium  
**Паттерн:** Binary Search (leftmost + rightmost)

### Problem
Дан отсортированный массив `nums` и `target`. Найдите **начальный и конечный** индексы `target`. Если не найден — `[-1, -1]`.

Решение за **O(log n)**.

### Example 1
```
Input: nums = [5, 7, 7, 8, 8, 10], target = 8
Output: [3, 4]
```

### Example 2
```
Input: nums = [5, 7, 7, 8, 8, 10], target = 6
Output: [-1, -1]
```

### Example 3
```
Input: nums = [], target = 0
Output: [-1, -1]
```

### Constraints
- `0 <= len(nums) <= 10^5`

### Hints
<details>
<summary>Подсказка 1</summary>
Два отдельных бинарных поиска: один для leftmost (первое вхождение), другой для rightmost (последнее).
</details>

<details>
<summary>Подсказка 2</summary>
Leftmost: если nums[mid] >= target → right = mid. Rightmost: если nums[mid] <= target → left = mid.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Linear | O(n) | O(1) |
| **Two Binary Searches** | **O(log n)** | **O(1)** |

---

## 10. Median of Two Sorted Arrays
**Difficulty:** 🔴 Hard  
**Паттерн:** Binary Search on Partition

### Problem
Даны два отсортированных массива `nums1` (длина m) и `nums2` (длина n). Найдите **медиану** объединённого отсортированного массива.

Решение за **O(log(m+n))**.

### Example 1
```
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.0
Explanation: Объединённый: [1, 2, 3]. Медиана = 2.
```

### Example 2
```
Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5
Explanation: Объединённый: [1, 2, 3, 4]. Медиана = (2+3)/2 = 2.5.
```

### Example 3
```
Input: nums1 = [], nums2 = [1]
Output: 1.0
```

### Constraints
- `0 <= m, n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

### Hints
<details>
<summary>Подсказка 1</summary>
Наивный подход: merge + find median → O(m+n). Но нужно O(log(m+n)).
</details>

<details>
<summary>Подсказка 2</summary>
Бинарный поиск по разделению меньшего массива. Разделите оба массива на левую и правую части, чтобы |left| == |right| и max(left) <= min(right).
</details>

<details>
<summary>Подсказка 3</summary>
Ищите partition в меньшем массиве (O(log min(m,n))). partition2 = (m+n+1)//2 - partition1. Проверяйте условия перекрёстных границ.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Merge + Find | O(m + n) | O(m + n) |
| **Binary Search** | **O(log min(m,n))** | **O(1)** |
