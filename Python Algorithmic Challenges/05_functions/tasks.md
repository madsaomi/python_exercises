# 🧩 Functions — Задачи

---

## 1. Plus One
**Difficulty:** 🟢 Easy  
**Паттерн:** Array Manipulation / Carry

### Problem
Дан массив `digits`, представляющий неотрицательное целое число. Цифры хранятся старшими разрядами вперёд. Прибавьте к числу `1` и верните результат как массив цифр.

### Example 1
```
Input: digits = [1, 2, 3]
Output: [1, 2, 4]
Explanation: 123 + 1 = 124
```

### Example 2
```
Input: digits = [4, 3, 2, 1]
Output: [4, 3, 2, 2]
```

### Example 3
```
Input: digits = [9, 9, 9]
Output: [1, 0, 0, 0]
Explanation: 999 + 1 = 1000. Массив увеличивается на 1 элемент.
```

### Constraints
- `1 <= len(digits) <= 100`
- `0 <= digits[i] <= 9`
- Число не содержит ведущих нулей (кроме самого числа 0)

### Hints
<details>
<summary>Подсказка 1</summary>
Обрабатывайте с конца. Если digit < 9 — просто +1 и вернуть. Если 9 — ставим 0 и переносим.
</details>

<details>
<summary>Подсказка 2</summary>
Если все цифры были 9 (цикл закончился) — добавьте 1 в начало.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Right-to-left with carry** | **O(n)** | **O(1)** (in-place, кроме случая 999→1000) |

---

## 2. Add Two Numbers (as Arrays)
**Difficulty:** 🟡 Medium  
**Паттерн:** Elementary Math / Carry

### Problem
Даны два неотрицательных числа, представленные массивами цифр в **обратном порядке** (младший разряд первый). Верните их сумму в таком же формате.

### Example 1
```
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]
Explanation: 342 + 465 = 807
```

### Example 2
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

### Example 3
```
Input: l1 = [9, 9, 9, 9], l2 = [9, 9, 9]
Output: [8, 9, 9, 0, 1]
Explanation: 9999 + 999 = 10998
```

### Constraints
- `1 <= len(l1), len(l2) <= 100`
- `0 <= l1[i], l2[i] <= 9`

### Hints
<details>
<summary>Подсказка 1</summary>
Складывайте поразрядно с переносом (carry). carry = sum // 10, digit = sum % 10.
</details>

<details>
<summary>Подсказка 2</summary>
Продолжайте пока есть цифры в l1, l2 или carry > 0.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Elementary Addition** | **O(max(m, n))** | **O(max(m, n))** |

---

## 3. Single Number
**Difficulty:** 🟢 Easy  
**Паттерн:** Bit Manipulation (XOR)

### Problem
Дан непустой массив, где каждый элемент встречается **ровно дважды**, кроме одного. Найдите этот единственный элемент.

Решите за **O(n)** времени и **O(1)** дополнительной памяти.

### Example 1
```
Input: nums = [2, 2, 1]
Output: 1
```

### Example 2
```
Input: nums = [4, 1, 2, 1, 2]
Output: 4
```

### Example 3
```
Input: nums = [1]
Output: 1
```

### Constraints
- `1 <= len(nums) <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Каждый элемент, кроме одного, встречается ровно дважды

### Hints
<details>
<summary>Подсказка 1</summary>
XOR обладает свойствами: a ^ a = 0, a ^ 0 = a, коммутативность и ассоциативность.
</details>

<details>
<summary>Подсказка 2</summary>
XOR всех элементов массива — парные обнулятся, останется единственный.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Hash Set | O(n) | O(n) |
| Sort + scan | O(n log n) | O(1) |
| **XOR** | **O(n)** | **O(1)** |

---

## 4. Missing Number
**Difficulty:** 🟢 Easy  
**Паттерн:** Math (Gauss Sum) / XOR

### Problem
Дан массив `nums` из `n` **различных** чисел в диапазоне `[0, n]`. Найдите единственное число из этого диапазона, которое **отсутствует** в массиве.

### Example 1
```
Input: nums = [3, 0, 1]
Output: 2
Explanation: n = 3, числа 0..3: пропущено 2.
```

### Example 2
```
Input: nums = [0, 1]
Output: 2
Explanation: n = 2, числа 0..2: пропущено 2.
```

### Example 3
```
Input: nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
Output: 8
```

### Constraints
- `n == len(nums)`
- `0 <= nums[i] <= n`
- Все числа уникальны

### Hints
<details>
<summary>Подсказка 1</summary>
Сумма чисел от 0 до n: n*(n+1)/2. Вычтите сумму массива — получите пропущенное.
</details>

<details>
<summary>Подсказка 2</summary>
Альтернатива: XOR всех чисел 0..n и всех элементов массива. Результат — пропущенное число.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Sort + scan | O(n log n) | O(1) |
| Hash Set | O(n) | O(n) |
| **Gauss Sum** | **O(n)** | **O(1)** |
| **XOR** | **O(n)** | **O(1)** |

---

## 5. Majority Element
**Difficulty:** 🟢 Easy  
**Паттерн:** Boyer-Moore Voting Algorithm

### Problem
Дан массив `nums` длины `n`. Найдите **элемент большинства** — элемент, который встречается более `⌊n/2⌋` раз.

Гарантируется, что такой элемент всегда существует.

### Example 1
```
Input: nums = [3, 2, 3]
Output: 3
```

### Example 2
```
Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
Explanation: 2 встречается 4 раза из 7. 4 > 7/2 = 3.5 ✓
```

### Constraints
- `n == len(nums)`
- `1 <= n <= 5 * 10^4`
- Элемент большинства всегда существует

### Hints
<details>
<summary>Подсказка 1</summary>
Hash Map: подсчитайте частоты и найдите max. O(n) время, O(n) память.
</details>

<details>
<summary>Подсказка 2</summary>
Boyer-Moore: candidate и count. Если count == 0 → новый candidate. Если nums[i] == candidate → count++, иначе count--. Финальный candidate — ответ.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Hash Map | O(n) | O(n) |
| Sorting | O(n log n) | O(1) |
| **Boyer-Moore Voting** | **O(n)** | **O(1)** |

---

## 6. Number of 1 Bits
**Difficulty:** 🟢 Easy  
**Паттерн:** Bit Manipulation

### Problem
Дано положительное целое число `n`. Верните количество **единичных битов** (бит со значением 1) в его двоичном представлении (Hamming weight).

### Example 1
```
Input: n = 11
Output: 3
Explanation: 11 = 1011₂ → три единичных бита.
```

### Example 2
```
Input: n = 128
Output: 1
Explanation: 128 = 10000000₂ → один единичный бит.
```

### Example 3
```
Input: n = 2147483645
Output: 30
```

### Constraints
- `1 <= n <= 2^31 - 1`

### Hints
<details>
<summary>Подсказка 1</summary>
n & 1 даёт младший бит. Сдвигайте n вправо (n >>= 1), считая единицы.
</details>

<details>
<summary>Подсказка 2</summary>
Трюк Кернигана: n & (n-1) убирает самый младший единичный бит. Считайте итерации до n == 0.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Bit shift loop | O(32) | O(1) |
| **Brian Kernighan's** | **O(k)** | **O(1)** (k = количество единиц) |

---

## 7. Reverse Integer
**Difficulty:** 🟡 Medium  
**Паттерн:** Math / Digit Extraction

### Problem
Дано 32-битное знаковое целое число `x`. Разверните его цифры.  
Если результат выходит за пределы `[-2^31, 2^31 - 1]` — верните `0`.

**Нельзя** хранить 64-битные числа (предполагается ограничение окружения).

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

### Example 3
```
Input: x = 120
Output: 21
Explanation: Ведущие нули отбрасываются.
```

### Example 4
```
Input: x = 0
Output: 0
```

### Constraints
- `-2^31 <= x <= 2^31 - 1`

### Hints
<details>
<summary>Подсказка 1</summary>
Извлекайте цифры: digit = x % 10, x = x // 10. Собирайте: result = result * 10 + digit.
</details>

<details>
<summary>Подсказка 2</summary>
Проверяйте overflow ПЕРЕД умножением на 10: если result > (2^31 - 1) // 10 → overflow.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Math (pop & push digits)** | **O(log x)** | **O(1)** |

---

## 8. Implement strStr()
**Difficulty:** 🟢 Easy  
**Паттерн:** String Matching

### Problem
Даны строки `haystack` и `needle`. Верните индекс **первого вхождения** `needle` в `haystack`, или `-1` если не найдено.

### Example 1
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" начинается с индекса 0 (и 6), возвращаем 0.
```

### Example 2
```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
```

### Example 3
```
Input: haystack = "hello", needle = "ll"
Output: 2
```

### Constraints
- `1 <= len(haystack), len(needle) <= 10^4`
- Строки содержат только строчные латинские буквы

### Hints
<details>
<summary>Подсказка 1</summary>
Наивный подход: для каждой позиции i проверяйте haystack[i:i+len(needle)] == needle.
</details>

<details>
<summary>Подсказка 2</summary>
Продвинутые алгоритмы: KMP (O(n+m)), Rabin-Karp (хеширование).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Sliding Window** | **O(n × m)** | **O(1)** |
| KMP | O(n + m) | O(m) |
| Rabin-Karp | O(n + m) avg | O(1) |

---

## 9. Integer to Roman
**Difficulty:** 🟡 Medium  
**Паттерн:** Greedy / Table Lookup

### Problem
Преобразуйте целое число `num` в римское число.

Таблица значений:
```
M=1000, CM=900, D=500, CD=400,
C=100, XC=90, L=50, XL=40,
X=10, IX=9, V=5, IV=4, I=1
```

### Example 1
```
Input: num = 3749
Output: "MMMDCCXLIX"
Explanation: 3000=MMM, 700=DCC, 40=XL, 9=IX
```

### Example 2
```
Input: num = 58
Output: "LVIII"
Explanation: 50=L, 5=V, 3=III
```

### Example 3
```
Input: num = 1994
Output: "MCMXCIV"
Explanation: 1000=M, 900=CM, 90=XC, 4=IV
```

### Constraints
- `1 <= num <= 3999`

### Hints
<details>
<summary>Подсказка 1</summary>
Создайте таблицу из 13 пар (значение, символ), отсортированную по убыванию. Жадно вычитайте.
</details>

<details>
<summary>Подсказка 2</summary>
Пока num >= value: result += symbol, num -= value. Переходите к следующей паре.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Greedy with table** | **O(1)** | **O(1)** (ограничено 3999) |

---

## 10. Encode and Decode Strings
**Difficulty:** 🟡 Medium  
**Паттерн:** String Encoding / Delimiter

### Problem
Реализуйте два метода:
- `encode(strs: List[str]) -> str` — кодирует список строк в одну строку
- `decode(s: str) -> List[str]` — декодирует обратно в список строк

Строки могут содержать **любые символы**, включая разделители.

### Example 1
```
Input: strs = ["hello", "world"]
Encode: "5#hello5#world"
Decode: ["hello", "world"]
```

### Example 2
```
Input: strs = ["we", "say", ":", "yes"]
Encode: "2#we3#say1#:3#yes"
Decode: ["we", "say", ":", "yes"]
```

### Example 3
```
Input: strs = [""]
Encode: "0#"
Decode: [""]
```

### Constraints
- `0 <= len(strs) <= 200`
- `0 <= len(strs[i]) <= 200`
- Строки могут содержать любые из 256 ASCII-символов

### Hints
<details>
<summary>Подсказка 1</summary>
Нельзя использовать простой разделитель (он может быть в строке). Используйте длину + разделитель.
</details>

<details>
<summary>Подсказка 2</summary>
Формат: "{length}#{string}". При декодировании: читаем число до #, затем берём length символов.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Length-prefixed encoding** | **O(n)** | **O(n)** |
