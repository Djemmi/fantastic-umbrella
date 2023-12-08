m = int(input("Кол-во кубиков в куче: "))
n = int(input("Кол-во играющих детей: "))

amount_to_take = 1
looser = 1

while amount_to_take <= m:

    print(looser, "took", amount_to_take)
    if looser < n:
        looser += 1
    else:
        looser = 1
    amount_to_take *= 2
print("Проиграл ребенок номер %0i" % looser)
