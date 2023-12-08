i = input().split(" ")

with open('hw1.txt', "w") as file:
    for number in i:
        file.write(number + "\n")
