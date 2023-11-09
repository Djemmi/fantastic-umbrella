start_speed = 5
G = 9.80665
time = 0.6

height = start_speed * time - 0.5 * G * time ** 2
print("Исходные данные:")
print("Начальная скорость: %21.5e" % start_speed)
print("Ускорение свободного падения: %0.5e" % G)
print("Время: %34.5e" % time)
print("\nВыходные данные:\nТекущая высота мяча: %20.5e" % height)
