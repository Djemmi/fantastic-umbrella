line = input("Enter line: ")

small_count = 0
big_count = 0

for x in line:
    if x.isupper():
        big_count += 1
    else:
        small_count += 1

if big_count > small_count:
    line = line.upper()
elif big_count < small_count:
    line = line.lower()

print(line)