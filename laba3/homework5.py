def getInput() -> str:
    return input()


def testInput(line: str) -> bool:
    return line.isnumeric()


def strToInt(line: str) -> int:
    return int(line)


def printInt(num: int) -> None:
    print(num)


io = getInput()
if testInput(io):
    io = strToInt(io)
    printInt(io)

