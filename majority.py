from timeit import timeit


def is_majority(items: list[bool]) -> bool:
    # your code here
    return items.count(True) > items.count(False)


def is_majority_opt(items: list) -> bool:
    return sum(items) > len(items) / 2


def is_majority_mixed(items: list[bool]) -> bool:
    # your code here
    return items.count(True) > len(items) / 2


def is_majority_mixed2(items: list[bool]) -> bool:
    # your code here
    return sum(items) > items.count(False)


print("Example:")
print(is_majority([True, True, False, True, False]))

itr = 10_000_000
items = [True, True, False, True, False]
for foo in [is_majority, is_majority_opt,
            is_majority_mixed, is_majority_mixed2]:
    t = timeit(stmt="foo(items)", number=itr, globals=globals())
    print(f"{foo.__name__} run in {t:.6f} sec with {itr:,} iters.")
