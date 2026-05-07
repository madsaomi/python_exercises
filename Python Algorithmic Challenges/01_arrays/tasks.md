# 🧩 Arrays — Задачи

---

## 1. Two Sum
**Difficulty:** 🟢 Easy

### Problem
Дан массив целых чисел `nums` и целое число `target`.  
Верните индексы двух чисел, сумма которых равна `target`.

Каждый вход имеет **ровно одно решение**. Нельзя использовать один элемент дважды.

### Example 1
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

### Example 2
```
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

### Constraints
- `2 <= len(nums) <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- Ровно одно решение существует

---

## 2. Remove Duplicates from Sorted Array
**Difficulty:** 🟢 Easy

### Problem
Дан отсортированный массив `nums`.  
Удалите дубликаты **in-place** так, чтобы каждый уникальный элемент появился **один раз**.  
Верните количество уникальных элементов `k`.

### Example 1
```
Input: nums = [1, 1, 2]
Output: 2, nums = [1, 2, ...]
```

### Example 2
```
Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, nums = [0, 1, 2, 3, 4, ...]
```

### Constraints
- `1 <= len(nums) <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` отсортирован по возрастанию

---

## 3. Best Time to Buy and Sell Stock
**Difficulty:** 🟢 Easy

### Problem
Дан массив `prices`, где `prices[i]` — цена акции в `i`-й день.  
Вы можете купить акцию **один раз** и продать **один раз**.  
Верните **максимальную прибыль**. Если прибыль невозможна — верните `0`.

### Example 1
```
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Купить в день 2 (цена 1), продать в день 5 (цена 6). Прибыль = 6 - 1 = 5.
```

### Example 2
```
Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: Прибыль невозможна.
```

### Constraints
- `1 <= len(prices) <= 10^5`
- `0 <= prices[i] <= 10^4`

---

## 4. Contains Duplicate
**Difficulty:** 🟢 Easy

### Problem
Дан массив целых чисел `nums`.  
Верните `True`, если в массиве есть хотя бы один дубликат.  
Верните `False`, если все элементы уникальны.

### Example 1
```
Input: nums = [1, 2, 3, 1]
Output: True
```

### Example 2
```
Input: nums = [1, 2, 3, 4]
Output: False
```

### Constraints
- `1 <= len(nums) <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## 5. Maximum Subarray
**Difficulty:** 🟡 Medium

### Problem
Дан массив целых чисел `nums`.  
Найдите подмассив (непрерывную подпоследовательность) с **наибольшей суммой** и верните эту сумму.

### Example 1
```
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: Подмассив [4, -1, 2, 1] имеет наибольшую сумму 6.
```

### Example 2
```
Input: nums = [5, 4, -1, 7, 8]
Output: 23
```

### Constraints
- `1 <= len(nums) <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## 6. Merge Sorted Arrays
**Difficulty:** 🟢 Easy

### Problem
Даны два отсортированных массива `nums1` и `nums2`.  
Объедините `nums2` в `nums1` как один отсортированный массив **in-place**.

`nums1` имеет длину `m + n`, где первые `m` элементов — значения, остальные `n` — нули (заполнители).

### Example 1
```
Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
Output: [1, 2, 2, 3, 5, 6]
```

### Constraints
- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`

---

## 7. Product of Array Except Self
**Difficulty:** 🟡 Medium

### Problem
Дан массив `nums`.  
Верните массив `answer`, где `answer[i]` равен произведению **всех элементов** `nums`, кроме `nums[i]`.

**Нельзя** использовать операцию деления. Решение за O(n).

### Example 1
```
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

### Example 2
```
Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```

### Constraints
- `2 <= len(nums) <= 10^5`
- `-30 <= nums[i] <= 30`

---

## 8. Move Zeroes
**Difficulty:** 🟢 Easy

### Problem
Дан массив `nums`.  
Переместите все `0` в конец, сохранив относительный порядок ненулевых элементов.  
Модифицируйте массив **in-place** без копирования.

### Example 1
```
Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
```

### Example 2
```
Input: nums = [0]
Output: [0]
```

### Constraints
- `1 <= len(nums) <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

---

## 9. Container With Most Water
**Difficulty:** 🟡 Medium

### Problem
Дан массив `height` длины `n`.  
Найдите две линии, которые вместе с осью X образуют контейнер с **наибольшим количеством воды**.

Верните максимальное количество воды.

### Example 1
```
Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
Explanation: Линии с индексами 1 и 8 (высоты 8 и 7), ширина = 7. Вода = 7 * 7 = 49.
```

### Constraints
- `2 <= len(height) <= 10^5`
- `0 <= height[i] <= 10^4`

---

## 10. Rotate Array
**Difficulty:** 🟡 Medium

### Problem
Дан массив `nums`. Сдвиньте массив вправо на `k` шагов **in-place**.

### Example 1
```
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
```

### Example 2
```
Input: nums = [-1, -100, 3, 99], k = 2
Output: [3, 99, -1, -100]
```

### Constraints
- `1 <= len(nums) <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`
