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

def main():
    head = ll_from_list([1, 2, 3])
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

if __name__ == "__main__":
    main()