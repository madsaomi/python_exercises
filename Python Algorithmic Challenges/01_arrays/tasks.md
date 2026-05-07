# 🧩 Arrays — Задачи

---

## 1. Two Sum
**Difficulty:** 🟢 Easy  
**Паттерн:** Hash Map

### Problem
Дан массив целых чисел `nums` и целое число `target`.  
Верните индексы двух чисел, сумма которых равна `target`.

Каждый вход имеет **ровно одно решение**. Нельзя использовать один элемент дважды.  
Ответ можно вернуть в любом порядке.

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
Explanation: nums[1] + nums[2] = 2 + 4 = 6
```

### Example 3
```
Input: nums = [3, 3], target = 6
Output: [0, 1]
```

### Constraints
- `2 <= len(nums) <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- Ровно одно решение существует

### Hints
<details>
<summary>Подсказка 1</summary>
Brute force: перебрать все пары — O(n²). Можно ли лучше?
</details>

<details>
<summary>Подсказка 2</summary>
Если нам нужен target - nums[i], можем ли мы найти это значение за O(1)?
</details>

<details>
<summary>Подсказка 3</summary>
Используйте словарь (hash map): ключ — число, значение — его индекс. За один проход по массиву проверяйте, есть ли дополнение (target - num) в словаре.
</details>

### Approach
| Подход | Время | Память | Описание |
|--------|-------|--------|----------|
| Brute Force | O(n²) | O(1) | Два вложенных цикла |
| **Hash Map** | **O(n)** | **O(n)** | Один проход + словарь |

---

## 2. Remove Duplicates from Sorted Array
**Difficulty:** 🟢 Easy  
**Паттерн:** Two Pointers

### Problem
Дан отсортированный массив `nums` в порядке неубывания.  
Удалите дубликаты **in-place** так, чтобы каждый уникальный элемент появился **один раз**.  
Относительный порядок должен сохраниться.

Верните количество уникальных элементов `k`. Первые `k` элементов `nums` должны содержать уникальные элементы.

### Example 1
```
Input: nums = [1, 1, 2]
Output: 2, nums = [1, 2, ...]
Explanation: Функция возвращает k=2. Первые два элемента nums — [1, 2].
```

### Example 2
```
Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, nums = [0, 1, 2, 3, 4, ...]
Explanation: Функция возвращает k=5. Первые пять элементов — [0, 1, 2, 3, 4].
```

### Example 3
```
Input: nums = [1]
Output: 1, nums = [1]
```

### Constraints
- `1 <= len(nums) <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` отсортирован по неубыванию

### Hints
<details>
<summary>Подсказка 1</summary>
Массив уже отсортирован — дубликаты идут подряд.
</details>

<details>
<summary>Подсказка 2</summary>
Используйте два указателя: slow (позиция записи) и fast (текущий элемент). Если nums[fast] != nums[slow], записывайте его.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Two Pointers** | **O(n)** | **O(1)** |

---

## 3. Best Time to Buy and Sell Stock
**Difficulty:** 🟢 Easy  
**Паттерн:** Sliding Window / Greedy

### Problem
Дан массив `prices`, где `prices[i]` — цена акции в `i`-й день.  
Вы можете выбрать **один день** для покупки и **один день в будущем** для продажи.  
Верните **максимальную прибыль**. Если прибыль невозможна — верните `0`.

### Example 1
```
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Купить в день 2 (цена 1), продать в день 5 (цена 6). 
Прибыль = 6 - 1 = 5.
Нельзя купить в день 2 и продать в день 1 — продажа должна быть после покупки.
```

### Example 2
```
Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: Цена всё время падает — выгодной сделки нет.
```

### Example 3
```
Input: prices = [2, 4, 1]
Output: 2
Explanation: Купить в день 1 (цена 2), продать в день 2 (цена 4). Прибыль = 2.
```

### Constraints
- `1 <= len(prices) <= 10^5`
- `0 <= prices[i] <= 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Какой минимальный price мы видели до сих пор?
</details>

<details>
<summary>Подсказка 2</summary>
Поддерживайте переменную min_price. На каждом шаге обновляйте max_profit = max(max_profit, price - min_price).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n²) | O(1) |
| **One Pass (Greedy)** | **O(n)** | **O(1)** |

---

## 4. Contains Duplicate
**Difficulty:** 🟢 Easy  
**Паттерн:** Hash Set

### Problem
Дан массив целых чисел `nums`.  
Верните `True`, если в массиве есть хотя бы один дубликат.  
Верните `False`, если все элементы уникальны.

### Example 1
```
Input: nums = [1, 2, 3, 1]
Output: True
Explanation: nums[0] == nums[3] = 1
```

### Example 2
```
Input: nums = [1, 2, 3, 4]
Output: False
```

### Example 3
```
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: True
```

### Constraints
- `1 <= len(nums) <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

### Hints
<details>
<summary>Подсказка 1</summary>
Какая структура данных позволяет проверить наличие элемента за O(1)?
</details>

<details>
<summary>Подсказка 2</summary>
Используйте set. Если длина set меньше длины массива — есть дубликаты.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n²) | O(1) |
| Sorting | O(n log n) | O(1) |
| **Hash Set** | **O(n)** | **O(n)** |

---

## 5. Maximum Subarray
**Difficulty:** 🟡 Medium  
**Паттерн:** Kadane's Algorithm / Dynamic Programming

### Problem
Дан массив целых чисел `nums`.  
Найдите **подмассив** (непрерывную подпоследовательность) с **наибольшей суммой** и верните эту сумму.

Подмассив — это непрерывная непустая часть массива.

### Example 1
```
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: Подмассив [4, -1, 2, 1] имеет наибольшую сумму 6.
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
Explanation: Весь массив — оптимальный подмассив.
```

### Example 4
```
Input: nums = [-1]
Output: -1
Explanation: Массив из одного отрицательного числа. Нельзя взять пустой подмассив.
```

### Constraints
- `1 <= len(nums) <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Подумайте: стоит ли продолжать текущий подмассив, или лучше начать новый с текущего элемента?
</details>

<details>
<summary>Подсказка 2</summary>
Алгоритм Кадане: current_sum = max(nums[i], current_sum + nums[i]). Обновляйте max_sum на каждом шаге.
</details>

<details>
<summary>Подсказка 3</summary>
Если текущая сумма стала отрицательной, «сбросьте» её — начните новый подмассив.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n²) | O(1) |
| **Kadane's Algorithm** | **O(n)** | **O(1)** |
| Divide & Conquer | O(n log n) | O(log n) |

---

## 6. Merge Sorted Arrays
**Difficulty:** 🟢 Easy  
**Паттерн:** Two Pointers (от конца)

### Problem
Даны два отсортированных массива `nums1` и `nums2`.  
Объедините `nums2` в `nums1` как один отсортированный массив **in-place**.

`nums1` имеет длину `m + n`, где первые `m` элементов — значения, остальные `n` — нули (заполнители).  
`nums2` имеет длину `n`.

### Example 1
```
Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
Output: [1, 2, 2, 3, 5, 6]
```

### Example 2
```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
```

### Example 3
```
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: nums1 пуст (m=0), просто копируем nums2.
```

### Constraints
- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`

### Hints
<details>
<summary>Подсказка 1</summary>
Если заполнять с начала, придётся сдвигать элементы. Что если заполнять с конца?
</details>

<details>
<summary>Подсказка 2</summary>
Используйте три указателя: p1 = m-1, p2 = n-1, p = m+n-1. Сравнивайте nums1[p1] и nums2[p2], записывайте бо́льший в nums1[p].
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Sort after merge | O((m+n) log(m+n)) | O(1) |
| **Two Pointers (от конца)** | **O(m + n)** | **O(1)** |

---

## 7. Product of Array Except Self
**Difficulty:** 🟡 Medium  
**Паттерн:** Prefix / Suffix Product

### Problem
Дан массив целых чисел `nums` длины `n`.  
Верните массив `answer`, где `answer[i]` равен произведению **всех элементов** `nums`, кроме `nums[i]`.

**Нельзя** использовать операцию деления. Решение должно быть за O(n).

### Example 1
```
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Explanation: 
  answer[0] = 2*3*4 = 24
  answer[1] = 1*3*4 = 12
  answer[2] = 1*2*4 = 8
  answer[3] = 1*2*3 = 6
```

### Example 2
```
Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
Explanation: Наличие нуля обнуляет все произведения, кроме позиции самого нуля.
```

### Constraints
- `2 <= len(nums) <= 10^5`
- `-30 <= nums[i] <= 30`
- Произведение любого подмножества помещается в 32-bit integer

### Hints
<details>
<summary>Подсказка 1</summary>
Для каждого элемента answer[i] = (произведение всех слева) × (произведение всех справа).
</details>

<details>
<summary>Подсказка 2</summary>
Сделайте два прохода: слева направо (prefix product) и справа налево (suffix product).
</details>

<details>
<summary>Подсказка 3</summary>
Для O(1) дополнительной памяти: используйте массив answer для prefix, затем переменную для suffix.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n²) | O(1) |
| **Prefix + Suffix** | **O(n)** | **O(1)** |

---

## 8. Move Zeroes
**Difficulty:** 🟢 Easy  
**Паттерн:** Two Pointers

### Problem
Дан массив целых чисел `nums`.  
Переместите все `0` в конец, сохранив относительный порядок ненулевых элементов.  
Модифицируйте массив **in-place** без создания копии.

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

### Example 3
```
Input: nums = [1, 2, 3]
Output: [1, 2, 3]
Explanation: Нулей нет — массив не меняется.
```

### Constraints
- `1 <= len(nums) <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

### Hints
<details>
<summary>Подсказка 1</summary>
Используйте указатель slow, который отслеживает позицию для записи ненулевого элемента.
</details>

<details>
<summary>Подсказка 2</summary>
Пройдитесь по массиву. Если nums[fast] != 0, поменяйте nums[slow] и nums[fast] местами, увеличьте slow.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Extra array | O(n) | O(n) |
| **Two Pointers (swap)** | **O(n)** | **O(1)** |

---

## 9. Container With Most Water
**Difficulty:** 🟡 Medium  
**Паттерн:** Two Pointers (от краёв к центру)

### Problem
Дан массив целых чисел `height` длины `n`.  
Каждый элемент представляет вертикальную линию от `(i, 0)` до `(i, height[i])`.

Найдите две линии, которые вместе с осью X образуют контейнер с **наибольшим количеством воды**.

Верните максимальное количество воды, которое контейнер может вместить.

### Example 1
```
Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
Explanation: Линии с индексами 1 и 8 (высоты 8 и 7).
Ширина = 8 - 1 = 7. Высота = min(8, 7) = 7.
Вода = 7 * 7 = 49.
```

### Example 2
```
Input: height = [1, 1]
Output: 1
```

### Example 3
```
Input: height = [4, 3, 2, 1, 4]
Output: 16
Explanation: Линии с индексами 0 и 4 (высоты 4 и 4).
Ширина = 4. Высота = 4. Вода = 16.
```

### Constraints
- `2 <= len(height) <= 10^5`
- `0 <= height[i] <= 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Brute force O(n²): проверить все пары. Но можно использовать два указателя.
</details>

<details>
<summary>Подсказка 2</summary>
Начните с left=0, right=n-1. Вычислите area. Двигайте указатель с меньшей высотой — так есть шанс найти бо́льшую площадь.
</details>

<details>
<summary>Подсказка 3</summary>
Почему двигаем меньший? Если двигать бо́льший — высота контейнера не увеличится, а ширина уменьшится. Площадь точно не вырастет.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Brute Force | O(n²) | O(1) |
| **Two Pointers** | **O(n)** | **O(1)** |

---

## 10. Rotate Array
**Difficulty:** 🟡 Medium  
**Паттерн:** Array Reversal / Cyclic Replacement

### Problem
Дан массив целых чисел `nums`. Сдвиньте массив вправо на `k` шагов **in-place**.

### Example 1
```
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
Explanation:
  Шаг 1: [7, 1, 2, 3, 4, 5, 6]
  Шаг 2: [6, 7, 1, 2, 3, 4, 5]
  Шаг 3: [5, 6, 7, 1, 2, 3, 4]
```

### Example 2
```
Input: nums = [-1, -100, 3, 99], k = 2
Output: [3, 99, -1, -100]
```

### Example 3
```
Input: nums = [1, 2, 3], k = 4
Output: [3, 1, 2]
Explanation: k > n, поэтому k = k % n = 4 % 3 = 1. Один сдвиг вправо.
```

### Constraints
- `1 <= len(nums) <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

### Hints
<details>
<summary>Подсказка 1</summary>
Если k >= len(nums), k = k % len(nums). Зачем делать лишние полные обороты?
</details>

<details>
<summary>Подсказка 2</summary>
Метод трёх реверсов: 1) Реверс всего массива. 2) Реверс первых k элементов. 3) Реверс оставшихся.
</details>

<details>
<summary>Подсказка 3</summary>
Пример: [1,2,3,4,5,6,7], k=3.
1) [7,6,5,4,3,2,1] — реверс всего
2) [5,6,7,4,3,2,1] — реверс [0:3]
3) [5,6,7,1,2,3,4] — реверс [3:7] ✓
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Extra array | O(n) | O(n) |
| Pop & Insert | O(n*k) | O(1) |
| **Three Reversals** | **O(n)** | **O(1)** |
