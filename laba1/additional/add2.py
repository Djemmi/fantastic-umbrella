nums = []


def solution() -> None:
    try:
        add = int(input("Ender number (0 to exit): "))
        if add == 0:
            return
        nums.append(add)
        print("Max: " + str(max(nums)))
        print("Min: " + str(min(nums)))
        solution()
    except ValueError:
        print("Invalid value!")
        solution()


solution()