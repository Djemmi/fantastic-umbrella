def move(n, source, target, auxiliary):
    if n > 0:
        # Перемещаем башню из (n-1) диска на промежуточный стержень
        move(n - 1, source, auxiliary, target)
        # Перемещаем оставшийся диск на целевой стержень
        print("Перемещаю диск номер %0i со стержня %0s на стержень %0s" % (n, source, target))
        # Перемещаем башню из (n-1) диска с промежуточного на целевой стержень
        move(n - 1, auxiliary, target, source)


# Пример использования
move(3, 'A', 'C', 'B')
