def getInput():
    return input()


def testInput(line):
    return line.isnumeric()


def strToInt(line):
    return int(line)


def printInt(num):
    print(num)


io = getInput()
if testInput(io):
    io = strToInt(io)
    printInt(io)

