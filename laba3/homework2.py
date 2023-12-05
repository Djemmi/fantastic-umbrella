def getAns1(x):
    return x != 3 or x != 5


def getAns2(x):
    return x == 3 and x == 5


for x in range(1, 10):
    print("Always true:", getAns1(x))
    print("Always false:", getAns2(x))
