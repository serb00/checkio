def index_power(ar: list[int], n: int) -> int:
    # your code here
    return ar[n]**n if len(ar) > n else -1


print("Example:")
print(index_power([1, 2, 3], 2))
