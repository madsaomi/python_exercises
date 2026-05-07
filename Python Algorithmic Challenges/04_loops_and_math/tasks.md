# 🧩 Loops & Math — Задачи

---

## 1. Fizz Buzz
**Difficulty:** 🟢 Easy

### Problem
Дано число `n`. Верните массив строк `answer` длины `n`:
- `answer[i] == "FizzBuzz"` если `i+1` делится на 3 и 5
- `answer[i] == "Fizz"` если делится на 3
- `answer[i] == "Buzz"` если делится на 5
- `answer[i] == str(i+1)` иначе

### Example 1
```
Input: n = 5
Output: ["1", "2", "Fizz", "4", "Buzz"]
```

### Constraints
- `1 <= n <= 10^4`

---

## 2. Palindrome Number
**Difficulty:** 🟢 Easy

### Problem
Определите, является ли целое число `x` палиндромом. Решите **без преобразования в строку**.

### Example 1
```
Input: x = 121
Output: True
```

### Example 2
```
Input: x = -121
Output: False
```

### Constraints
- `-2^31 <= x <= 2^31 - 1`

---

## 3. Roman to Integer
**Difficulty:** 🟢 Easy

### Problem
Дана строка с римским числом. Преобразуйте в целое число.

### Example 1
```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M=1000, CM=900, XC=90, IV=4
```

### Constraints
- `1 <= len(s) <= 15`

---

## 4. Power of Three
**Difficulty:** 🟢 Easy

### Problem
Определите, является ли число `n` степенью тройки.

### Example 1
```
Input: n = 27
Output: True
```

### Example 2
```
Input: n = 0
Output: False
```

### Constraints
- `-2^31 <= n <= 2^31 - 1`

---

## 5. Count Primes
**Difficulty:** 🟡 Medium

### Problem
Подсчитайте количество **простых** чисел, строго меньших `n`. Используйте **Решето Эратосфена**.

### Example 1
```
Input: n = 10
Output: 4
Explanation: Простые < 10: 2, 3, 5, 7
```

### Constraints
- `0 <= n <= 5 * 10^6`

---

## 6. Happy Number
**Difficulty:** 🟢 Easy

### Problem
Число «счастливое», если при повторном заменении числа суммой квадратов его цифр, в итоге получается `1`.

### Example 1
```
Input: n = 19
Output: True
Explanation: 1²+9²=82, 8²+2²=68, 6²+8²=100, 1²+0²+0²=1
```

### Constraints
- `1 <= n <= 2^31 - 1`

---

## 7. Excel Sheet Column Number
**Difficulty:** 🟢 Easy

### Problem
Дано название столбца Excel. Верните его номер.
`A → 1, B → 2, ..., Z → 26, AA → 27, AB → 28, ...`

### Example 1
```
Input: columnTitle = "AB"
Output: 28
```

### Constraints
- `1 <= len(columnTitle) <= 7`

---

## 8. Pow(x, n)
**Difficulty:** 🟡 Medium

### Problem
Реализуйте `myPow(x, n)` — вычисление `x^n`. Используйте **быстрое возведение в степень** за O(log n).

### Example 1
```
Input: x = 2.0, n = 10
Output: 1024.0
```

### Example 2
```
Input: x = 2.0, n = -2
Output: 0.25
```

### Constraints
- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`

---

## 9. Sqrt(x)
**Difficulty:** 🟢 Easy

### Problem
Вычислите целочисленный квадратный корень из `x` **без** `math.sqrt`.

### Example 1
```
Input: x = 8
Output: 2
Explanation: √8 = 2.828..., отбрасываем дробную часть → 2
```

### Constraints
- `0 <= x <= 2^31 - 1`

---

## 10. Ugly Number
**Difficulty:** 🟢 Easy

### Problem
Число «уродливое», если его простые множители — только `2, 3, 5`. Определите, является ли `n` уродливым числом.

### Example 1
```
Input: n = 6
Output: True
Explanation: 6 = 2 × 3
```

### Example 2
```
Input: n = 14
Output: False
Explanation: 14 = 2 × 7 — 7 не допускается
```

### Constraints
- `-2^31 <= n <= 2^31 - 1`
