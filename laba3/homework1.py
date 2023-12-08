# Условие 1
def getAns1(x):
    return len(str(x)) == 3 and str(x)[-1] == "0" and x > 0


# Условие 2
def getAns2(x):
    return x % 2 != 0 and (x % 3 == 0 or x % 5 == 0)


# Условие 3
def getAns3(x):
    return 2 <= x <= 6


# Условие 4
def getAns4(x):
    return len(str(x)) == 3 and str(x)[0] == str(x)[1] == str(x)[2]


i = int(input("Enter integer x: "))
print(getAns(i))
print(getAns1(i))
print(getAns2(i))
print(getAns3(i))
print(getAns4(i))
