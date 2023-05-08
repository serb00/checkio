n = input()
a = list(map(int, input().split()))
k = int(input())

res = []
current_sum = sum(a[0:k])
res.append(str(current_sum/k))

for i in range(0, len(a) - k):
    current_sum -= a[i]
    current_sum += a[i+k]
    res.append(str(current_sum/k))

print(' '.join(res))
