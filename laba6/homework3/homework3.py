"""
опяяять задание бредовое еще и о печаткой...
в целом по тз проходит, можете дописать приколов разных,
а я писать ничего не хочу :3
"""

with open('hw3.txt', 'r') as file:
    hall = [r.replace('\n', '').split(" ") for r in file.readlines()]
    free_places = 0
    total_places = 0
    row_number = 1
    row_free_places = []

    # parse
    for row in hall:
        row_free_places_num = 0
        for place in row:
            if place == "1":
                free_places += 1
                row_free_places_num += 1
            total_places += 1
        row_free_places.append(row_free_places_num)
        row_number += 1

    your_place: [] = input("Enter your place: ").split(" ")
    print("Your place is empty\n\n") if hall[int(your_place[0])][int(your_place[1])] == "1" else print("Your place is taken\n\n")

    print("Free places in each row:", " ".join([str(x) for x in row_free_places]))
    print("Total free places:", free_places)
    print("Total places:", total_places)
