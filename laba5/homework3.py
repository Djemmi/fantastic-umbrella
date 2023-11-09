def askForInput(array=[]):
    data = array
    i = input()
    for char in i:
        if char.isnumeric():
            data.append(int(char))
    print(sum(data))
    askForInput(data)


askForInput()