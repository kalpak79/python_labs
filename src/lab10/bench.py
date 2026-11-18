import csv
import os
import timeit
from collections import deque
from src.lab10.linked_list import ll_prepend
from src.lab04.io_txt_csv import write_csv


def bench_queue(n: int) -> tuple[float, float]:
    """Сравнение извлечения из начала: list.pop(0) против deque.popleft()."""
    lst = list(range(n))
    dq = deque(range(n))

    t_list = timeit.timeit(lambda: lst.pop(0), number=n)
    t_deque = timeit.timeit(lambda: dq.popleft(), number=n)
    return t_list, t_deque


def bench_prepend(n: int) -> tuple[float, float]:
    """Сравнение вставки в начало: list.insert(0, x) против ll_prepend(head, x)."""
    lst = []
    t_list = timeit.timeit(lambda: lst.insert(0, 1), number=n)

    head = None

    def step():
        nonlocal head
        head = ll_prepend(head, 1)

    t_ll = timeit.timeit(step, number=n)
    return t_list, t_ll


def run_benchmarks() -> None:
    sizes = [10_000, 100_000]
    results = []

    print(f"{'Операция':<28} | {'n':<8} | {'list (с)':<12} | {'deque/ll (с)':<14} | {'Ускорение':<10}")
    print("-" * 82)

    for n in sizes:
        t_list_q, t_dq = bench_queue(n)
        ratio_q = t_list_q / t_dq if t_dq > 0 else 0
        print(f"{'Очередь (popleft vs pop(0))':<28} | {n:<8} | {t_list_q:<12.6f} | {t_dq:<14.6f} | {ratio_q:<8.1f}x")
        results.append(["queue_dequeue", n, t_list_q, t_dq, ratio_q])

    for n in sizes:
        t_list_p, t_ll = bench_prepend(n)
        ratio_p = t_list_p / t_ll if t_ll > 0 else 0
        print(f"{'Вставка в начало (prepend)':<28} | {n:<8} | {t_list_p:<12.6f} | {t_ll:<14.6f} | {ratio_p:<8.1f}x")
        results.append(["prepend", n, t_list_p, t_ll, ratio_p])

    out_path = "data/lab10/bench.csv"
    write_csv(results, out_path, header=["operation", "n", "list_sec", "fast_struct_sec", "speedup"])
    print(f"\nРезультаты сохранены в {out_path}")


if __name__ == "__main__":
    run_benchmarks()