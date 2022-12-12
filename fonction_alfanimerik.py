import random
import string


def alfanimerik(n):
    kod = []
    while n > 0:
        alf = string.ascii_letters+string.digits
        nb= random.choice(alf)
        if nb not in kod:
            kod.append(nb)
            n -=1
    return "".join(kod)
print(alfanimerik(7))

