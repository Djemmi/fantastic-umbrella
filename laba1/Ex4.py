start_speed = int(input("Введите начальную скорость ( м/c ) "))

if start_speed < 0:
    while start_speed < 0:
        print("Начальная скорость должна быть не меньше нуля!")
        start_speed = int(input("Введите начальную скорость ( м/c ) "))

G = float(input("Введите ускорение свободного падения ( м/c^2 ) "))

if G < 0:
    while G < 0:
        print("Свободное падение должно быть не меньше нуля!")
        G = float(input("Введите ускорение свободного падения ( м/c^2 ) "))

time = float(input("Введите время ( c ) "))

if (time < 0) or time > (2 * start_speed) // G:
    while time > (2 * start_speed) // G or time < 0:
        print("Введенное время не корректно!")
        time = float(input("Введите время ( c ) "))

height = start_speed * time - 0.5 * G * time ** 2
print("\nИсходные данные:")
print("Начальная скорость: %21.5e" % start_speed)
print("Ускорение свободного падения: %0.5e" % G)
print("Время: %34.5e" % time)
print("\nВыходные данные:\nТекущая высота мяча: %20.5e" % height)
