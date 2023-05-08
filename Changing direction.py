def changing_direction(e: list) -> int:
    count = dir2 = 0

    for a, b in zip(e, e[1:]):
        dir = a - b
        if dir:
            if dir * dir2 < 0:
                count += 1
        dir2 = dir
        print(a, ' ', b, ' ', dir, ' ', dir2)
    return count


print("Example:")
print(changing_direction([1, 1, 2, 3, 2, 5]))
