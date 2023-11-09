import math


def clean_fibbonacci(n: int):
    return 0.5 * (((1 + math.sqrt(5)) / 2) ** (n + 1) - ((1 - math.sqrt(5)) // 2) ** (n + 1))


# Уберите комментарии если хотите видеть сам ряд фиббоначи
def based_fibbonacci(n: int):
    row = [0, 1, 1]
    if n <= len(row):
        # print("[DEBUG]", row)
        return row[n - 1]
    else:
        while len(row) < n:
            row.append(row[len(row) - 1] + row[len(row) - 2])
        # print("[DEBUG]", row)
        return row[n - 1]


# Unit-tests

for x in range(100):
    clean = clean_fibbonacci(x)
    based = based_fibbonacci(x)
    print("math-method:", clean)
    print("default-method:", based)
    if abs(clean - based) > 0.001:
        break
