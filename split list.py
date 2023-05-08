from timeit import timeit
from typing import Any, Iterable


def split_list(items: list[Any]) -> Iterable[list[Any]]:
    # your code here
    if len(items) % 2 == 0:
        mid = int(len(items) / 2)
    else:
        mid = int(len(items) / 2) + 1

    return [items[:mid], items[mid:]]


def split_list_opt(items: list[Any]) -> Iterable[list[Any]]:
    mid = (len(items) + 1) // 2
    return [items[:mid], items[mid:]]


print("Example:")
print(list(split_list([1, 2, 3, 4, 5])))
print(list(split_list_opt([1, 2, 3, 4, 5, 6])))

itr = 1000000
list = [1, 2, 3, 4, 5]
for foo in [split_list, split_list_opt]:
    t = timeit(stmt="foo(list)", number=itr, globals=globals())
    print(f'{foo.__name__} took {t:6f} seconds over {itr:,} iterations.')
