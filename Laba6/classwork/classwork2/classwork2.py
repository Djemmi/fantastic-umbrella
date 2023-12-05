from sympy import pi

def hasNines(line: str):
    try:
        line.index("9999999")
        return True
    except:
        return False


pilen = 1
while not hasNines(str(pi.n(pilen))):
    print(str(pi.n(pilen)))
    pilen += 1

print(str(pi.n(pilen)).index("9999999"))
