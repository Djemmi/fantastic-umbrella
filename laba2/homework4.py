def forDiv(num):
    for x in range(2, num // 2):
        if num % x == 0:
            return x
    return num


def whileDiv(num):
    div = 2
    while num % div != 0:
        div += 1
    return div


num = int(input("Enter number "))
print(forDiv(num))
print(whileDiv(num))
