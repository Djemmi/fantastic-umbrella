new_number = input("Ender number (0 to exit): ")
while new_number != "0":
    digits_sum = 0
    for digit in new_number:
        digits_sum += int(digit)
    print(digits_sum)
    new_number = input("Ender number (0 to exit): ")
