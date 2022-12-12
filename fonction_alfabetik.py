import random
import string

def kod_aleyatwa(n):
    kod = []

    while n > 0:

        alf = string.ascii_letters
        nb = random.choice(alf)
        if nb not in kod:
            kod.append(nb)
            n -= 1
    return "".join(kod)

print(kod_aleyatwa(9))

