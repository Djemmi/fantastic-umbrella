numbers = []


def Solution() -> None:
    i = input("Введите число (0 для прерывания): ")
    if i == 0:
        return
    try:
        numbers.append(int(i))
        print("Максимальное значение:", max(numbers), "\nМинимальное значение:", min(numbers))
    except ValueError:
        print("Invalid input")
    Solution()


Solution()
