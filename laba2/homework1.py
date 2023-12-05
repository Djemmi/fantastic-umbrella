year = input("Число: ")

if len(year) < 4:
    while len(year) < 4:
        year = "0" + year

if year == year[::-1]:
    print("1")
else:
    print("2")
