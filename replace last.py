from timeit import timeit
from typing import Iterable


def replace_last(line: list) -> Iterable:
    # your code here
    res = []
    if len(line) > 0:
        res.append(line[-1])
        for i in line[:-1]:
            res.append(i)
    return res


def replace_last_opt(items):
    if items:
        yield items[-1]
        for i in range(len(items)-1):
            yield items[i]


# Change items IN-PLACE.
def replace_last_in_place(items: list) -> list:
    if items:
        items.insert(0, items.pop())
    return items


# Slices
def replace_last_slices(items: list) -> list:
    return items[-1:] + items[:-1]


print("Example:")
print(list(replace_last([2, 3, 4, 1])))

itr = 1000000
items = [2, 3, 4, 1]
for foo in [replace_last,
            replace_last_opt,
            replace_last_in_place,
            replace_last_slices]:
    t = timeit(stmt="foo(items)", number=itr, globals=globals())
    print(f"{foo.__name__} run in {t:.6f} sec with {itr:,} iters.")
