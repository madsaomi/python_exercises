# 🧩 Dynamic Programming — Задачи

---

## 1. Climbing Stairs
**Difficulty:** 🟢 Easy

### Problem
Вы поднимаетесь по лестнице из `n` ступенек. На каждом шаге можно подняться на 1 или 2 ступеньки. Сколько **различных способов** подняться наверх?

### Example 1
```
Input: n = 3
Output: 3
Explanation: 1+1+1, 1+2, 2+1
```

### Constraints
- `1 <= n <= 45`

---

## 2. House Robber
**Difficulty:** 🟡 Medium

### Problem
Грабитель не может грабить **два соседних** дома. Дан массив `nums` — сумма в каждом доме. Найдите **максимальную** сумму.

### Example 1
```
Input: nums = [2, 7, 9, 3, 1]
Output: 12
Explanation: 2 + 9 + 1 = 12
```

### Constraints
- `1 <= len(nums) <= 100`

---

## 3. Coin Change
**Difficulty:** 🟡 Medium

### Problem
Даны монеты `coins` и сумма `amount`. Верните **минимальное количество** монет для суммы. Если невозможно — `-1`.

### Example 1
```
Input: coins = [1, 5, 10], amount = 11
Output: 3
Explanation: 10 + 1 = 11 (нет, это 2 монеты → 5 + 5 + 1)
→ Правильно: 10 + 1 = 2 монеты? Нет: 11 = 5+5+1 = 3 монеты
→ На самом деле 11 = 10+1 = 2 монеты ✓
```

### Example 2
```
Input: coins = [1, 5, 10], amount = 11
Output: 2
Explanation: 10 + 1 = 11
```

### Constraints
- `1 <= len(coins) <= 12`
- `0 <= amount <= 10^4`

---

## 4. Longest Increasing Subsequence
**Difficulty:** 🟡 Medium

### Problem
Найдите длину **самой длинной строго возрастающей подпоследовательности**.

### Example 1
```
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: [2, 3, 7, 101] — длина 4
```

### Constraints
- `1 <= len(nums) <= 2500`

---

## 5. Unique Paths
**Difficulty:** 🟡 Medium

### Problem
Робот в левом верхнем углу сетки `m x n`. Может двигаться **только вправо или вниз**. Сколько **уникальных путей** до правого нижнего угла?

### Example 1
```
Input: m = 3, n = 7
Output: 28
```

### Constraints
- `1 <= m, n <= 100`

---

## 6. Maximum Subarray (DP approach)
**Difficulty:** 🟡 Medium

### Problem
Найдите подмассив с **наибольшей суммой**. Решите через DP (Kadane's Algorithm).

### Example 1
```
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1]
```

### Constraints
- `1 <= len(nums) <= 10^5`

---

## 7. Word Break
**Difficulty:** 🟡 Medium

### Problem
Дана строка `s` и словарь `wordDict`. Можно ли **разбить** строку на слова из словаря?

### Example 1
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: True
```

### Example 2
```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: False
```

### Constraints
- `1 <= len(s) <= 300`

---

## 8. Longest Common Subsequence
**Difficulty:** 🟡 Medium

### Problem
Даны строки `text1` и `text2`. Найдите длину их **самой длинной общей подпоследовательности**.

### Example 1
```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: LCS = "ace"
```

### Constraints
- `1 <= len(text1), len(text2) <= 1000`

---

## 9. 0/1 Knapsack
**Difficulty:** 🟡 Medium

### Problem
Дан рюкзак вместимостью `W`. Есть `n` предметов с весами `weights` и стоимостями `values`. Каждый предмет можно взять **только один раз**. Найдите **максимальную стоимость**.

### Example 1
```
Input: W = 7, weights = [1, 3, 4, 5], values = [1, 4, 5, 7]
Output: 9
Explanation: Взять предметы с весами 3 и 4 (стоимость 4 + 5 = 9)
```

### Constraints
- `1 <= n <= 100`
- `1 <= W <= 1000`

---

## 10. Edit Distance
**Difficulty:** 🔴 Hard

### Problem
Даны строки `word1` и `word2`. Верните **минимальное количество операций** для преобразования `word1` в `word2`. Допустимые операции: вставка, удаление, замена символа.

### Example 1
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse → rorse (замена h → r)
rorse → rose (удаление r)
rose → ros (удаление e)
```

### Constraints
- `0 <= len(word1), len(word2) <= 500`
