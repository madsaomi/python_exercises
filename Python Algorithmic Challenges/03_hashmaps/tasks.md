# 🧩 Hashmaps — Задачи

---

## 1. Two Sum (HashMap Approach)
**Difficulty:** 🟢 Easy

### Problem
Дан массив `nums` и число `target`. Верните индексы двух чисел, дающих `target`. Решите за **O(n)** с помощью хеш-таблицы.

### Example 1
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

### Constraints
- `2 <= len(nums) <= 10^4`
- Ровно одно решение

---

## 2. Valid Anagram
**Difficulty:** 🟢 Easy

### Problem
Даны строки `s` и `t`. Верните `True`, если `t` — анаграмма `s`. Используйте хеш-таблицу.

### Example 1
```
Input: s = "anagram", t = "nagaram"
Output: True
```

### Constraints
- `1 <= len(s), len(t) <= 5 * 10^4`

---

## 3. Ransom Note
**Difficulty:** 🟢 Easy

### Problem
Дана строка `ransomNote` и строка `magazine`. Верните `True`, если `ransomNote` можно составить из букв `magazine`. Каждую букву можно использовать только один раз.

### Example 1
```
Input: ransomNote = "aa", magazine = "aab"
Output: True
```

### Example 2
```
Input: ransomNote = "aa", magazine = "ab"
Output: False
```

### Constraints
- `1 <= len(ransomNote), len(magazine) <= 10^5`

---

## 4. Intersection of Two Arrays II
**Difficulty:** 🟢 Easy

### Problem
Даны два массива `nums1` и `nums2`. Верните массив их **пересечения** (с учётом количества).

### Example 1
```
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2, 2]
```

### Constraints
- `1 <= len(nums1), len(nums2) <= 1000`

---

## 5. Subarray Sum Equals K
**Difficulty:** 🟡 Medium

### Problem
Дан массив `nums` и число `k`. Верните **количество** непрерывных подмассивов с суммой `k`.

### Example 1
```
Input: nums = [1, 1, 1], k = 2
Output: 2
```

### Example 2
```
Input: nums = [1, 2, 3], k = 3
Output: 2
```

### Constraints
- `1 <= len(nums) <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`

---

## 6. Top K Frequent Elements
**Difficulty:** 🟡 Medium

### Problem
Дан массив `nums` и число `k`. Верните `k` **наиболее частых** элементов.

### Example 1
```
Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
```

### Constraints
- `1 <= len(nums) <= 10^5`
- `1 <= k <= количество уникальных`

---

## 7. Isomorphic Strings
**Difficulty:** 🟢 Easy

### Problem
Даны строки `s` и `t`. Определите, **изоморфны** ли они (каждый символ `s` маппится на один символ `t` и наоборот).

### Example 1
```
Input: s = "egg", t = "add"
Output: True
```

### Example 2
```
Input: s = "foo", t = "bar"
Output: False
```

### Constraints
- `1 <= len(s) <= 5 * 10^4`
- `len(s) == len(t)`

---

## 8. Longest Consecutive Sequence
**Difficulty:** 🟡 Medium

### Problem
Дан несортированный массив `nums`. Найдите длину **самой длинной** последовательности идущих подряд чисел. Решение за **O(n)**.

### Example 1
```
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: Последовательность [1, 2, 3, 4] — длина 4.
```

### Constraints
- `0 <= len(nums) <= 10^5`

---

## 9. Word Pattern
**Difficulty:** 🟢 Easy

### Problem
Дан паттерн `pattern` и строка `s`. Проверьте, соответствует ли `s` паттерну (биекция).

### Example 1
```
Input: pattern = "abba", s = "dog cat cat dog"
Output: True
```

### Example 2
```
Input: pattern = "abba", s = "dog cat cat fish"
Output: False
```

### Constraints
- `1 <= len(pattern) <= 300`

---

## 10. 4Sum II
**Difficulty:** 🟡 Medium

### Problem
Даны 4 массива `nums1`, `nums2`, `nums3`, `nums4` длины `n`. Подсчитайте количество кортежей `(i, j, k, l)`, таких что `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`.

### Example 1
```
Input: nums1 = [1, 2], nums2 = [-2, -1], nums3 = [-1, 2], nums4 = [0, 2]
Output: 2
```

### Constraints
- `n == len(nums1) == len(nums2) == len(nums3) == len(nums4)`
- `1 <= n <= 200`
