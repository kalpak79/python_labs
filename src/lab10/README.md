# ЛР10 — Структуры данных: Stack, Queue, Linked List и бенчмарки

## 1. Краткая теория

### Стек (Stack)
* **Принцип работы:** LIFO (*Last In, First Out* — «последним пришел, первым вышел»).
* **Реализация:** на базе стандартного динамического массива `list`. Вершиной стека является последний элемент списка (`st[-1]`).
* **Сложность операций:**
  * Добавление на вершину (`stack_push` / `append`) — \(O(1)\) амортизированно.
  * Извлечение с вершины (`stack_pop` / `pop`) — \(O(1)\).
  * Просмотр вершины (`stack_peek`) и проверка на пустоту (`stack_is_empty`) — \(O(1)\).

### Очередь (Queue)
* **Принцип работы:** FIFO (*First In, First Out* — «первым пришел, первым вышел»).
* **Реализация:** на базе двусторонней очереди `collections.deque` (реализована как двусвязный список блоков).
* **Сложность операций:**
  * Добавление в конец (`queue_enqueue` / `append`) — \(O(1)\).
  * Извлечение из начала (`queue_dequeue` / `popleft`) — \(O(1)\) (в отличие от `list.pop(0)`, который работает за \(O(n)\)).
  * Просмотр первого элемента (`queue_peek`) и проверка на пустоту (`queue_is_empty`) — \(O(1)\).

### Связный список (Linked List)
* **Принцип работы:** линейная структура данных, состоящая из узлов (`Node`), каждый из которых хранит значение и ссылку на следующий элемент. Узлы располагаются в памяти не последовательно, а связываются через указатели.
* **Сложность операций:**
  * Вставка в начало (`ll_prepend`) — \(O(1)\).
  * Вставка в конец (`ll_append`), вставка по индексу (`ll_insert`), удаление по значению (`ll_remove`), подсчет длины (`ll_length`) — \(O(n)\), так как требуется последовательный проход от головы списка (`head`).
  * Разворот списка на месте (`ll_reverse`) — \(O(n)\) по времени и \(O(1)\) по дополнительной памяти.

---

## 2. Реализованные функции

### structures.py

``` python
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
```

### linked_list.py

``` python
from typing import Any, Iterable


class Node:
    """Узел односвязного списка (только конструктор)."""
    def __init__(self, value: Any, next: "Node | None" = None):
        self.value = value
        self.next = next


def ll_from_list(values: Iterable[Any]) -> Node | None:
    """Собрать односвязный список из итерируемого объекта."""
    head = None
    tail = None
    for val in values:
        new_node = Node(val)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head


def ll_to_list(head: Node | None) -> list:
    """Преобразовать односвязный список в обычный list."""
    result = []
    cur = head
    while cur is not None:
        result.append(cur.value)
        cur = cur.next
    return result


def ll_length(head: Node | None) -> int:
    """Вычислить количество узлов в списке."""
    count = 0
    cur = head
    while cur is not None:
        count += 1
        cur = cur.next
    return count


def ll_prepend(head: Node | None, value: Any) -> Node:
    """Добавить элемент в начало списка за O(1). Возвращает новую голову."""
    return Node(value, head)


def ll_append(head: Node | None, value: Any) -> Node:
    """Добавить элемент в конец списка за O(n). Возвращает голову."""
    new_node = Node(value)
    if head is None:
        return new_node
    cur = head
    while cur.next is not None:
        cur = cur.next
    cur.next = new_node
    return head


def ll_insert(head: Node | None, idx: int, value: Any) -> Node:
    """Вставить элемент по индексу idx в диапазоне [0, len]."""
    if idx < 0:
        raise IndexError("Индекс не может быть отрицательным")
    if idx == 0:
        return ll_prepend(head, value)

    cur = head
    pos = 0
    while cur is not None and pos < idx - 1:
        cur = cur.next
        pos += 1

    if cur is None:
        raise IndexError("Индекс вне диапазона списка")

    cur.next = Node(value, cur.next)
    return head


def ll_remove(head: Node | None, value: Any) -> Node | None:
    """Удалить первое вхождение значения value. Выбрасывает ValueError, если не найдено."""
    if head is None:
        raise ValueError(f"Значение {value!r} не найдено в пустом списке")

    if head.value == value:
        return head.next

    cur = head
    while cur.next is not None:
        if cur.next.value == value:
            cur.next = cur.next.next
            return head
        cur = cur.next

    raise ValueError(f"Значение {value!r} не найдено в списке")


def ll_reverse(head: Node | None) -> Node | None:
    """Развернуть список на месте итеративно тремя указателями."""
    prev = None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def ll_repr(head: Node | None) -> str:
    """Строковое представление списка: [1] -> [2] -> None."""
    if head is None:
        return "None"
    parts = []
    cur = head
    while cur is not None:
        parts.append(f"[{cur.value}]")
        cur = cur.next
    parts.append("None")
    return " -> ".join(parts)


def ll_middle(head: Node | None) -> Node | None:
    """Найти средний узел за один проход (метод двух указателей)."""
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


def ll_has_cycle(head: Node | None) -> bool:
    """Проверить наличие цикла алгоритмом Флойда (черепаха и заяц)."""
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


class DoublyNode:
    """Узел двусвязного списка (только конструктор)."""
    def __init__(self, value: Any, prev: "DoublyNode | None" = None, next: "DoublyNode | None" = None):
        self.value = value
        self.prev = prev
        self.next = next


def dll_from_list(values: Iterable[Any]) -> DoublyNode | None:
    """Собрать двусвязный список из обычного списка."""
    head = None
    tail = None
    for val in values:
        new_node = DoublyNode(val, prev=tail)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head


def dll_append(head: DoublyNode | None, value: Any) -> DoublyNode:
    """Добавить элемент в конец двусвязного списка."""
    if head is None:
        return DoublyNode(value)
    cur = head
    while cur.next is not None:
        cur = cur.next
    cur.next = DoublyNode(value, prev=cur)
    return head


def dll_repr(head: DoublyNode | None) -> str:
    """Строковое представление двусвязного списка."""
    if head is None:
        return "None"
    parts = []
    cur = head
    while cur is not None:
        parts.append(f"[{cur.value}]")
        cur = cur.next
    return "None <- " + " <-> ".join(parts) + " -> None"

```

## 3.Примеры использования

``` python
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
```
![](../../images/lab10/img02.png)

``` python
head = ll_from_list()
print("Исходный список:", ll_repr(head))
print("Длина:", ll_length(head))

head = ll_prepend(head, 5)
head = ll_append(head, 40)
head = ll_insert(head, 2, 15)
print("После вставки 5, 40 и 15:", ll_repr(head))

head = ll_remove(head, 15)
print("После удаления 15:", ll_repr(head))

mid = ll_middle(head)
print("Средний элемент:", mid.value)
print("Есть ли цикл:", ll_has_cycle(head))

print("ДО разворота:   ", ll_repr(head))
head = ll_reverse(head)
print("ПОСЛЕ разворота:", ll_repr(head))

dhead = dll_from_list(["A", "B", "C"])
dhead = dll_append(dhead, "D")
print("Двусвязный список:", dll_repr(dhead))
```
![](../../images/lab10/img03.png)

## 4. Результаты бенчмарков

![](../../images/lab10/img01.png)

### bench.csv
```
operation,n,list_sec,fast_struct_sec,speedup
queue_dequeue,10000,0.08026539999991655,0.0005441999528557062,147.49247878233243
queue_dequeue,100000,13.067289600148797,0.005895599955692887,2216.4478082558517
prepend,10000,0.02111859992146492,0.004755599889904261,4.440785686427896
prepend,100000,2.215496600139886,0.019488999852910638,113.67933792708233
```

### Выводы по производительности

**Почему `list.pop(0)` и `list.insert(0, x)` работают медленно?**
Стандартный `list` в Python устроен как непрерывный массив указателей в памяти. Когда мы удаляем нулевой элемент через `pop(0)` или вставляем новый элемент в начало через `insert(0, x)`, интерпретатор вынужден физически сдвинуть в памяти все остальные $n - 1$ элементов на одну позицию влево или вправо. Таким образом, одна операция занимает $O(n)$ времени, а повторение её $n$ раз приводит к квадратичной сложности $O(n^2)$: при увеличении объема данных в 10 раз время выполнения возрастает примерно в 100 раз.

**Почему `deque.popleft()` и `ll_prepend` работают быстро и не замедляются с ростом $n$?**
Операция `ll_prepend` просто создает новый узел `Node` в свободной области памяти и записывает в его поле `next` ссылку на текущую голову списка. Ей не нужно перемещать существующие узлы или знать длину списка, поэтому время одной вставки строго константно — $O(1)$, а $n$ вставок выполняются за линейное время $O(n)$. Аналогично устроена двусторонняя очередь `collections.deque`: она хранит ссылки на крайние блоки элементов, поэтому удаление слева (`popleft`) сводится к сдвигу внутреннего индекса за $O(1)$ без перезаписи всего массива.