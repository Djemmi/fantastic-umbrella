i = input().split(" ")

with open('hw2.txt', "w") as file:
    file.truncate(0)
    while i != ['']:
        print(i)
        print("passed while")
        for number in i:
            file.write(number + '\n')
        i = input().split(" ")

with open('hw2.txt', 'r+') as file:
    lines = [int(l.replace('\n', '')) for l in file.readlines()]
    file.write("Sum: " + str(sum(lines)) + "\n")
    file.write("Max: " + str(max(lines)) + "\n")
    file.write("Min: " + str(min(lines)))

