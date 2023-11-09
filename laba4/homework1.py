def solution():
    a = input("Введите значение 1: ")
    b = input("Введите значение 2: ")

    try:
        return int(a) + int(b)
    except ValueError:
        return str(a) + str(b)


print(solution())
