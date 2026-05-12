# 🧩 Loops & Math — Задачи

---

## 1. Fizz Buzz
**Difficulty:** 🟢 Easy  
**Паттерн:** Modular Arithmetic

### Problem
Дано число `n`. Верните массив строк `answer` длины `n`, где `answer[i]` (1-indexed):
- `"FizzBuzz"` если `i` делится на 3 **и** на 5
- `"Fizz"` если делится только на 3
- `"Buzz"` если делится только на 5
- `str(i)` иначе

### Example 1
```
Input: n = 5
Output: ["1", "2", "Fizz", "4", "Buzz"]
```

### Example 2
```
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
```

### Constraints
- `1 <= n <= 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Проверяйте деление на 15 первым (или на 3 и 5 одновременно), затем на 3, затем на 5.
</details>

<details>
<summary>Подсказка 2</summary>
Элегантный подход: конкатенация строк. result = "". Если делится на 3: result += "Fizz". Если на 5: result += "Buzz". Если пусто: result = str(i).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **If-Elif Chain** | **O(n)** | **O(n)** |
| String Concatenation | O(n) | O(n) |

---

## 2. Palindrome Number
**Difficulty:** 🟢 Easy  
**Паттерн:** Math (Reverse Half)

### Problem
Определите, является ли целое число `x` палиндромом.  
Решите **без преобразования в строку**.

### Example 1
```
Input: x = 121
Output: True
Explanation: 121 читается как 121 справа налево.
```

### Example 2
```
Input: x = -121
Output: False
Explanation: Слева направо: -121. Справа налево: 121-. Не палиндром.
```

### Example 3
```
Input: x = 10
Output: False
Explanation: Справа налево: 01. Не палиндром.
```

### Constraints
- `-2^31 <= x <= 2^31 - 1`

### Hints
<details>
<summary>Подсказка 1</summary>
Отрицательные числа — не палиндромы. Числа, оканчивающиеся на 0 (кроме 0) — тоже.
</details>

<details>
<summary>Подсказка 2</summary>
Реверсируйте только вторую половину числа. Когда reversed >= x, сравните: x == reversed или x == reversed // 10 (для нечётной длины).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Convert to string | O(n) | O(n) |
| **Reverse half** | **O(log n)** | **O(1)** |

---

## 3. Roman to Integer
**Difficulty:** 🟢 Easy  
**Паттерн:** Hash Map + Linear Scan

### Problem
Дана строка с римским числом. Преобразуйте его в целое десятичное число.

Римские цифры: `I=1, V=5, X=10, L=50, C=100, D=500, M=1000`  
Особые комбинации: `IV=4, IX=9, XL=40, XC=90, CD=400, CM=900`

### Example 1
```
Input: s = "III"
Output: 3
```

### Example 2
```
Input: s = "LVIII"
Output: 58
Explanation: L=50, V=5, III=3 → 58
```

### Example 3
```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M=1000, CM=900, XC=90, IV=4 → 1994
```

### Constraints
- `1 <= len(s) <= 15`
- `s` содержит только символы `I, V, X, L, C, D, M`
- Число в диапазоне `[1, 3999]`

### Hints
<details>
<summary>Подсказка 1</summary>
Если текущий символ < следующего (например, I перед V), то вычитаем. Иначе — прибавляем.
</details>

<details>
<summary>Подсказка 2</summary>
Пройдитесь справа налево: если roman[i] < roman[i+1], вычитайте; иначе прибавляйте.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Linear Scan (right to left)** | **O(n)** | **O(1)** |

---

## 4. Power of Three
**Difficulty:** 🟢 Easy  
**Паттерн:** Math / Loop

### Problem
Определите, является ли число `n` степенью тройки. То есть, существует ли целое `k >= 0`, такое что `n == 3^k`.

### Example 1
```
Input: n = 27
Output: True
Explanation: 3^3 = 27
```

### Example 2
```
Input: n = 0
Output: False
```

### Example 3
```
Input: n = -1
Output: False
```

### Example 4
```
Input: n = 9
Output: True
Explanation: 3^2 = 9
```

### Constraints
- `-2^31 <= n <= 2^31 - 1`

### Hints
<details>
<summary>Подсказка 1</summary>
Цикл: делите n на 3, пока делится нацело. Если в конце n == 1 → True.
</details>

<details>
<summary>Подсказка 2</summary>
Без цикла: максимальная степень 3 в int32 — 3^19 = 1162261467. Если 1162261467 % n == 0 → True.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Loop (divide by 3)** | **O(log₃ n)** | **O(1)** |
| Math (max power) | O(1) | O(1) |

---

## 5. Count Primes
**Difficulty:** 🟡 Medium  
**Паттерн:** Sieve of Eratosthenes

### Problem
Подсчитайте количество **простых** чисел, строго меньших `n`.

### Example 1
```
Input: n = 10
Output: 4
Explanation: Простые < 10: 2, 3, 5, 7.
```

### Example 2
```
Input: n = 0
Output: 0
```

### Example 3
```
Input: n = 1
Output: 0
```

### Example 4
```
Input: n = 2
Output: 0
Explanation: Нет простых < 2.
```

### Constraints
- `0 <= n <= 5 * 10^6`

### Hints
<details>
<summary>Подсказка 1</summary>
Наивный подход (проверка каждого числа) — O(n√n). Слишком медленно для n = 5·10⁶.
</details>

<details>
<summary>Подсказка 2</summary>
Решето Эратосфена: создайте массив bool[n]. Для каждого простого p: помечайте p², p²+p, p²+2p, ... как составные.
</details>

<details>
<summary>Подсказка 3</summary>
Достаточно проверять p до √n. Оставшиеся True — простые.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n√n) | O(1) |
| **Sieve of Eratosthenes** | **O(n log log n)** | **O(n)** |

---

## 6. Happy Number
**Difficulty:** 🟢 Easy  
**Паттерн:** Hash Set / Floyd's Cycle Detection

### Problem
Число «счастливое», если при повторном замещении числа суммой квадратов его цифр, процесс в итоге приходит к `1`.

Если процесс зацикливается и никогда не достигнет 1 — число не счастливое.

### Example 1
```
Input: n = 19
Output: True
Explanation: 
  1² + 9² = 82
  8² + 2² = 68
  6² + 8² = 100
  1² + 0² + 0² = 1 ✓
```

### Example 2
```
Input: n = 2
Output: False
Explanation: 
  2→4→16→37→58→89→145→42→20→4→... (цикл!)
```

### Constraints
- `1 <= n <= 2^31 - 1`

### Hints
<details>
<summary>Подсказка 1</summary>
Ключевой вопрос: как обнаружить цикл? Используйте set для хранения уже посещённых чисел.
</details>

<details>
<summary>Подсказка 2</summary>
Альтернатива: алгоритм Флойда (быстрый и медленный указатели) — без дополнительной памяти.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Hash Set** | **O(log n)** | **O(log n)** |
| Floyd's Cycle | O(log n) | O(1) |

---

## 7. Excel Sheet Column Number
**Difficulty:** 🟢 Easy  
**Паттерн:** Base-26 Conversion

### Problem
Дано название столбца Excel (как в таблице). Верните его порядковый номер.

```
A → 1,  B → 2,  ...,  Z → 26,
AA → 27,  AB → 28,  ...,  AZ → 52,
BA → 53, ...
```

### Example 1
```
Input: columnTitle = "A"
Output: 1
```

### Example 2
```
Input: columnTitle = "AB"
Output: 28
Explanation: A=1, B=2 → 1*26 + 2 = 28
```

### Example 3
```
Input: columnTitle = "ZY"
Output: 701
Explanation: Z=26, Y=25 → 26*26 + 25 = 701
```

### Constraints
- `1 <= len(columnTitle) <= 7`
- `columnTitle` содержит только заглавные латинские буквы

### Hints
<details>
<summary>Подсказка 1</summary>
Это система счисления с основанием 26, где A=1, B=2, ..., Z=26.
</details>

<details>
<summary>Подсказка 2</summary>
result = 0. Для каждого символа: result = result * 26 + (ord(char) - ord('A') + 1).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Base-26 conversion** | **O(n)** | **O(1)** |

---

## 8. Pow(x, n)
**Difficulty:** 🟡 Medium  
**Паттерн:** Fast Exponentiation (Binary)

### Problem
Реализуйте `myPow(x, n)` — вычисление `x^n`.

Используйте **быстрое возведение в степень** за O(log n).

### Example 1
```
Input: x = 2.0, n = 10
Output: 1024.0
```

### Example 2
```
Input: x = 2.1, n = 3
Output: 9.261
```

### Example 3
```
Input: x = 2.0, n = -2
Output: 0.25
Explanation: 2^(-2) = 1 / 2^2 = 1/4 = 0.25
```

### Constraints
- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`
- Если x == 0, n > 0

### Hints
<details>
<summary>Подсказка 1</summary>
x^n = (x²)^(n/2) если n чётный, x · (x²)^((n-1)/2) если нечётный.
</details>

<details>
<summary>Подсказка 2</summary>
Если n < 0: x^n = (1/x)^(-n). Осторожно: -n может вызвать overflow для n = -2^31!
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Linear | O(n) | O(1) |
| **Binary Exponentiation** | **O(log n)** | **O(1)** итеративно / **O(log n)** рекурсивно |

---

## 9. Sqrt(x)
**Difficulty:** 🟢 Easy  
**Паттерн:** Binary Search

### Problem
Вычислите целочисленный квадратный корень из `x` **без** использования встроенных функций.

Верните только целую часть (отбросьте дробную).

### Example 1
```
Input: x = 4
Output: 2
```

### Example 2
```
Input: x = 8
Output: 2
Explanation: √8 = 2.828..., отбрасываем → 2
```

### Example 3
```
Input: x = 0
Output: 0
```

### Example 4
```
Input: x = 1
Output: 1
```

### Constraints
- `0 <= x <= 2^31 - 1`

### Hints
<details>
<summary>Подсказка 1</summary>
Бинарный поиск: ищите наибольшее mid, такое что mid * mid <= x.
</details>

<details>
<summary>Подсказка 2</summary>
left = 0, right = x. Если mid*mid <= x → запоминаем mid, left = mid + 1. Иначе right = mid - 1.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Linear search | O(√x) | O(1) |
| **Binary Search** | **O(log x)** | **O(1)** |
| Newton's Method | O(log x) | O(1) |

---

## 10. Ugly Number
**Difficulty:** 🟢 Easy  
**Паттерн:** Math / Division

### Problem
«Уродливое число» (ugly number) — положительное число, чьи простые множители ограничены `2, 3, 5`.

Число `1` считается ugly. Определите, является ли `n` ugly number.

### Example 1
```
Input: n = 6
Output: True
Explanation: 6 = 2 × 3
```

### Example 2
```
Input: n = 1
Output: True
Explanation: 1 не имеет простых множителей — считается ugly.
```

### Example 3
```
Input: n = 14
Output: False
Explanation: 14 = 2 × 7. Число 7 не в {2, 3, 5}.
```

### Example 4
```
Input: n = 0
Output: False
```

### Constraints
- `-2^31 <= n <= 2^31 - 1`

### Hints
<details>
<summary>Подсказка 1</summary>
Если n <= 0 → False. Делите n на 2, пока делится. Потом на 3. Потом на 5. Если осталось 1 → True.
</details>

<details>
<summary>Подсказка 2</summary>
Порядок деления не важен. Главное — убрать все множители 2, 3, 5.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Iterative Division** | **O(log n)** | **O(1)** |
