numbers = []


def askForNumber():
    io = int(input())
    if io == 0:
        return
    numbers.append(io)
    askForNumber()


askForNumber()
print("Введено чисел:", len(numbers))

print("Что сделать?\n1. Найти сумму введённых чисел.\n2. Найти произведение введённых чисел.\n3. Найти среднее "
      "значение введённых чисел.\n4. Найти максимальное из введённых чисел.\n5. Найти минимальное из введённых "
      "чисел.\n6. Определить количество чётных и нечётных эллементов.\n")

operation = int(input())

match operation:
    case 1:
        result = 0
        for x in numbers:
            result += x
        print(result)
    case 2:
        result = 0
        for x in numbers:
            result *= x
        print(result)
    case 3:
        result = 0
        for x in numbers:
            result += x
        print(result // len(numbers))
    case 4:
        print(max(numbers))
    case 5:
        print(min(numbers))
    case 6:
        chet = 0
        nech = 0
        for x in numbers:
            if x % 2 == 0:
                chet += 1
            else:
                nech += 1
        print('Чётных:', chet, "Нечётных:", nech)
    case _:
        print("Увы, но такой операции не существует")
        