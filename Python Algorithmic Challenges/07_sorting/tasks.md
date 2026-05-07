# 🧩 Sorting — Задачи

---

## 1. Sort an Array
**Difficulty:** 🟡 Medium

### Problem
Дан массив `nums`. Отсортируйте его по возрастанию. Реализуйте **Merge Sort** или **Quick Sort** (не используйте `sort()`).

### Example 1
```
Input: nums = [5, 2, 3, 1]
Output: [1, 2, 3, 5]
```

### Constraints
- `1 <= len(nums) <= 5 * 10^4`

---

## 2. Merge Intervals
**Difficulty:** 🟡 Medium

### Problem
Дан массив интервалов `intervals[i] = [start, end]`. Объедините пересекающиеся интервалы.

### Example 1
```
Input: intervals = [[1,3], [2,6], [8,10], [15,18]]
Output: [[1,6], [8,10], [15,18]]
```

### Constraints
- `1 <= len(intervals) <= 10^4`

---

## 3. Sort Colors (Dutch National Flag)
**Difficulty:** 🟡 Medium

### Problem
Дан массив из `0`, `1`, `2`. Отсортируйте **in-place** за один проход без `sort()`.

### Example 1
```
Input: nums = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
```

### Constraints
- `1 <= len(nums) <= 300`

---

## 4. Kth Largest Element
**Difficulty:** 🟡 Medium

### Problem
Найдите `k`-й по величине элемент в массиве. Используйте **Quick Select**.

### Example 1
```
Input: nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
```

### Constraints
- `1 <= k <= len(nums) <= 10^5`

---

## 5. Valid Anagram (Sorting Approach)
**Difficulty:** 🟢 Easy

### Problem
Определите, является ли строка `t` анаграммой `s` с помощью **сортировки**.

### Example 1
```
Input: s = "anagram", t = "nagaram"
Output: True
```

### Constraints
- `1 <= len(s), len(t) <= 5 * 10^4`

---

## 6. Largest Number
**Difficulty:** 🟡 Medium

### Problem
Дан массив чисел. Расположите их так, чтобы получилось **максимальное число** (как строка).

### Example 1
```
Input: nums = [10, 2]
Output: "210"
```

### Example 2
```
Input: nums = [3, 30, 34, 5, 9]
Output: "9534330"
```

### Constraints
- `1 <= len(nums) <= 100`

---

## 7. Meeting Rooms
**Difficulty:** 🟢 Easy

### Problem
Дан массив интервалов встреч `[start, end]`. Может ли человек посетить **все** встречи?

### Example 1
```
Input: intervals = [[0,30], [5,10], [15,20]]
Output: False
```

### Example 2
```
Input: intervals = [[7,10], [2,4]]
Output: True
```

### Constraints
- `0 <= len(intervals) <= 10^4`

---

## 8. Insert Interval
**Difficulty:** 🟡 Medium

### Problem
Даны **неперекрывающиеся** отсортированные интервалы и новый интервал. Вставьте новый, объединив при необходимости.

### Example 1
```
Input: intervals = [[1,3], [6,9]], newInterval = [2,5]
Output: [[1,5], [6,9]]
```

### Constraints
- `0 <= len(intervals) <= 10^4`

---

## 9. H-Index
**Difficulty:** 🟡 Medium

### Problem
Дан массив цитирований учёного. Вычислите **h-индекс** (максимальное `h`, при котором h статей имеют ≥ h цитирований).

### Example 1
```
Input: citations = [3, 0, 6, 1, 5]
Output: 3
```

### Constraints
- `1 <= len(citations) <= 5000`

---

## 10. Wiggle Sort II
**Difficulty:** 🟡 Medium

### Problem
Дан массив `nums`. Переставьте его так, чтобы `nums[0] < nums[1] > nums[2] < nums[3] > ...`

### Example 1
```
Input: nums = [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
```

### Constraints
- `1 <= len(nums) <= 5 * 10^4`
