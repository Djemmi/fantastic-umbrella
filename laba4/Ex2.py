def Parity():
    sf = 1
    while bool(sf):
        s = input('Введите число ')
        try:
            sf = int(s)
            f = sf % 2
            if not bool(f):
                print('четное')
            else:
                print('не четное')
        except ValueError:
            print("Неверный тип данных (Value Error)")


Parity()
