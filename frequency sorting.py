from collections import Counter
from collections.abc import Iterable
from timeit import timeit


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    # replace this for solution
    return sorted(numbers, key=lambda i: (-numbers.count(i), i))


def frequency_sorting_opt(numbers: list[int]) -> Iterable[int]:
    # replace this for solution
    cnt = Counter(numbers)
    return sorted(numbers, key=lambda i: (-cnt[i], i))


def frequency_sorting2(numbers: list[int]) -> Iterable[int]:
    # replace this for solution
    cnt = Counter(numbers)
    return sorted(numbers, key=lambda i: (-cnt[i], numbers.index(i)))


print("Example:")


print(frequency_sorting([2, 1, 3, 1, 2]))
print(frequency_sorting_opt([2, 1, 3, 1, 2]))

for f in [frequency_sorting, frequency_sorting_opt]:
    t = timeit(number=10000000, globals=globals())
    print(f"{f.__name__} took: {t:.6f}")
