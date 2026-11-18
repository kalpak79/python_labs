from collections import deque
from typing import Any


def stack_push(st: list, item: Any) -> None:
    """Добавить элемент на вершину стека."""
    st.append(item)


def stack_pop(st: list) -> Any:
    """Снять верхний элемент стека и вернуть его."""
    if not st:
        raise IndexError("Невозможно выполнить pop: стек пуст")
    return st.pop()


def stack_peek(st: list) -> Any | None:
    """Вернуть верхний элемент стека без удаления (None, если пуст)."""
    if not st:
        return None
    return st[-1]


def stack_is_empty(st: list) -> bool:
    """Проверить, пуст ли стек."""
    return len(st) == 0


def queue_enqueue(q: deque, item: Any) -> None:
    """Добавить элемент в конец очереди."""
    q.append(item)


def queue_dequeue(q: deque) -> Any:
    """Взять элемент из начала очереди и вернуть его."""
    if not q:
        raise IndexError("Невозможно выполнить dequeue: очередь пуста")
    return q.popleft()


def queue_peek(q: deque) -> Any | None:
    """Вернуть первый элемент очереди без удаления (None, если пуста)."""
    if not q:
        return None
    return q[0]


def queue_is_empty(q: deque) -> bool:
    """Проверить, пуста ли очередь."""
    return len(q) == 0


# --- Задачи на стек ---

def is_balanced(s: str) -> bool:
    """Проверка правильности скобочной последовательности (), [], {}."""
    st = []
    pairs = {")": "(", "]": "[", "}": "{"}
    opening = set(pairs.values())

    for ch in s:
        if ch in opening:
            stack_push(st, ch)
        elif ch in pairs:
            if stack_is_empty(st) or stack_pop(st) != pairs[ch]:
                return False

    return stack_is_empty(st)


def rpn(expr: str) -> float:
    """Калькулятор обратной польской записи (RPN) на стеке."""
    st = []
    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }

    for token in expr.split():
        if token in operators:
            if len(st) < 2:
                raise ValueError("Некорректное выражение RPN: недостаточно операндов")
            b = stack_pop(st)
            a = stack_pop(st)
            stack_push(st, operators[token](a, b))
        else:
            stack_push(st, float(token))

    if len(st) != 1:
        raise ValueError("Некорректное выражение RPN: лишние операнды")
    return float(stack_pop(st))

def main():
    st = []
    stack_push(st, 10)
    stack_push(st, 20)
    stack_push(st, 30)
    print("Стек:", st)
    print("Вершина (peek):", stack_peek(st))
    print("Извлекли (pop):", stack_pop(st))
    print("Стек после pop:", st)
    print("Пустой ли стек:", stack_is_empty(st))

    q = deque()
    queue_enqueue(q, "Задача 1")
    queue_enqueue(q, "Задача 2")
    queue_enqueue(q, "Задача 3")
    print("Первый в очереди (peek):", queue_peek(q))
    print("Выполнили (dequeue):", queue_dequeue(q))
    print("Очередь после dequeue:", list(q))

    print("([]{}):", is_balanced("([]{})"))
    print("([)]:", is_balanced("([)]"))
    print("RPN '3 4 + 2 *':", rpn("3 4 + 2 *"))

if __name__ == "__main__":
    main()