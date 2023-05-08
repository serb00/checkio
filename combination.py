# n = input()
# a = list(map(int, input().split()))
# b = int(input())

a = [-9, -7, -6, -1, -1, 3]
b = 2


def search_pair(a, b):
    search = []
    for v in a:
        search.append(b - v)
    print(search)
    for i in range(0, len(a)-1):
        if a[i] in search[:i] or a[i] in search[i+1:]:
            return f'{a[i]} {a[search.index(a[i])]}'
    return 'None'


def search_pair_opt(a, b):
    left = 0
    right = len(a) - 1

    while left < right:
        if a[left] + a[right] == b:
            return f'{a[left]} {a[right]}'
        elif a[left] + a[right] > b:
            right -= 1
        else:
            left += 1
    return 'None'


print(search_pair_opt(a, b))
