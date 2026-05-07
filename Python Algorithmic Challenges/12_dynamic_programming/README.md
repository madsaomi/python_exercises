# 📘 Dynamic Programming — Теория

## Что такое DP?

**Динамическое программирование** — метод решения задач путём разбиения на подзадачи и запоминания их решений.

## Два подхода

### Top-Down (Мемоизация)
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)
```

### Bottom-Up (Табуляция)
```python
def fib(n):
    if n < 2: return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

## Оптимизация памяти
```python
def fib(n):
    if n < 2: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

## Как распознать DP-задачу?

1. **Оптимальная подструктура** — оптимальное решение содержит оптимальные подрешения
2. **Перекрывающиеся подзадачи** — одни и те же подзадачи решаются многократно

## Типичные категории

| Тип | Примеры |
|-----|---------|
| 1D DP | Fibonacci, Climbing Stairs |
| 2D DP | Unique Paths, LCS, Edit Distance |
| Knapsack | 0/1 Knapsack, Coin Change |
| String DP | Palindrome, Edit Distance |
| Tree DP | Maximum Path Sum |

## Шаблон решения

1. **Определить состояние** — что описывает подзадачу?
2. **Определить переход** — как связаны подзадачи?
3. **Определить базовые случаи** — начальные значения
4. **Определить порядок вычисления** — снизу вверх
5. **Оптимизировать память** — если зависим только от предыдущих состояний
