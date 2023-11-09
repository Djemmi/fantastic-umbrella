def getFactorial(num: int) -> int:
    result = 1
    for x in range(1, num + 1):
        result *= x
    return result


# Unit-tests
for x in range(10):
    print(getFactorial(x))
