num = input("Enter number ")
if int(num) in [x for x in range(5, 21)]:
    print("На лугу пасется...", num, "коров")
elif num[-1] == '1':
    print("На лугу пасется...", num, "корова")
elif num[-1] in '234':
    print("На лугу пасется...", num, "коровы")
else:
    print("На лугу пасется...", num, "коров")