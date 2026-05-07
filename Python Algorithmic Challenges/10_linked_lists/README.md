# 📘 Linked Lists — Теория

## Структура узла

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Операции

| Операция | Сложность |
|----------|-----------|
| Доступ по индексу | O(n) |
| Вставка в начало | O(1) |
| Вставка в конец | O(n) |
| Удаление по значению | O(n) |
| Поиск | O(n) |

## Основные подходы

### Dummy Node
```python
dummy = ListNode(0)
dummy.next = head
# ... модификации ...
return dummy.next
```

### Two Pointers (Fast & Slow)
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow — на середине
```

### Реверс списка
```python
def reverse(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
```

## Паттерны
- **Dummy node** → упрощает граничные случаи
- **Fast/Slow** → обнаружение цикла, середина
- **Реверс** → итеративный или рекурсивный
- **Merge** → объединение отсортированных
