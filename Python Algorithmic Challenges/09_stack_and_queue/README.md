# 📘 Stack & Queue — Теория

## Стек (Stack) — LIFO

Последний вошёл — первый вышел.

```python
stack = []
stack.append(1)   # push
stack.append(2)
stack.pop()       # 2 (pop)
stack[-1]         # peek — верхний элемент
len(stack) == 0   # is_empty
```

**Сложность:** push O(1), pop O(1), peek O(1)

## Очередь (Queue) — FIFO

Первый вошёл — первый вышел.

```python
from collections import deque

queue = deque()
queue.append(1)      # enqueue (в конец)
queue.append(2)
queue.popleft()      # dequeue (из начала) — O(1)
queue[0]             # peek
```

## Приоритетная очередь (Min-Heap)

```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappop(heap)     # 1 — минимальный
```

## Типичные задачи

- **Стек** → валидация скобок, обратная польская нотация, моноторный стек
- **Очередь** → BFS, скользящее окно максимумов
- **Monotonic Stack** → следующий больший/меньший элемент

## Monotonic Stack

```python
# Следующий больший элемент
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            result[stack.pop()] = num
        stack.append(i)
    return result
```
