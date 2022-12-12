import string


def kripte():
    m = input("antre on mo: ")
    mo = []
    for i in m:
        mo.append(str(string.ascii_lowercase.index(i)))
    return "-".join(mo)
print(kripte())