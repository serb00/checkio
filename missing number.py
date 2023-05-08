from datetime import datetime
from itertools import pairwise


def missing_number(items: list[int]) -> int:
    # your code here
    items.sort()
    step = int((items[-1] - items[0])/len(items))
    for i in range(len(items)):
        if items[i] + step != items[i+1]:
            return items[i] + step
    return -1


def missing_number_opt(i: list[int]) -> int:
    i.sort()
    h = min(i[1] - i[0], i[-1] - i[-2])
    for a, b in pairwise(i):
        if b-a != h:
            return a+h


print("Example:")


iter = 10000000

start_time = datetime.now()


for i in range(iter):
    missing_number([1, 4, 2, 5])

print(f'{iter} iterations with for loop took'
      f' { datetime.now() - start_time } seconds')


start_time = datetime.now()


for i in range(iter):
    missing_number_opt([1, 4, 2, 5])

print(f'{iter} iterations with find function took'
      f' { datetime.now() - start_time } seconds')
