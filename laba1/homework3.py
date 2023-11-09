summa = [1, 2, 3, 4, 5]

num_to_add = int(input("Введите дополнительное число для добавления к сумме: "))
while num_to_add != 0:
    summa.append(num_to_add)
    print("Среднее значение этих 5 чисел равно {:.5f}".format(sum(summa) / len(summa)))
    num_to_add = int(input("Введите дополнительное число для добавления к сумме: "))
