k = int(input("Count per circle: "))
m = int(input("Minutes per circle: "))
n = int(input("Total number: "))

sircles = n // k
if n % k != 0:
    sircles += 1

print(sircles * m)