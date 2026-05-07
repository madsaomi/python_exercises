# 📘 Trees — Теория

## Бинарное дерево

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Обходы дерева

### DFS (Depth-First Search)

```python
# Inorder (Left → Root → Right) — для BST даёт отсортированный порядок
def inorder(node):
    if not node: return []
    return inorder(node.left) + [node.val] + inorder(node.right)

# Preorder (Root → Left → Right)
def preorder(node):
    if not node: return []
    return [node.val] + preorder(node.left) + preorder(node.right)

# Postorder (Left → Right → Root)
def postorder(node):
    if not node: return []
    return postorder(node.left) + postorder(node.right) + [node.val]
```

### BFS (Breadth-First Search) — по уровням

```python
from collections import deque

def level_order(root):
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

## BST (Binary Search Tree)

- Левое поддерево < корень < правое поддерево
- Inorder обход даёт отсортированную последовательность
- Поиск, вставка, удаление: O(h), где h — высота

## Паттерны
- **Рекурсия** → большинство задач на деревья
- **DFS** → обход в глубину (inorder, preorder, postorder)
- **BFS** → обход по уровням
- **Высота** → max(left_h, right_h) + 1
