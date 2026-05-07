# 🧩 Trees — Задачи

---

## 1. Maximum Depth of Binary Tree
**Difficulty:** 🟢 Easy

### Problem
Найдите **максимальную глубину** бинарного дерева (число узлов на самом длинном пути от корня до листа).

### Example 1
```
Input: root = [3, 9, 20, null, null, 15, 7]
Output: 3
```

### Constraints
- `0 <= количество узлов <= 10^4`

---

## 2. Invert Binary Tree
**Difficulty:** 🟢 Easy

### Problem
Инвертируйте бинарное дерево (зеркально отразите).

### Example 1
```
Input: root = [4, 2, 7, 1, 3, 6, 9]
Output: [4, 7, 2, 9, 6, 3, 1]
```

### Constraints
- `0 <= количество узлов <= 100`

---

## 3. Same Tree
**Difficulty:** 🟢 Easy

### Problem
Определите, **одинаковы** ли два бинарных дерева (структура + значения).

### Example 1
```
Input: p = [1, 2, 3], q = [1, 2, 3]
Output: True
```

### Constraints
- `0 <= количество узлов <= 100`

---

## 4. Symmetric Tree
**Difficulty:** 🟢 Easy

### Problem
Определите, является ли дерево **симметричным** (зеркальным относительно центра).

### Example 1
```
Input: root = [1, 2, 2, 3, 4, 4, 3]
Output: True
```

### Constraints
- `1 <= количество узлов <= 1000`

---

## 5. Binary Tree Level Order Traversal
**Difficulty:** 🟡 Medium

### Problem
Верните обход дерева **по уровням** (BFS).

### Example 1
```
Input: root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [9, 20], [15, 7]]
```

### Constraints
- `0 <= количество узлов <= 2000`

---

## 6. Validate Binary Search Tree
**Difficulty:** 🟡 Medium

### Problem
Определите, является ли дерево **валидным BST**.

### Example 1
```
Input: root = [5, 1, 4, null, null, 3, 6]
Output: False
Explanation: Корень 5, но правый потомок 4 < 5
```

### Constraints
- `1 <= количество узлов <= 10^4`

---

## 7. Lowest Common Ancestor of BST
**Difficulty:** 🟡 Medium

### Problem
Найдите **наименьшего общего предка** двух узлов в BST.

### Example 1
```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
```

### Constraints
- `2 <= количество узлов <= 10^5`
- Все значения уникальны

---

## 8. Binary Tree Paths
**Difficulty:** 🟢 Easy

### Problem
Верните **все пути** от корня до листьев в виде строк.

### Example 1
```
Input: root = [1, 2, 3, null, 5]
Output: ["1->2->5", "1->3"]
```

### Constraints
- `1 <= количество узлов <= 100`

---

## 9. Construct Binary Tree from Preorder and Inorder
**Difficulty:** 🟡 Medium

### Problem
Постройте дерево из массивов **preorder** и **inorder** обходов.

### Example 1
```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

### Constraints
- `1 <= len(preorder) <= 3000`

---

## 10. Serialize and Deserialize Binary Tree
**Difficulty:** 🔴 Hard

### Problem
Реализуйте **сериализацию** дерева в строку и **десериализацию** обратно.

### Example 1
```
Input: root = [1, 2, 3, null, null, 4, 5]
Serialized: "1,2,null,null,3,4,null,null,5,null,null"
Output: [1, 2, 3, null, null, 4, 5]
```

### Constraints
- `0 <= количество узлов <= 10^4`
