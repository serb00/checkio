from datetime import date


def days_diff(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    # your code here
    return abs((date(*a)-date(*b)).days)


print("Example:")
print(days_diff((1982, 4, 19), (1982, 4, 22)))
