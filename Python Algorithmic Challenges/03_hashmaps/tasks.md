# 🧩 Hashmaps — Задачи

---

## 1. Two Sum (HashMap Approach)
**Difficulty:** 🟢 Easy  
**Паттерн:** Hash Map Lookup

### Problem
Дан массив `nums` и число `target`. Верните индексы двух чисел, дающих в сумме `target`.  
Решите за **O(n)** с помощью хеш-таблицы.

Каждый вход имеет ровно одно решение. Один элемент нельзя использовать дважды.

### Example 1
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: 2 + 7 = 9. Используем dict: {2: 0}, ищем 9-7=2 → найден!
```

### Example 2
```
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

### Example 3
```
Input: nums = [3, 3], target = 6
Output: [0, 1]
```

### Constraints
- `2 <= len(nums) <= 10^4`
- Ровно одно решение

### Hints
<details>
<summary>Подсказка 1</summary>
Для каждого числа complement = target - num. Проверьте, есть ли complement в словаре.
</details>

<details>
<summary>Подсказка 2</summary>
За один проход: добавляйте числа в dict и сразу проверяйте complement.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Hash Map (1 pass)** | **O(n)** | **O(n)** |

---

## 2. Valid Anagram
**Difficulty:** 🟢 Easy  
**Паттерн:** Frequency Counter

### Problem
Даны строки `s` и `t`. Верните `True`, если `t` — анаграмма `s`. Используйте хеш-таблицу для подсчёта.

### Example 1
```
Input: s = "anagram", t = "nagaram"
Output: True
Explanation: Частоты: {a:3, n:1, g:1, r:1, m:1} — одинаковы.
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
Explanation: Разная длина → сразу False.
```

### Constraints
- `1 <= len(s), len(t) <= 5 * 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Используйте collections.Counter или dict для подсчёта букв. Counter(s) == Counter(t).
</details>

<details>
<summary>Подсказка 2</summary>
Альтернатива: один словарь — увеличивайте для s, уменьшайте для t. В конце все значения должны быть 0.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Sorting | O(n log n) | O(n) |
| **Counter / Dict** | **O(n)** | **O(1)** (26 букв) |

---

## 3. Ransom Note
**Difficulty:** 🟢 Easy  
**Паттерн:** Frequency Counter

### Problem
Дана строка `ransomNote` и строка `magazine`. Верните `True`, если `ransomNote` можно составить из букв `magazine`. Каждую букву из magazine можно использовать **только один раз**.

### Example 1
```
Input: ransomNote = "a", magazine = "b"
Output: False
```

### Example 2
```
Input: ransomNote = "aa", magazine = "ab"
Output: False
Explanation: В magazine только одна 'a', а нужно две.
```

### Example 3
```
Input: ransomNote = "aa", magazine = "aab"
Output: True
```

### Constraints
- `1 <= len(ransomNote), len(magazine) <= 10^5`
- Только строчные латинские буквы

### Hints
<details>
<summary>Подсказка 1</summary>
Подсчитайте буквы в magazine. Для каждой буквы ransomNote уменьшайте счётчик. Если стало < 0 → False.
</details>

<details>
<summary>Подсказка 2</summary>
Или: Counter(magazine) должен «покрывать» Counter(ransomNote). Проверьте: Counter(ransomNote) - Counter(magazine) == пусто.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Counter / Dict** | **O(m + n)** | **O(1)** (26 букв) |

---

## 4. Intersection of Two Arrays II
**Difficulty:** 🟢 Easy  
**Паттерн:** Hash Map / Two Pointers

### Problem
Даны два массива `nums1` и `nums2`. Верните массив их **пересечения** — каждый элемент должен появиться столько раз, сколько он встречается в обоих массивах. Порядок не важен.

### Example 1
```
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2, 2]
```

### Example 2
```
Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [4, 9] (или [9, 4])
```

### Constraints
- `1 <= len(nums1), len(nums2) <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

### Hints
<details>
<summary>Подсказка 1</summary>
Подсчитайте частоты в nums1 (Counter). Пройдитесь по nums2 — если элемент в Counter и count > 0, добавьте в результат.
</details>

<details>
<summary>Подсказка 2</summary>
Альтернатива: отсортируйте оба массива и используйте два указателя.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Hash Map** | **O(m + n)** | **O(min(m, n))** |
| Sort + Two Pointers | O(m log m + n log n) | O(1) |

### Follow-up
- Что если nums1 отсортирован? → Бинарный поиск
- Что если nums2 огромный и не помещается в память? → Отсортировать оба, читать чанками

---

## 5. Subarray Sum Equals K
**Difficulty:** 🟡 Medium  
**Паттерн:** Prefix Sum + Hash Map

### Problem
Дан массив целых чисел `nums` и число `k`. Верните **количество** непрерывных подмассивов, сумма которых равна `k`.

### Example 1
```
Input: nums = [1, 1, 1], k = 2
Output: 2
Explanation: Подмассивы [1,1] (индексы 0-1) и [1,1] (индексы 1-2).
```

### Example 2
```
Input: nums = [1, 2, 3], k = 3
Output: 2
Explanation: [1,2] и [3].
```

### Example 3
```
Input: nums = [1, -1, 0], k = 0
Output: 3
Explanation: [1,-1], [-1,0], [1,-1,0] — все дают сумму 0.
```

### Constraints
- `1 <= len(nums) <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

### Hints
<details>
<summary>Подсказка 1</summary>
Prefix sum: если prefix[j] - prefix[i] == k, то подмассив от i до j-1 имеет сумму k.
</details>

<details>
<summary>Подсказка 2</summary>
Храните в dict количество каждого значения prefix sum. Для текущего prefix ищите prefix - k в словаре.
</details>

<details>
<summary>Подсказка 3</summary>
Не забудьте инициализировать: {0: 1} — пустой префикс с суммой 0.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n²) | O(1) |
| **Prefix Sum + Hash Map** | **O(n)** | **O(n)** |

---

## 6. Top K Frequent Elements
**Difficulty:** 🟡 Medium  
**Паттерн:** Hash Map + Bucket Sort / Heap

### Problem
Дан массив целых чисел `nums` и число `k`. Верните `k` **наиболее часто встречающихся** элементов. Ответ можно вернуть в любом порядке. Гарантируется единственность ответа.

### Example 1
```
Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
Explanation: 1 встречается 3 раза, 2 — 2 раза, 3 — 1 раз.
```

### Example 2
```
Input: nums = [1], k = 1
Output: [1]
```

### Constraints
- `1 <= len(nums) <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= количество уникальных элементов`
- Ответ гарантированно уникален

### Hints
<details>
<summary>Подсказка 1</summary>
Подсчитайте частоты (Counter). Как найти top-k? Heap или сортировка.
</details>

<details>
<summary>Подсказка 2</summary>
Для O(n): Bucket Sort. Создайте массив из n+1 списков. bucket[freq] = [элементы с такой частотой]. Пройдитесь от конца.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Sort by frequency | O(n log n) | O(n) |
| Heap (heapq.nlargest) | O(n log k) | O(n) |
| **Bucket Sort** | **O(n)** | **O(n)** |

---

## 7. Isomorphic Strings
**Difficulty:** 🟢 Easy  
**Паттерн:** Bijection / Dual Hash Map

### Problem
Даны строки `s` и `t`. Определите, **изоморфны** ли они.

Две строки изоморфны, если символы в `s` можно заменить на символы `t` с сохранением порядка. Никакие два разных символа не могут маппиться на один, и наоборот (биекция).

### Example 1
```
Input: s = "egg", t = "add"
Output: True
Explanation: e→a, g→d. Маппинг взаимно однозначный.
```

### Example 2
```
Input: s = "foo", t = "bar"
Output: False
Explanation: o→a и o→r — один символ маппится на два разных.
```

### Example 3
```
Input: s = "paper", t = "title"
Output: True
Explanation: p→t, a→i, e→l, r→e.
```

### Example 4
```
Input: s = "badc", t = "baba"
Output: False
Explanation: d→b и b→b — два разных символа маппятся на один.
```

### Constraints
- `1 <= len(s) <= 5 * 10^4`
- `len(s) == len(t)`

### Hints
<details>
<summary>Подсказка 1</summary>
Используйте два словаря: s→t и t→s. Проверяйте оба направления маппинга.
</details>

<details>
<summary>Подсказка 2</summary>
Альтернатива: сравните «паттерн первых вхождений» обеих строк. Например, "egg" → [0,1,1], "add" → [0,1,1].
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Dual Hash Map** | **O(n)** | **O(n)** |

---

## 8. Longest Consecutive Sequence
**Difficulty:** 🟡 Medium  
**Паттерн:** Hash Set + Linear Scan

### Problem
Дан несортированный массив целых чисел `nums`. Найдите длину **самой длинной последовательности** идущих подряд чисел (consecutive elements).

Алгоритм должен работать за **O(n)**.

### Example 1
```
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: Последовательность [1, 2, 3, 4] — длина 4.
```

### Example 2
```
Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
Explanation: Последовательность [0, 1, 2, 3, 4, 5, 6, 7, 8] — длина 9.
```

### Example 3
```
Input: nums = []
Output: 0
```

### Constraints
- `0 <= len(nums) <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

### Hints
<details>
<summary>Подсказка 1</summary>
Положите все числа в set. Начало последовательности — число, у которого нет (num - 1) в set.
</details>

<details>
<summary>Подсказка 2</summary>
Для каждого начала: считайте длину, проверяя num+1, num+2, ... в set. Обновляйте максимум.
</details>

<details>
<summary>Подсказка 3</summary>
Каждый элемент посещается не более 2 раз → суммарно O(n), не O(n²).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Sorting | O(n log n) | O(1) |
| **Hash Set + Smart Scan** | **O(n)** | **O(n)** |

---

## 9. Word Pattern
**Difficulty:** 🟢 Easy  
**Паттерн:** Bijection / Dual Hash Map

### Problem
Дан паттерн `pattern` (строка из букв) и строка `s` (слова через пробел). Проверьте, соответствует ли `s` паттерну — полная **биекция** между буквами паттерна и словами.

### Example 1
```
Input: pattern = "abba", s = "dog cat cat dog"
Output: True
Explanation: a↔dog, b↔cat. Биекция выполняется.
```

### Example 2
```
Input: pattern = "abba", s = "dog cat cat fish"
Output: False
Explanation: a→dog и a→fish — не совпадает.
```

### Example 3
```
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: False
Explanation: a→dog и a→cat — нет однозначного маппинга.
```

### Example 4
```
Input: pattern = "abba", s = "dog dog dog dog"
Output: False
Explanation: a→dog и b→dog — два разных символа маппятся на одно слово.
```

### Constraints
- `1 <= len(pattern) <= 300`
- `pattern` содержит только строчные латинские буквы
- `s` содержит строчные буквы и пробелы

### Hints
<details>
<summary>Подсказка 1</summary>
Разбейте s на слова. Если len(words) != len(pattern) → False.
</details>

<details>
<summary>Подсказка 2</summary>
Два словаря: pattern_char → word и word → pattern_char. Проверяйте оба направления.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Dual Hash Map** | **O(n)** | **O(n)** |

---

## 10. 4Sum II
**Difficulty:** 🟡 Medium  
**Паттерн:** Hash Map + Divide in Half

### Problem
Даны 4 массива целых чисел `nums1`, `nums2`, `nums3`, `nums4` одинаковой длины `n`.

Подсчитайте количество кортежей `(i, j, k, l)`, таких что:  
`nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`

### Example 1
```
Input: nums1 = [1, 2], nums2 = [-2, -1], nums3 = [-1, 2], nums4 = [0, 2]
Output: 2
Explanation:
  (0,0,0,1): 1 + (-2) + (-1) + 2 = 0
  (1,1,0,0): 2 + (-1) + (-1) + 0 = 0
```

### Example 2
```
Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
```

### Constraints
- `n == len(nums1) == len(nums2) == len(nums3) == len(nums4)`
- `1 <= n <= 200`
- `-2^28 <= nums1[i], nums2[j], nums3[k], nums4[l] <= 2^28`

### Hints
<details>
<summary>Подсказка 1</summary>
Brute Force O(n⁴) — слишком медленно. Разделите 4 массива на две группы по 2.
</details>

<details>
<summary>Подсказка 2</summary>
Подсчитайте все суммы nums1[i] + nums2[j] в dict. Для каждой суммы nums3[k] + nums4[l] ищите -(sum) в dict.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n⁴) | O(1) |
| **Hash Map (2+2 split)** | **O(n²)** | **O(n²)** |
