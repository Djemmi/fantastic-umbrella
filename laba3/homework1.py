def getAns(x: int) -> bool:
    return len(str(x)) == 3 and str(x).find("0") == 2 and x % 2 != 0 and (x % 3 == 0 or x % 5 == 0) and 2 <= x <= 6 and \
        str(x)[0] == str(x)[1] == str(x)[2]


def getAns1(x: int) -> bool:
    return len(str(x)) == 3 and str(x)[-1] == "0" and x > 0


def getAns2(x: int) -> bool:
    return x % 2 != 0 and (x % 3 == 0 or x % 5 == 0)


def getAns3(x: int) -> bool:
    return 2 <= x <= 6


def getAns4(x: int) -> bool:
    return len(str(x)) == 3 and str(x)[0] == str(x)[1] == str(x)[2]


i = int(input("Enter integer x: "))
print(getAns(i))
print(getAns1(i))
print(getAns2(i))
print(getAns3(i))
print(getAns4(i))
