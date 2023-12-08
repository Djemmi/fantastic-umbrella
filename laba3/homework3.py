"""
спасибо дяде минералке за то что помог с десмосом <3
"""

x = int(input("Введите х: "))
y = int(input("Введите y: "))


# Функция 1
def func1(x, y):
    return ((x < 3 and y < 4) and x < -y) or (x > 3 and y > 4)


# Функция 2
def func2(x, y):
    return (x ** 2 + y ** 2 > 9) and (-3 < x < 3) and (-3 < y < 3)


# Функция 3
def func3(x, y):
    return ((x - 5) ** 2 + (y - 5) ** 2 > 25) and (5 > x > 0) and (5 > y > 0)


print(func1(x, y))
print(func2(x, y))
print(func3(x, y))
