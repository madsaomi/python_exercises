# 🧩 Strings — Задачи

---

## 1. Valid Palindrome
**Difficulty:** 🟢 Easy

### Problem
Дана строка `s`. Определите, является ли она палиндромом, учитывая только буквы и цифры, игнорируя регистр.

### Example 1
```
Input: s = "A man, a plan, a canal: Panama"
Output: True
Explanation: "amanaplanacanalpanama" — палиндром
```

### Example 2
```
Input: s = "race a car"
Output: False
```

### Constraints
- `1 <= len(s) <= 2 * 10^5`
- `s` содержит ASCII-символы

---

## 2. Reverse String
**Difficulty:** 🟢 Easy

### Problem
Дан массив символов `s`. Разверните строку **in-place** с O(1) дополнительной памяти.

### Example 1
```
Input: s = ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]
```

### Constraints
- `1 <= len(s) <= 10^5`

---

## 3. Valid Anagram
**Difficulty:** 🟢 Easy

### Problem
Даны две строки `s` и `t`. Верните `True`, если `t` — анаграмма `s`.

### Example 1
```
Input: s = "anagram", t = "nagaram"
Output: True
```

### Example 2
```
Input: s = "rat", t = "car"
Output: False
```

### Constraints
- `1 <= len(s), len(t) <= 5 * 10^4`
- Строки содержат только строчные латинские буквы

---

## 4. First Unique Character in a String
**Difficulty:** 🟢 Easy

### Problem
Дана строка `s`. Найдите **первый** неповторяющийся символ и верните его индекс. Если нет — верните `-1`.

### Example 1
```
Input: s = "leetcode"
Output: 0
```

### Example 2
```
Input: s = "aabb"
Output: -1
```

### Constraints
- `1 <= len(s) <= 10^5`
- Только строчные латинские буквы

---

## 5. Longest Substring Without Repeating Characters
**Difficulty:** 🟡 Medium

### Problem
Дана строка `s`. Найдите длину **самой длинной подстроки** без повторяющихся символов.

### Example 1
```
Input: s = "abcabcbb"
Output: 3
Explanation: Ответ — "abc", длина 3.
```

### Example 2
```
Input: s = "bbbbb"
Output: 1
```

### Example 3
```
Input: s = "pwwkew"
Output: 3
Explanation: Ответ — "wke", длина 3.
```

### Constraints
- `0 <= len(s) <= 5 * 10^4`

---

## 6. Longest Palindromic Substring
**Difficulty:** 🟡 Medium

### Problem
Дана строка `s`. Верните **самую длинную палиндромную подстроку**.

### Example 1
```
Input: s = "babad"
Output: "bab" (или "aba")
```

### Example 2
```
Input: s = "cbbd"
Output: "bb"
```

### Constraints
- `1 <= len(s) <= 1000`

---

## 7. String to Integer (atoi)
**Difficulty:** 🟡 Medium

### Problem
Реализуйте функцию `myAtoi(s)`, которая преобразует строку в 32-битное целое число.

Алгоритм:
1. Пропустить ведущие пробелы
2. Определить знак (`+` или `-`)
3. Прочитать цифры, пока они есть
4. Обрезать до диапазона `[-2^31, 2^31 - 1]`

### Example 1
```
Input: s = "   -42"
Output: -42
```

### Example 2
```
Input: s = "4193 with words"
Output: 4193
```

### Constraints
- `0 <= len(s) <= 200`

---

## 8. Count and Say
**Difficulty:** 🟡 Medium

### Problem
Последовательность "Count and Say":
- `1` → `"1"`
- `2` → `"11"` (одна 1)
- `3` → `"21"` (две 1)
- `4` → `"1211"` (одна 2, одна 1)

Верните `n`-й элемент последовательности.

### Example 1
```
Input: n = 4
Output: "1211"
```

### Constraints
- `1 <= n <= 30`

---

## 9. Longest Common Prefix
**Difficulty:** 🟢 Easy

### Problem
Дан массив строк `strs`. Найдите **самый длинный общий префикс**. Если нет — верните `""`.

### Example 1
```
Input: strs = ["flower", "flow", "flight"]
Output: "fl"
```

### Example 2
```
Input: strs = ["dog", "racecar", "car"]
Output: ""
```

### Constraints
- `1 <= len(strs) <= 200`
- `0 <= len(strs[i]) <= 200`

---

## 10. Group Anagrams
**Difficulty:** 🟡 Medium

### Problem
Дан массив строк `strs`. Сгруппируйте **анаграммы** вместе. Порядок не важен.

### Example 1
```
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```

### Constraints
- `1 <= len(strs) <= 10^4`
- `0 <= len(strs[i]) <= 100`
- Только строчные латинские буквы
