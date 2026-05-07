# 🧩 Sorting — Задачи

---

## 1. Sort an Array
**Difficulty:** 🟡 Medium  
**Паттерн:** Merge Sort / Quick Sort

### Problem
Дан массив целых чисел `nums`. Отсортируйте по возрастанию.  
Реализуйте **Merge Sort** или **Quick Sort** (не используйте встроенный `sort()`).

### Example 1
```
Input: nums = [5, 2, 3, 1]
Output: [1, 2, 3, 5]
```

### Example 2
```
Input: nums = [5, 1, 1, 2, 0, 0]
Output: [0, 0, 1, 1, 2, 5]
```

### Constraints
- `1 <= len(nums) <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

### Hints
<details>
<summary>Подсказка 1 (Merge Sort)</summary>
Разделите массив пополам, рекурсивно отсортируйте обе половины, затем слейте (merge) два отсортированных массива.
</details>

<details>
<summary>Подсказка 2 (Quick Sort)</summary>
Выберите pivot, разделите массив на элементы < pivot и > pivot. Рекурсивно отсортируйте обе части. Осторожно: worst case O(n²) при плохом pivot!
</details>

### Approach
| Подход | Время (avg) | Время (worst) | Память | Стабильный? |
|--------|-------------|---------------|--------|-------------|
| **Merge Sort** | **O(n log n)** | **O(n log n)** | **O(n)** | ✅ Да |
| Quick Sort | O(n log n) | O(n²) | O(log n) | ❌ Нет |
| Heap Sort | O(n log n) | O(n log n) | O(1) | ❌ Нет |

---

## 2. Merge Intervals
**Difficulty:** 🟡 Medium  
**Паттерн:** Sort + Linear Scan

### Problem
Дан массив интервалов `intervals`, где `intervals[i] = [start_i, end_i]`. Объедините все пересекающиеся интервалы и верните массив непересекающихся интервалов, покрывающих все входные.

### Example 1
```
Input: intervals = [[1,3], [2,6], [8,10], [15,18]]
Output: [[1,6], [8,10], [15,18]]
Explanation: [1,3] и [2,6] пересекаются → [1,6].
```

### Example 2
```
Input: intervals = [[1,4], [4,5]]
Output: [[1,5]]
Explanation: [1,4] и [4,5] соприкасаются → [1,5].
```

### Example 3
```
Input: intervals = [[1,4], [0,4]]
Output: [[0,4]]
```

### Constraints
- `1 <= len(intervals) <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Отсортируйте интервалы по start. Затем пройдитесь: если текущий пересекается с последним в результате — объедините (расширьте end).
</details>

<details>
<summary>Подсказка 2</summary>
Два интервала пересекаются, если start текущего <= end предыдущего.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Sort + Merge** | **O(n log n)** | **O(n)** |

---

## 3. Sort Colors (Dutch National Flag)
**Difficulty:** 🟡 Medium  
**Паттерн:** Three-Way Partition / Two Pointers

### Problem
Дан массив из элементов `0`, `1` и `2` (красный, белый, синий). Отсортируйте **in-place** так, чтобы одинаковые цвета шли подряд: 0, 1, 2.

Решите за **один проход** без использования `sort()`.

### Example 1
```
Input: nums = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
```

### Example 2
```
Input: nums = [2, 0, 1]
Output: [0, 1, 2]
```

### Constraints
- `1 <= len(nums) <= 300`
- `nums[i]` ∈ {0, 1, 2}

### Hints
<details>
<summary>Подсказка 1</summary>
Алгоритм «голландского флага» Дейкстры: три указателя — low, mid, high.
</details>

<details>
<summary>Подсказка 2</summary>
low = 0 (граница 0/1), mid = 0 (текущий), high = n-1 (граница 1/2).
Если nums[mid] == 0: swap с low, low++, mid++.
Если nums[mid] == 1: mid++.
Если nums[mid] == 2: swap с high, high--.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Counting Sort | O(n) два прохода | O(1) |
| **Dutch National Flag** | **O(n)** один проход | **O(1)** |

---

## 4. Kth Largest Element
**Difficulty:** 🟡 Medium  
**Паттерн:** Quick Select / Heap

### Problem
Дан массив `nums` и число `k`. Найдите `k`-й по величине элемент.

Это `k`-й **по величине**, не `k`-й уникальный.

### Example 1
```
Input: nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
Explanation: Отсортированный: [1,2,3,4,5,6]. 2-й с конца = 5.
```

### Example 2
```
Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

### Constraints
- `1 <= k <= len(nums) <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Quick Select: partition массива (как в Quick Sort). Если pivot на нужной позиции — ответ. Иначе рекурсия в одну сторону.
</details>

<details>
<summary>Подсказка 2</summary>
Heap: используйте min-heap размера k. В конце вершина = k-й по величине.
</details>

### Approach
| Подход | Время (avg) | Время (worst) | Память |
|--------|-------------|---------------|--------|
| Sort | O(n log n) | O(n log n) | O(n) |
| **Quick Select** | **O(n)** | O(n²) | **O(1)** |
| Min Heap | O(n log k) | O(n log k) | O(k) |

---

## 5. Valid Anagram (Sorting Approach)
**Difficulty:** 🟢 Easy  
**Паттерн:** Sorting + Comparison

### Problem
Определите, является ли строка `t` анаграммой `s` с помощью **сортировки**.

Анаграмма — строка, полученная перестановкой букв другой строки.

### Example 1
```
Input: s = "anagram", t = "nagaram"
Output: True
Explanation: sorted("anagram") == sorted("nagaram") == "aaagmnr"
```

### Example 2
```
Input: s = "rat", t = "car"
Output: False
```

### Constraints
- `1 <= len(s), len(t) <= 5 * 10^4`
- Только строчные латинские буквы

### Hints
<details>
<summary>Подсказка 1</summary>
Отсортируйте обе строки и сравните. Если равны — анаграмма.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Sorting** | **O(n log n)** | **O(n)** |
| Counter (альт.) | O(n) | O(1) |

---

## 6. Largest Number
**Difficulty:** 🟡 Medium  
**Паттерн:** Custom Comparator Sort

### Problem
Дан список неотрицательных целых чисел `nums`. Расположите их так, чтобы образовалось **наибольшее возможное число**. Верните результат как строку.

### Example 1
```
Input: nums = [10, 2]
Output: "210"
Explanation: "210" > "102"
```

### Example 2
```
Input: nums = [3, 30, 34, 5, 9]
Output: "9534330"
```

### Example 3
```
Input: nums = [0, 0]
Output: "0"
Explanation: Не "00", а "0"!
```

### Constraints
- `1 <= len(nums) <= 100`
- `0 <= nums[i] <= 10^9`

### Hints
<details>
<summary>Подсказка 1</summary>
Кастомный компаратор: сравнивайте a+b vs b+a (как строки). Если "330" > "303" → 3 идёт перед 30.
</details>

<details>
<summary>Подсказка 2</summary>
Используйте functools.cmp_to_key для передачи компаратора в sorted().
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Custom Sort** | **O(n log n × k)** | **O(n × k)** |

*k = средняя длина числа в строковом представлении*

---

## 7. Meeting Rooms
**Difficulty:** 🟢 Easy  
**Паттерн:** Sort + Linear Scan

### Problem
Дан массив интервалов встреч `intervals[i] = [start_i, end_i]`. Определите, может ли человек посетить **все** встречи (нет пересечений).

### Example 1
```
Input: intervals = [[0,30], [5,10], [15,20]]
Output: False
Explanation: [0,30] пересекается с [5,10] и [15,20].
```

### Example 2
```
Input: intervals = [[7,10], [2,4]]
Output: True
```

### Example 3
```
Input: intervals = []
Output: True
```

### Constraints
- `0 <= len(intervals) <= 10^4`
- `0 <= start_i < end_i <= 10^6`

### Hints
<details>
<summary>Подсказка 1</summary>
Отсортируйте по start. Проверьте: если start[i] < end[i-1] → пересечение.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Sort + Scan** | **O(n log n)** | **O(1)** |

---

## 8. Insert Interval
**Difficulty:** 🟡 Medium  
**Паттерн:** Linear Scan + Merge

### Problem
Даны **неперекрывающиеся** интервалы, отсортированные по start. Вставьте новый интервал, объединяя пересекающиеся при необходимости. Верните результат.

### Example 1
```
Input: intervals = [[1,3], [6,9]], newInterval = [2,5]
Output: [[1,5], [6,9]]
Explanation: [1,3] и [2,5] пересекаются → [1,5].
```

### Example 2
```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: [3,5], [6,7], [8,10] объединяются с [4,8] → [3,10].
```

### Constraints
- `0 <= len(intervals) <= 10^4`
- `intervals` отсортированы и не пересекаются

### Hints
<details>
<summary>Подсказка 1</summary>
Три фазы: 1) Добавить все интервалы, которые заканчиваются ДО нового. 2) Объединить все пересекающиеся с новым. 3) Добавить оставшиеся.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Three-phase scan** | **O(n)** | **O(n)** |

---

## 9. H-Index
**Difficulty:** 🟡 Medium  
**Паттерн:** Sorting / Counting Sort

### Problem
Дан массив `citations`, где `citations[i]` — количество цитирований i-й статьи. Вычислите **h-индекс** учёного.

h-индекс: максимальное `h`, при котором **h статей** имеют **≥ h** цитирований.

### Example 1
```
Input: citations = [3, 0, 6, 1, 5]
Output: 3
Explanation: 3 статьи (с 3, 6, 5 цитированиями) имеют ≥ 3 цитирований.
```

### Example 2
```
Input: citations = [1, 3, 1]
Output: 1
```

### Constraints
- `1 <= len(citations) <= 5000`
- `0 <= citations[i] <= 1000`

### Hints
<details>
<summary>Подсказка 1</summary>
Отсортируйте по убыванию. h-индекс = максимальный i+1, при котором citations[i] >= i+1.
</details>

<details>
<summary>Подсказка 2</summary>
Для O(n): counting sort. Создайте массив counts[0..n]. counts[i] = сколько статей имеют ровно i цитирований (citations >= n → counts[n]). Пройдите справа.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Sort + Scan** | **O(n log n)** | **O(1)** |
| Counting Sort | O(n) | O(n) |

---

## 10. Wiggle Sort II
**Difficulty:** 🟡 Medium  
**Паттерн:** Sort + Interleave

### Problem
Дан массив целых чисел `nums`. Переставьте его так, чтобы:  
`nums[0] < nums[1] > nums[2] < nums[3] > nums[4] < ...`

### Example 1
```
Input: nums = [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
Explanation: 1<6>1<5>1<4 ✓
```

### Example 2
```
Input: nums = [1, 3, 2, 2, 3, 1]
Output: [2, 3, 1, 3, 1, 2]
```

### Constraints
- `1 <= len(nums) <= 5 * 10^4`
- `0 <= nums[i] <= 5000`
- Гарантируется, что ответ существует

### Hints
<details>
<summary>Подсказка 1</summary>
Отсортируйте. Разделите на две половины: малые и большие. Чередуйте: малый, большой, малый, большой...
</details>

<details>
<summary>Подсказка 2</summary>
Важно: берите из конца каждой половины, чтобы дубликаты не оказались рядом. Пример: sorted = [1,1,1,4,5,6] → small=[1,1,1], big=[4,5,6] → [1,6,1,5,1,4].
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Sort + Interleave** | **O(n log n)** | **O(n)** |
| Quick Select + 3-way partition | O(n) avg | O(1) |
