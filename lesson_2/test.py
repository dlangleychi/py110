def even_values(lst):
    evens = []

    for value in lst:
        if value % 2 == 0:
            evens.append(value)
        lst.pop(0)

    return evens

print(even_values([1, 3, 4, 2, 4, 6, 5, 7, 9, 10, 12]))

[return True for _ in range(10)]

[print(i) if (i < 4) else break for i in range(10)]