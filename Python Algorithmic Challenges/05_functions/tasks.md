# 🧩 Functions — Задачи

---

## 1. Plus One
**Difficulty:** 🟢 Easy

### Problem
Дан массив `digits` — представление неотрицательного числа. Прибавьте к числу `1` и верните результат как массив.

### Example 1
```
Input: digits = [1, 2, 3]
Output: [1, 2, 4]
```

### Example 2
```
Input: digits = [9, 9, 9]
Output: [1, 0, 0, 0]
```

### Constraints
- `1 <= len(digits) <= 100`
- `0 <= digits[i] <= 9`

---

## 2. Add Two Numbers (as Arrays)
**Difficulty:** 🟡 Medium

### Problem
Даны два числа, представленные массивами цифр в обратном порядке. Верните их сумму в таком же формате.

### Example 1
```
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]
Explanation: 342 + 465 = 807
```

### Constraints
- `1 <= len(l1), len(l2) <= 100`

---

## 3. Single Number
**Difficulty:** 🟢 Easy

### Problem
Дан массив, где каждый элемент встречается **дважды**, кроме одного. Найдите этот элемент за **O(n)** времени и **O(1)** памяти.

### Example 1
```
Input: nums = [4, 1, 2, 1, 2]
Output: 4
```

### Constraints
- `1 <= len(nums) <= 3 * 10^4`

---

## 4. Missing Number
**Difficulty:** 🟢 Easy

### Problem
Дан массив из `n` различных чисел в диапазоне `[0, n]`. Найдите **отсутствующее** число.

### Example 1
```
Input: nums = [3, 0, 1]
Output: 2
```

### Constraints
- `n == len(nums)`
- `0 <= nums[i] <= n`

---

## 5. Majority Element
**Difficulty:** 🟢 Easy

### Problem
Дан массив `nums` длины `n`. Найдите **элемент большинства** — встречается более `n/2` раз.

### Example 1
```
Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
```

### Constraints
- `n == len(nums)`
- Элемент большинства всегда существует

---

## 6. Number of 1 Bits
**Difficulty:** 🟢 Easy

### Problem
Дано положительное целое число `n`. Верните количество **единичных битов** в его двоичном представлении.

### Example 1
```
Input: n = 11
Output: 3
Explanation: 11 в двоичной = 1011, три единицы
```

### Constraints
- `1 <= n <= 2^31 - 1`

---

## 7. Reverse Integer
**Difficulty:** 🟡 Medium

### Problem
Дано 32-битное целое число `x`. Разверните его цифры. Если результат выходит за пределы `[-2^31, 2^31 - 1]` — верните `0`.

### Example 1
```
Input: x = 123
Output: 321
```

### Example 2
```
Input: x = -123
Output: -321
```

### Constraints
- `-2^31 <= x <= 2^31 - 1`

---

## 8. Implement strStr()
**Difficulty:** 🟢 Easy

### Problem
Даны строки `haystack` и `needle`. Верните индекс первого вхождения `needle` в `haystack` или `-1`.

### Example 1
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
```

### Constraints
- `1 <= len(haystack), len(needle) <= 10^4`

---

## 9. Integer to Roman
**Difficulty:** 🟡 Medium

### Problem
Преобразуйте целое число в римское число.

### Example 1
```
Input: num = 1994
Output: "MCMXCIV"
```

### Constraints
- `1 <= num <= 3999`

---

## 10. Encode and Decode Strings
**Difficulty:** 🟡 Medium

### Problem
Реализуйте два метода:
- `encode(strs)` — кодирует список строк в одну строку
- `decode(s)` — декодирует обратно в список строк

### Example 1
```
Input: strs = ["hello", "world"]
Output (encode): "5#hello5#world"
Output (decode): ["hello", "world"]
```

### Constraints
- `0 <= len(strs) <= 200`
- Строки могут содержать любые символы
