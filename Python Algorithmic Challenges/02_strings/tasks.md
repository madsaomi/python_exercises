# 🧩 Strings — Задачи

---

## 1. Valid Palindrome
**Difficulty:** 🟢 Easy  
**Паттерн:** Two Pointers

### Problem
Дана строка `s`. Определите, является ли она палиндромом, учитывая только буквы и цифры (alphanumeric), игнорируя регистр.

Пустая строка считается палиндромом.

### Example 1
```
Input: s = "A man, a plan, a canal: Panama"
Output: True
Explanation: После очистки: "amanaplanacanalpanama" — палиндром
```

### Example 2
```
Input: s = "race a car"
Output: False
Explanation: После очистки: "raceacar" — не палиндром
```

### Example 3
```
Input: s = " "
Output: True
Explanation: Пустая строка после очистки — палиндром.
```

### Constraints
- `1 <= len(s) <= 2 * 10^5`
- `s` содержит ASCII-символы

### Hints
<details>
<summary>Подсказка 1</summary>
Можно очистить строку (оставить только буквы/цифры, привести к lower), потом сравнить с реверсом.
</details>

<details>
<summary>Подсказка 2</summary>
Для O(1) памяти: два указателя с краёв, пропуская неалфавитные символы.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Clean + Reverse | O(n) | O(n) |
| **Two Pointers** | **O(n)** | **O(1)** |

---

## 2. Reverse String
**Difficulty:** 🟢 Easy  
**Паттерн:** Two Pointers

### Problem
Дан массив символов `s`. Разверните строку **in-place** с O(1) дополнительной памяти.

Нельзя возвращать новую строку — нужно модифицировать входной массив.

### Example 1
```
Input: s = ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]
```

### Example 2
```
Input: s = ["H", "a", "n", "n", "a", "h"]
Output: ["h", "a", "n", "n", "a", "H"]
```

### Constraints
- `1 <= len(s) <= 10^5`
- Каждый `s[i]` — печатный ASCII-символ

### Hints
<details>
<summary>Подсказка 1</summary>
Два указателя: left=0, right=len-1. Меняйте s[left] и s[right] местами, двигайте навстречу.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Two Pointers (swap)** | **O(n)** | **O(1)** |

---

## 3. Valid Anagram
**Difficulty:** 🟢 Easy  
**Паттерн:** Hash Map / Sorting

### Problem
Даны две строки `s` и `t`. Верните `True`, если `t` — анаграмма `s`, иначе `False`.

Анаграмма — слово, полученное перестановкой букв другого слова, используя все буквы ровно один раз.

### Example 1
```
Input: s = "anagram", t = "nagaram"
Output: True
Explanation: Обе строки содержат: a×3, n×1, g×1, r×1, m×1
```

### Example 2
```
Input: s = "rat", t = "car"
Output: False
```

### Example 3
```
Input: s = "a", t = "ab"
Output: False
Explanation: Разная длина — точно не анаграмма.
```

### Constraints
- `1 <= len(s), len(t) <= 5 * 10^4`
- Строки содержат только строчные латинские буквы

### Hints
<details>
<summary>Подсказка 1</summary>
Если длины строк разные — ответ сразу False.
</details>

<details>
<summary>Подсказка 2</summary>
Подсчитайте частоту каждой буквы в обеих строках и сравните.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Sorting | O(n log n) | O(n) |
| **Counter / Hash Map** | **O(n)** | **O(1)** (26 букв) |

---

## 4. First Unique Character in a String
**Difficulty:** 🟢 Easy  
**Паттерн:** Hash Map

### Problem
Дана строка `s`. Найдите **первый** неповторяющийся символ и верните его индекс.  
Если такого символа нет — верните `-1`.

### Example 1
```
Input: s = "leetcode"
Output: 0
Explanation: 'l' встречается один раз и стоит первой.
```

### Example 2
```
Input: s = "loveleetcode"
Output: 2
Explanation: 'v' — первый символ, который встречается один раз (индекс 2).
```

### Example 3
```
Input: s = "aabb"
Output: -1
Explanation: Все символы повторяются.
```

### Constraints
- `1 <= len(s) <= 10^5`
- Только строчные латинские буквы

### Hints
<details>
<summary>Подсказка 1</summary>
Первый проход: подсчитайте частоты. Второй проход: найдите первый символ с частотой 1.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n²) | O(1) |
| **Two Pass + Hash Map** | **O(n)** | **O(1)** (26 букв) |

---

## 5. Longest Substring Without Repeating Characters
**Difficulty:** 🟡 Medium  
**Паттерн:** Sliding Window + Hash Set/Map

### Problem
Дана строка `s`. Найдите длину **самой длинной подстроки** без повторяющихся символов.

Подстрока — непрерывная последовательность символов.

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
Explanation: Ответ — "b", длина 1.
```

### Example 3
```
Input: s = "pwwkew"
Output: 3
Explanation: Ответ — "wke", длина 3.
Обратите внимание: "pwke" — подпоследовательность, а не подстрока!
```

### Example 4
```
Input: s = ""
Output: 0
```

### Constraints
- `0 <= len(s) <= 5 * 10^4`
- `s` содержит английские буквы, цифры, символы, пробелы

### Hints
<details>
<summary>Подсказка 1</summary>
Скользящее окно: расширяйте правую границу, пока символы уникальны.
</details>

<details>
<summary>Подсказка 2</summary>
Если встретили повтор — сужайте левую границу, пока символ не будет удалён из окна.
</details>

<details>
<summary>Подсказка 3</summary>
Используйте set для отслеживания символов в текущем окне, или dict с последней позицией символа для «прыжка» левой границы.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n³) | O(n) |
| **Sliding Window + Set** | **O(n)** | **O(min(n, m))** |
| Sliding Window + Dict | O(n) | O(min(n, m)) |

---

## 6. Longest Palindromic Substring
**Difficulty:** 🟡 Medium  
**Паттерн:** Expand Around Center

### Problem
Дана строка `s`. Верните **самую длинную палиндромную подстроку** в `s`.

### Example 1
```
Input: s = "babad"
Output: "bab" (или "aba" — оба допустимы)
```

### Example 2
```
Input: s = "cbbd"
Output: "bb"
```

### Example 3
```
Input: s = "a"
Output: "a"
```

### Example 4
```
Input: s = "ac"
Output: "a" (или "c")
```

### Constraints
- `1 <= len(s) <= 1000`
- `s` содержит только цифры и английские буквы

### Hints
<details>
<summary>Подсказка 1</summary>
Палиндромы «растут» из центра. Центром может быть один символ (нечётная длина) или пара (чётная).
</details>

<details>
<summary>Подсказка 2</summary>
Для каждого индекса i: расширяйте от (i, i) для нечётных и (i, i+1) для чётных палиндромов. Обновляйте лучший результат.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n³) | O(1) |
| DP | O(n²) | O(n²) |
| **Expand Around Center** | **O(n²)** | **O(1)** |
| Manacher's Algorithm | O(n) | O(n) |

---

## 7. String to Integer (atoi)
**Difficulty:** 🟡 Medium  
**Паттерн:** String Parsing / State Machine

### Problem
Реализуйте функцию `myAtoi(s)`, которая преобразует строку в 32-битное целое число.

Алгоритм:
1. Пропустить ведущие пробелы
2. Определить знак (`+` или `-`). По умолчанию — положительный
3. Прочитать цифры, пока они идут подряд
4. Обрезать результат до диапазона `[-2^31, 2^31 - 1]`

Если цифр нет — вернуть 0.

### Example 1
```
Input: s = "42"
Output: 42
```

### Example 2
```
Input: s = "   -42"
Output: -42
Explanation: Пропускаем пробелы, читаем знак '-', читаем "42".
```

### Example 3
```
Input: s = "4193 with words"
Output: 4193
Explanation: Читаем "4193", останавливаемся на пробеле.
```

### Example 4
```
Input: s = "words and 987"
Output: 0
Explanation: Первый непробельный символ — не цифра и не знак.
```

### Example 5
```
Input: s = "-91283472332"
Output: -2147483648
Explanation: Число меньше -2^31, обрезаем до -2^31 = -2147483648.
```

### Constraints
- `0 <= len(s) <= 200`
- `s` содержит латинские буквы, цифры, пробелы, `+`, `-`, `.`

### Hints
<details>
<summary>Подсказка 1</summary>
Обрабатывайте строку посимвольно, следуя алгоритму из условия. Главное — не забыть про overflow.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Sequential Parsing** | **O(n)** | **O(1)** |

---

## 8. Count and Say
**Difficulty:** 🟡 Medium  
**Паттерн:** String Building / Simulation

### Problem
Последовательность "Count and Say" строится так:
- `countAndSay(1)` = `"1"`
- `countAndSay(n)` — описывает предыдущий элемент «словами»

Описание: перечислить последовательные группы одинаковых цифр.

```
1  → "1"              (начало)
2  → "11"             (одна 1)
3  → "21"             (две 1)
4  → "1211"           (одна 2, одна 1)
5  → "111221"         (одна 1, одна 2, две 1)
6  → "312211"         (три 1, две 2, одна 1)
```

Верните `n`-й элемент последовательности.

### Example 1
```
Input: n = 1
Output: "1"
```

### Example 2
```
Input: n = 4
Output: "1211"
```

### Example 3
```
Input: n = 5
Output: "111221"
```

### Constraints
- `1 <= n <= 30`

### Hints
<details>
<summary>Подсказка 1</summary>
Стройте каждый элемент последовательности из предыдущего. Итерируйте n-1 раз.
</details>

<details>
<summary>Подсказка 2</summary>
Для каждого элемента: пройдитесь по строке, считая подряд идущие одинаковые символы. Формируйте новую строку: f"{count}{digit}".
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Iterative Simulation** | **O(n × L)** | **O(L)** |

---

## 9. Longest Common Prefix
**Difficulty:** 🟢 Easy  
**Паттерн:** Vertical / Horizontal Scanning

### Problem
Дан массив строк `strs`. Найдите **самый длинный общий префикс** среди всех строк.

Если общего префикса нет — верните `""`.

### Example 1
```
Input: strs = ["flower", "flow", "flight"]
Output: "fl"
```

### Example 2
```
Input: strs = ["dog", "racecar", "car"]
Output: ""
Explanation: Нет общего префикса.
```

### Example 3
```
Input: strs = ["interspecies", "interstellar", "interstate"]
Output: "inters"
```

### Example 4
```
Input: strs = ["a"]
Output: "a"
```

### Constraints
- `1 <= len(strs) <= 200`
- `0 <= len(strs[i]) <= 200`
- Только строчные латинские буквы

### Hints
<details>
<summary>Подсказка 1</summary>
Вертикальное сканирование: сравнивайте символы на позиции i во всех строках. Остановитесь, когда символы различаются.
</details>

<details>
<summary>Подсказка 2</summary>
Альтернатива: отсортируйте массив. Общий префикс всего массива = общий префикс первой и последней строки.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Vertical Scanning** | **O(S)** | **O(1)** |
| Horizontal Scanning | O(S) | O(1) |
| Sort + Compare | O(n log n × m) | O(1) |

*S = сумма длин всех строк*

---

## 10. Group Anagrams
**Difficulty:** 🟡 Medium  
**Паттерн:** Hash Map + Sorting/Counting

### Problem
Дан массив строк `strs`. Сгруппируйте **анаграммы** вместе.

Ответ можно вернуть в любом порядке. Порядок внутри групп тоже не важен.

### Example 1
```
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
Explanation: 
  "eat", "tea", "ate" — анаграммы друг друга
  "tan", "nat" — анаграммы друг друга
  "bat" — не имеет анаграмм
```

### Example 2
```
Input: strs = [""]
Output: [[""]]
```

### Example 3
```
Input: strs = ["a"]
Output: [["a"]]
```

### Constraints
- `1 <= len(strs) <= 10^4`
- `0 <= len(strs[i]) <= 100`
- Только строчные латинские буквы

### Hints
<details>
<summary>Подсказка 1</summary>
Два слова — анаграммы, если при сортировке они дают одинаковую строку. Используйте sorted(word) как ключ словаря.
</details>

<details>
<summary>Подсказка 2</summary>
Альтернативный ключ: кортеж из 26 чисел — количество каждой буквы. Это O(n×k) вместо O(n×k×log k).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Sorted Key + Dict** | **O(n × k log k)** | **O(n × k)** |
| Count Key + Dict | O(n × k) | O(n × k) |

*n = количество строк, k = максимальная длина строки*
