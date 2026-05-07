# 🧩 Trees — Задачи

---

## 1. Maximum Depth of Binary Tree
**Difficulty:** 🟢 Easy  
**Паттерн:** DFS (Recursive)

### Problem
Найдите **максимальную глубину** бинарного дерева — количество узлов на самом длинном пути от корня до листа.

### Example 1
```
Input: root = [3, 9, 20, null, null, 15, 7]
Output: 3
Explanation:
        3
       / \
      9  20
         / \
        15   7
  Глубина = 3.
```

### Example 2
```
Input: root = [1, null, 2]
Output: 2
```

### Example 3
```
Input: root = []
Output: 0
```

### Constraints
- `0 <= количество узлов <= 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Рекурсия: depth(node) = 1 + max(depth(left), depth(right)). Базовый случай: node is None → 0.
</details>

<details>
<summary>Подсказка 2</summary>
Итеративно: BFS (уровневый обход), считая количество уровней.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **DFS Recursive** | **O(n)** | **O(h)** h = высота |
| BFS | O(n) | O(w) w = ширина |

---

## 2. Invert Binary Tree
**Difficulty:** 🟢 Easy  
**Паттерн:** DFS / BFS

### Problem
Инвертируйте бинарное дерево (зеркально отразите): каждый левый потомок меняется с правым на всех уровнях.

### Example 1
```
Input:       4              4
           / \    →      / \
          2   7          7   2
         / \ / \        / \ / \
        1  3 6  9      9  6 3  1
Output: [4, 7, 2, 9, 6, 3, 1]
```

### Example 2
```
Input: root = [2, 1, 3]
Output: [2, 3, 1]
```

### Example 3
```
Input: root = []
Output: []
```

### Constraints
- `0 <= количество узлов <= 100`

### Hints
<details>
<summary>Подсказка 1</summary>
Рекурсия: поменяйте left и right, затем рекурсивно инвертируйте оба поддерева.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **DFS Recursive** | **O(n)** | **O(h)** |

---

## 3. Same Tree
**Difficulty:** 🟢 Easy  
**Паттерн:** DFS (Parallel Traversal)

### Problem
Даны два бинарных дерева `p` и `q`. Определите, **структурно идентичны** ли они (одинаковая структура и значения узлов).

### Example 1
```
Input: p = [1, 2, 3], q = [1, 2, 3]
Output: True
```

### Example 2
```
Input: p = [1, 2], q = [1, null, 2]
Output: False
Explanation: Разная структура.
```

### Example 3
```
Input: p = [1, 2, 1], q = [1, 1, 2]
Output: False
Explanation: Одинаковая структура, но разные значения.
```

### Constraints
- `0 <= количество узлов <= 100`

### Hints
<details>
<summary>Подсказка 1</summary>
Рекурсия: оба None → True. Один None → False. Значения разные → False. Иначе: рекурсивно left и right.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **DFS Recursive** | **O(n)** | **O(h)** |

---

## 4. Symmetric Tree
**Difficulty:** 🟢 Easy  
**Паттерн:** DFS (Mirror Check)

### Problem
Определите, является ли бинарное дерево **зеркально симметричным** (симметричным относительно своего центра).

### Example 1
```
Input: root = [1, 2, 2, 3, 4, 4, 3]
Output: True
Explanation:
        1
       / \
      2   2
     / \ / \
    3  4 4  3   ← зеркально!
```

### Example 2
```
Input: root = [1, 2, 2, null, 3, null, 3]
Output: False
```

### Constraints
- `1 <= количество узлов <= 1000`

### Hints
<details>
<summary>Подсказка 1</summary>
Задача: проверить, является ли левое поддерево зеркалом правого. Рекурсия: isMirror(left, right).
</details>

<details>
<summary>Подсказка 2</summary>
isMirror(a, b): оба None → True. Один None → False. a.val != b.val → False. Иначе: isMirror(a.left, b.right) and isMirror(a.right, b.left).
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **DFS Recursive** | **O(n)** | **O(h)** |
| BFS (queue) | O(n) | O(w) |

---

## 5. Binary Tree Level Order Traversal
**Difficulty:** 🟡 Medium  
**Паттерн:** BFS (Queue)

### Problem
Верните обход бинарного дерева **по уровням** (level order). Результат — список списков значений для каждого уровня.

### Example 1
```
Input: root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [9, 20], [15, 7]]
Explanation:
  Уровень 0: [3]
  Уровень 1: [9, 20]
  Уровень 2: [15, 7]
```

### Example 2
```
Input: root = [1]
Output: [[1]]
```

### Example 3
```
Input: root = []
Output: []
```

### Constraints
- `0 <= количество узлов <= 2000`

### Hints
<details>
<summary>Подсказка 1</summary>
BFS с очередью. На каждом уровне: обработать len(queue) узлов, добавить их детей.
</details>

<details>
<summary>Подсказка 2</summary>
Используйте collections.deque для эффективного popleft.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **BFS (Queue)** | **O(n)** | **O(n)** |
| DFS + level param | O(n) | O(n) |

---

## 6. Validate Binary Search Tree
**Difficulty:** 🟡 Medium  
**Паттерн:** DFS with Bounds / Inorder Traversal

### Problem
Определите, является ли бинарное дерево **валидным BST**.

Правила BST:
- Все значения в левом поддереве < значения узла
- Все значения в правом поддереве > значения узла
- Оба поддерева — тоже BST

### Example 1
```
Input: root = [2, 1, 3]
Output: True
```

### Example 2
```
Input: root = [5, 1, 4, null, null, 3, 6]
Output: False
Explanation: Узел 4 в правом поддереве от 5, но 4 < 5.
```

### Example 3
```
Input: root = [5, 4, 6, null, null, 3, 7]
Output: False
Explanation: Узел 3 в правом поддереве от 5, но 3 < 5.
```

### Constraints
- `1 <= количество узлов <= 10^4`

### Hints
<details>
<summary>Подсказка 1</summary>
Передавайте допустимые границы (min_val, max_val): validate(node, low=-inf, high=+inf). Для левого: high=node.val. Для правого: low=node.val.
</details>

<details>
<summary>Подсказка 2</summary>
Альтернатива: inorder обход BST даёт отсортированный массив. Проверьте, что каждый следующий элемент > предыдущего.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **DFS with bounds** | **O(n)** | **O(h)** |
| Inorder + check | O(n) | O(n) |

---

## 7. Lowest Common Ancestor of BST
**Difficulty:** 🟡 Medium  
**Паттерн:** BST Property Exploitation

### Problem
Найдите **наименьшего общего предка** (LCA) двух узлов `p` и `q` в BST.

LCA — самый глубокий узел, который является предком обоих p и q (узел может быть предком самого себя).

### Example 1
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: LCA узлов 2 и 8 — корень 6.
```

### Example 2
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: Узел 2 — предок самого себя и 4.
```

### Constraints
- `2 <= количество узлов <= 10^5`
- Все значения уникальны
- p != q, оба существуют в дереве

### Hints
<details>
<summary>Подсказка 1</summary>
Используйте свойство BST! Если оба p, q < node → LCA слева. Если оба > node → LCA справа. Иначе — текущий node = LCA.
</details>

<details>
<summary>Подсказка 2</summary>
Итеративно: пока node, проверяйте направление. Не нужна рекурсия.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **Iterative (BST property)** | **O(h)** | **O(1)** |
| Recursive | O(h) | O(h) |

---

## 8. Binary Tree Paths
**Difficulty:** 🟢 Easy  
**Паттерн:** DFS + Path Tracking

### Problem
Верните **все пути** от корня до листьев в виде строк формата `"1->2->5"`.

### Example 1
```
Input: root = [1, 2, 3, null, 5]
Output: ["1->2->5", "1->3"]
Explanation:
      1
     / \
    2   3
     \
      5
  Пути: 1→2→5 и 1→3.
```

### Example 2
```
Input: root = [1]
Output: ["1"]
```

### Constraints
- `1 <= количество узлов <= 100`

### Hints
<details>
<summary>Подсказка 1</summary>
DFS: передавайте текущий путь как строку. Лист (нет детей) → добавить путь в результат. Иначе → рекурсия для left и right.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **DFS + string path** | **O(n)** | **O(n × h)** |

---

## 9. Construct Binary Tree from Preorder and Inorder
**Difficulty:** 🟡 Medium  
**Паттерн:** Divide and Conquer + Hash Map

### Problem
Постройте бинарное дерево из массивов **preorder** (корень-левый-правый) и **inorder** (левый-корень-правый) обходов.

Гарантируется, что все значения уникальны.

### Example 1
```
Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
Output: [3, 9, 20, null, null, 15, 7]
Explanation:
      3
     / \
    9  20
       / \
      15   7
```

### Example 2
```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

### Constraints
- `1 <= len(preorder) <= 3000`
- `preorder.length == inorder.length`
- Все значения уникальны

### Hints
<details>
<summary>Подсказка 1</summary>
preorder[0] — корень. Найдите его в inorder: всё слева — левое поддерево, справа — правое.
</details>

<details>
<summary>Подсказка 2</summary>
Используйте hash map для быстрого поиска индекса в inorder (O(1) вместо O(n)).
</details>

<details>
<summary>Подсказка 3</summary>
Рекурсия: build(pre_start, pre_end, in_start, in_end). Количество элементов в левом поддереве = root_index_in_inorder - in_start.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| Recursive + linear search | O(n²) | O(n) |
| **Recursive + hash map** | **O(n)** | **O(n)** |

---

## 10. Serialize and Deserialize Binary Tree
**Difficulty:** 🔴 Hard  
**Паттерн:** BFS / DFS + String Encoding

### Problem
Реализуйте **сериализацию** бинарного дерева в строку и **десериализацию** обратно в дерево.

Формат на ваш выбор — главное, чтобы decode(encode(root)) воссоздавало исходное дерево.

### Example 1
```
Input: root = [1, 2, 3, null, null, 4, 5]
Serialized: "1,2,null,null,3,4,null,null,5,null,null"
Output: [1, 2, 3, null, null, 4, 5]
```

### Example 2
```
Input: root = []
Serialized: "null"
Output: []
```

### Constraints
- `0 <= количество узлов <= 10^4`
- `-1000 <= Node.val <= 1000`

### Hints
<details>
<summary>Подсказка 1</summary>
Preorder DFS: serialize — записывайте значение, "null" для пустых узлов. Deserialize — читайте токены и стройте дерево рекурсивно.
</details>

<details>
<summary>Подсказка 2</summary>
BFS: serialize уровень за уровнем (включая null). Deserialize — обратный BFS с очередью.
</details>

### Approach
| Подход | Время | Память |
|--------|-------|--------|
| **DFS Preorder** | **O(n)** | **O(n)** |
| BFS Level-order | O(n) | O(n) |
