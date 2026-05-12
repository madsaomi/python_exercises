# 🧩 Dynamic Programming — Задачи

---

## 1. Climbing Stairs
**Difficulty:** 🟢 Easy  
**Паттерн:** 1D DP / Fibonacci

### Problem
Вы поднимаетесь по лестнице из `n` ступенек. На каждом шаге можно подняться на **1 или 2** ступеньки. Сколько **различных способов** добраться до вершины?

### Example 1
```
Input: n = 2
Output: 2
Explanation: 1+1 или 2.
```

### Example 2
```
Input: n = 3
Output: 3
Explanation: 1+1+1, 1+2, 2+1.
```

### Example 3
```
Input: n = 5
Output: 8
```

### Constraints
- `1 <= n <= 45`

### Hints
<details>
<summary>Подсказка 1</summary>
dp[i] = dp[i-1] + dp[i-2]. С i-1 ступеньки — шаг 1, с i-2 — шаг 2. Это числа Фибоначчи!
</details>

<details>
<summary>Подсказка 2</summary>
Оптимизация памяти: нужны только два предыдущих значения. O(1) память.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Naive Recursion | O(2ⁿ) | O(n) |
| Memoization | O(n) | O(n) |
| **Tabulation** | **O(n)** | **O(n)** |
| Two variables | O(n) | O(1) |

### State Transition
```
dp[0] = 1 (стоим на земле — 1 способ)
dp[1] = 1
dp[i] = dp[i-1] + dp[i-2]
```

---

## 2. House Robber
**Difficulty:** 🟡 Medium  
**Паттерн:** 1D DP (Include/Exclude)

### Problem
Грабитель планирует ограбить дома вдоль улицы. Соседние дома связаны сигнализацией — нельзя грабить **два соседних** дома.

Дан массив `nums[i]` — сумма денег в i-м доме. Найдите **максимальную сумму**, которую можно украсть.

### Example 1
```
Input: nums = [1, 2, 3, 1]
Output: 4
Explanation: Ограбить дом 0 (1) + дом 2 (3) = 4.
```

### Example 2
```
Input: nums = [2, 7, 9, 3, 1]
Output: 12
Explanation: Дом 0 (2) + дом 2 (9) + дом 4 (1) = 12.
```

### Example 3
```
Input: nums = [2, 1, 1, 2]
Output: 4
Explanation: Дом 0 (2) + дом 3 (2) = 4.
```

### Constraints
- `1 <= len(nums) <= 100`
- `0 <= nums[i] <= 400`

### Hints
<details>
<summary>Подсказка 1</summary>
Для каждого дома два варианта: ограбить (взять nums[i] + лучшее до i-2) или не грабить (лучшее до i-1).
</details>

<details>
<summary>Подсказка 2</summary>
dp[i] = max(dp[i-1], dp[i-2] + nums[i]). Можно оптимизировать до O(1) памяти.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **DP (tabulation)** | **O(n)** | **O(n)** |
| Two variables | O(n) | O(1) |

### State Transition
```
dp[i] = max(
    dp[i-1],           # не грабить i-й
    dp[i-2] + nums[i]  # ограбить i-й
)
```

---

## 3. Coin Change
**Difficulty:** 🟡 Medium  
**Паттерн:** Unbounded Knapsack / 1D DP

### Problem
Даны монеты номиналов `coins` (бесконечный запас каждой) и сумма `amount`. Верните **минимальное количество монет** для набора суммы. Если невозможно — `-1`.

### Example 1
```
Input: coins = [1, 5, 10], amount = 11
Output: 2
Explanation: 10 + 1 = 11 → 2 монеты.
```

### Example 2
```
Input: coins = [2], amount = 3
Output: -1
Explanation: Невозможно набрать 3 из монет номиналом 2.
```

### Example 3
```
Input: coins = [1], amount = 0
Output: 0
Explanation: Нужно 0 монет для суммы 0.
```

### Constraints
- `1 <= len(coins) <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
dp[i] = минимум монет для суммы i. dp[0] = 0. Для каждой монеты c: dp[i] = min(dp[i], dp[i-c] + 1).
</details>

<details>
<summary>Подсказка 2</summary>
Инициализируйте dp массив значением float('inf'). Если dp[amount] == inf → -1.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force (recursion) | O(amount^n) | O(amount) |
| **DP (tabulation)** | **O(amount × len(coins))** | **O(amount)** |

### State Transition
```
dp[0] = 0
dp[i] = min(dp[i - coin] + 1) для каждой coin в coins, если i - coin >= 0
```

---

## 4. Longest Increasing Subsequence
**Difficulty:** 🟡 Medium  
**Паттерн:** 1D DP / Binary Search + Patience Sort

### Problem
Дан массив `nums`. Найдите длину **самой длинной строго возрастающей подпоследовательности** (LIS).

Подпоследовательность — не обязательно непрерывная.

### Example 1
```
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: LIS = [2, 3, 7, 101] или [2, 5, 7, 101]. Длина 4.
```

### Example 2
```
Input: nums = [0, 1, 0, 3, 2, 3]
Output: 4
Explanation: LIS = [0, 1, 2, 3].
```

### Example 3
```
Input: nums = [7, 7, 7, 7, 7]
Output: 1
Explanation: Строго возрастающая → только один элемент.
```

### Constraints
- `1 <= len(nums) <= 2500`
- `-10^4 <= nums[i] <= 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
DP O(n²): dp[i] = длина LIS, заканчивающейся на nums[i]. dp[i] = max(dp[j] + 1) для всех j < i, если nums[j] < nums[i].
</details>

<details>
<summary>Подсказка 2</summary>
Оптимальный O(n log n): поддерживайте массив tails. Для каждого числа: бинарный поиск позиции вставки (bisect_left).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **DP** | **O(n²)** | **O(n)** |
| Binary Search (Patience) | O(n log n) | O(n) |

### State Transition
```
dp[i] = 1  (минимум — сам элемент)
dp[i] = max(dp[j] + 1) для j < i, если nums[j] < nums[i]
Ответ = max(dp)
```

---

## 5. Unique Paths
**Difficulty:** 🟡 Medium  
**Паттерн:** 2D DP / Combinatorics

### Problem
Робот стоит в левом верхнем углу сетки `m × n`. Может двигаться **только вправо или вниз**. Сколько **уникальных путей** до правого нижнего угла?

### Example 1
```
Input: m = 3, n = 7
Output: 28
```

### Example 2
```
Input: m = 3, n = 2
Output: 3
Explanation: 
  Вправо→Вниз→Вниз
  Вниз→Вправо→Вниз
  Вниз→Вниз→Вправо
```

### Example 3
```
Input: m = 1, n = 1
Output: 1
```

### Constraints
- `1 <= m, n <= 100`

### Hints
<details>
<summary>Подсказка 1</summary>
dp[i][j] = dp[i-1][j] + dp[i][j-1]. Первая строка и первый столбец = 1 (один путь).
</details>

<details>
<summary>Подсказка 2</summary>
Оптимизация: достаточно одного массива dp[n], обновляемого построчно. Или математика: C(m+n-2, m-1).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **2D DP** | **O(m × n)** | **O(m × n)** |
| 1D DP | O(m × n) | O(n) |
| Combinatorics | O(m + n) | O(1) |

### State Transition
```
dp[0][j] = 1, dp[i][0] = 1
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

---

## 6. Maximum Subarray (DP approach)
**Difficulty:** 🟡 Medium  
**Паттерн:** Kadane's Algorithm / 1D DP

### Problem
Найдите непрерывный подмассив с **наибольшей суммой** и верните эту сумму.

Формализуйте как DP: dp[i] = максимальная сумма подмассива, **заканчивающегося** на nums[i].

### Example 1
```
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] → сумма 6.
```

### Example 2
```
Input: nums = [1]
Output: 1
```

### Example 3
```
Input: nums = [5, 4, -1, 7, 8]
Output: 23
Explanation: Весь массив.
```

### Constraints
- `1 <= len(nums) <= 10^5`

### Hints
<details>
<summary>Подсказка 1</summary>
dp[i] = max(nums[i], dp[i-1] + nums[i]). Либо начинаем новый подмассив, либо продолжаем старый.
</details>

<details>
<summary>Подсказка 2</summary>
Достаточно одной переменной current_sum вместо массива dp. Ответ = max(все current_sum).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n²) | O(1) |
| **Kadane's (DP)** | **O(n)** | **O(1)** |

### State Transition
```
dp[i] = max(nums[i], dp[i-1] + nums[i])
answer = max(dp[0], dp[1], ..., dp[n-1])
```

---

## 7. Word Break
**Difficulty:** 🟡 Medium  
**Паттерн:** 1D DP / BFS

### Problem
Дана строка `s` и словарь слов `wordDict`. Определите, можно ли **разбить** строку `s` на одно или несколько слов из словаря. Слова можно использовать повторно.

### Example 1
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: True
Explanation: "leet" + "code" = "leetcode"
```

### Example 2
```
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: True
Explanation: "apple" + "pen" + "apple"
```

### Example 3
```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: False
```

### Constraints
- `1 <= len(s) <= 300`
- `1 <= len(wordDict) <= 1000`
- `1 <= len(wordDict[i]) <= 20`

### Hints
<details>
<summary>Подсказка 1</summary>
dp[i] = True, если s[:i] можно разбить на слова из словаря. dp[0] = True (пустая строка).
</details>

<details>
<summary>Подсказка 2</summary>
Для каждого i: проверьте все j < i. Если dp[j] == True и s[j:i] в словаре → dp[i] = True.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **DP** | **O(n² × k)** | **O(n)** |
| BFS | O(n² × k) | O(n) |

### State Transition
```
dp[0] = True
dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(i))
```

---

## 8. Longest Common Subsequence
**Difficulty:** 🟡 Medium  
**Паттерн:** 2D DP (Classic)

### Problem
Даны две строки `text1` и `text2`. Найдите длину их **самой длинной общей подпоследовательности** (LCS). Если нет — верните `0`.

Подпоследовательность — последовательность символов, полученная удалением некоторых (или нуля) символов без изменения порядка.

### Example 1
```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: LCS = "ace", длина 3.
```

### Example 2
```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: LCS = "abc".
```

### Example 3
```
Input: text1 = "abc", text2 = "def"
Output: 0
```

### Constraints
- `1 <= len(text1), len(text2) <= 1000`

### Hints
<details>
<summary>Подсказка 1</summary>
Если text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1.  
Иначе: dp[i][j] = max(dp[i-1][j], dp[i][j-1]).
</details>

<details>
<summary>Подсказка 2</summary>
Можно оптимизировать до O(min(m,n)) памяти, используя два массива.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **2D DP** | **O(m × n)** | **O(m × n)** |
| 1D DP (optimized) | O(m × n) | O(min(m,n)) |

### State Transition
```
dp[0][j] = 0, dp[i][0] = 0
Если text1[i-1] == text2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
Иначе:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

---

## 9. 0/1 Knapsack
**Difficulty:** 🟡 Medium  
**Паттерн:** 2D DP (Classic Knapsack)

### Problem
Дан рюкзак вместимостью `W`. Есть `n` предметов с весами `weights[i]` и стоимостями `values[i]`. Каждый предмет можно взять **только один раз**. Найдите **максимальную стоимость**, которая помещается в рюкзак.

### Example 1
```
Input: W = 7, weights = [1, 3, 4, 5], values = [1, 4, 5, 7]
Output: 9
Explanation: Взять предметы 1 и 2 (веса 3+4=7, стоимость 4+5=9).
```

### Example 2
```
Input: W = 5, weights = [2, 3, 4], values = [3, 4, 5]
Output: 7
Explanation: Взять предметы 0 и 1 (веса 2+3=5, стоимость 3+4=7).
```

### Example 3
```
Input: W = 0, weights = [1], values = [1]
Output: 0
Explanation: Рюкзак пуст — ничего не помещается.
```

### Constraints
- `1 <= n <= 100`
- `1 <= W <= 1000`
- `1 <= weights[i], values[i] <= 1000`

### Hints
<details>
<summary>Подсказка 1</summary>
dp[i][w] = максимальная стоимость, используя первые i предметов и рюкзак ёмкости w.
</details>

<details>
<summary>Подсказка 2</summary>
Если weights[i-1] > w: dp[i][w] = dp[i-1][w] (не берём).  
Иначе: dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1]).
</details>

<details>
<summary>Подсказка 3</summary>
Оптимизация: 1D массив, проход по w справа налево (чтобы не использовать предмет дважды).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **2D DP** | **O(n × W)** | **O(n × W)** |
| 1D DP (optimized) | O(n × W) | O(W) |

### State Transition
```
dp[0][w] = 0 для всех w
Если weights[i-1] <= w:
    dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
Иначе:
    dp[i][w] = dp[i-1][w]
```

---

## 10. Edit Distance
**Difficulty:** 🔴 Hard  
**Паттерн:** 2D DP (Classic)

### Problem
Даны две строки `word1` и `word2`. Верните **минимальное количество операций** для преобразования `word1` в `word2`.

Допустимые операции:
- **Вставка** одного символа
- **Удаление** одного символа
- **Замена** одного символа

### Example 1
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
  horse → rorse (замена h → r)
  rorse → rose  (удаление r)
  rose  → ros   (удаление e)
```

### Example 2
```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
  intention → inention  (удаление t)
  inention  → enention  (замена i → e)
  enention  → exention  (замена n → x)
  exention  → exection  (замена n → c)
  exection  → execution (вставка u)
```

### Example 3
```
Input: word1 = "", word2 = "abc"
Output: 3
Explanation: Три вставки.
```

### Constraints
- `0 <= len(word1), len(word2) <= 500`
- Строки содержат только строчные латинские буквы

### Hints
<details>
<summary>Подсказка 1</summary>
dp[i][j] = минимум операций для преобразования word1[:i] в word2[:j].
</details>

<details>
<summary>Подсказка 2</summary>
Если word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1] (бесплатно).  
Иначе: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) — удаление, вставка, замена.
</details>

<details>
<summary>Подсказка 3</summary>
Базовые случаи: dp[i][0] = i (удалить все символы), dp[0][j] = j (вставить все символы).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **2D DP** | **O(m × n)** | **O(m × n)** |
| 1D DP | O(m × n) | O(min(m, n)) |

### State Transition
```
dp[0][j] = j, dp[i][0] = i
Если word1[i-1] == word2[j-1]:
    dp[i][j] = dp[i-1][j-1]
Иначе:
    dp[i][j] = 1 + min(
        dp[i-1][j],     # удаление
        dp[i][j-1],     # вставка
        dp[i-1][j-1]    # замена
    )
```
