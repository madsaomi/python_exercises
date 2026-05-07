# 🧩 Binary Search — Задачи

---

## 1. Binary Search
**Difficulty:** 🟢 Easy

### Problem
Дан отсортированный массив `nums` и число `target`. Верните индекс `target` или `-1`.

### Example 1
```
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
```

### Constraints
- `1 <= len(nums) <= 10^4`
- Все элементы уникальны
- `nums` отсортирован

---

## 2. Search Insert Position
**Difficulty:** 🟢 Easy

### Problem
Дан отсортированный массив и `target`. Верните индекс `target` или позицию, куда его следует вставить.

### Example 1
```
Input: nums = [1, 3, 5, 6], target = 5
Output: 2
```

### Example 2
```
Input: nums = [1, 3, 5, 6], target = 2
Output: 1
```

### Constraints
- `1 <= len(nums) <= 10^4`

---

## 3. First Bad Version
**Difficulty:** 🟢 Easy

### Problem
Вы — менеджер продукта. Версия `n` — плохая, если `isBadVersion(n)` возвращает `True`. Найдите **первую** плохую версию, минимизируя вызовы API.

### Example 1
```
Input: n = 5, bad = 4
Output: 4
```

### Constraints
- `1 <= bad <= n <= 2^31 - 1`

---

## 4. Find Minimum in Rotated Sorted Array
**Difficulty:** 🟡 Medium

### Problem
Отсортированный массив был **повёрнут** на `k` позиций. Найдите **минимальный** элемент за O(log n).

### Example 1
```
Input: nums = [3, 4, 5, 1, 2]
Output: 1
```

### Constraints
- `1 <= len(nums) <= 5000`
- Все элементы уникальны

---

## 5. Search in Rotated Sorted Array
**Difficulty:** 🟡 Medium

### Problem
Дан повёрнутый отсортированный массив и `target`. Верните индекс `target` или `-1` за **O(log n)**.

### Example 1
```
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
```

### Constraints
- `1 <= len(nums) <= 5000`
- Все элементы уникальны

---

## 6. Find Peak Element
**Difficulty:** 🟡 Medium

### Problem
Найдите индекс **пикового элемента** (больше соседей) за O(log n).

### Example 1
```
Input: nums = [1, 2, 3, 1]
Output: 2
```

### Constraints
- `1 <= len(nums) <= 1000`
- `nums[i] != nums[i+1]`

---

## 7. Search a 2D Matrix
**Difficulty:** 🟡 Medium

### Problem
Дана матрица `m x n`: строки отсортированы, первый элемент каждой строки > последнего предыдущей. Определите, есть ли `target`.

### Example 1
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: True
```

### Constraints
- `m, n >= 1`
- `m * n <= 10^4`

---

## 8. Koko Eating Bananas
**Difficulty:** 🟡 Medium

### Problem
Коко ест бананы. Дан массив `piles` и `h` часов. Найдите **минимальную скорость** `k` бананов/час, чтобы съесть все за `h` часов.

### Example 1
```
Input: piles = [3, 6, 7, 11], h = 8
Output: 4
```

### Constraints
- `1 <= len(piles) <= 10^4`
- `1 <= h <= 10^9`

---

## 9. Find First and Last Position
**Difficulty:** 🟡 Medium

### Problem
Дан отсортированный массив. Найдите **начальный и конечный** индексы `target`. За O(log n).

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

### Constraints
- `0 <= len(nums) <= 10^5`

---

## 10. Median of Two Sorted Arrays
**Difficulty:** 🔴 Hard

### Problem
Даны два отсортированных массива `nums1` и `nums2`. Найдите **медиану** объединённого массива за **O(log(m+n))**.

### Example 1
```
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.0
```

### Example 2
```
Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5
```

### Constraints
- `0 <= len(nums1), len(nums2) <= 1000`
