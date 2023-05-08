from collections.abc import Iterable
from timeit import timeit


def remove_all_after(items: list[int], border: int) -> Iterable[int]:
    # your code here
    ind = items.index(border) + 1 if items.count(border) > 0 else None
    return items[:ind]


def remove_all_after_opt(items: list, border: int) -> Iterable:
    for item in items:
        yield item
        if item == border:
            return


print("Example:")

itr = 1_000_000
lst = [1, 2, 3, 4, 5]
brd = 3
for foo in [remove_all_after, remove_all_after_opt]:
    t = timeit(stmt="foo(lst, brd)", number=itr, globals=globals())
    print(f"{foo.__name__} executed {itr:,} iterations in {t:.6f} seconds")
