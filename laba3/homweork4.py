def solution():
    io = int(input("Enter integer "))
    if io >= 0:
        positive()
        return
    negative()


def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


solution()