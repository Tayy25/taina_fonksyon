import string


def dekripte():
    alf = "abcdefghijklmnopqrstuvwxyz"
    tab = []
    n = (input("antre mo ou vle dekripte a"))
    for i in n.split("-"):
        tab.append((alf[int(i)]))
    return "-".join(tab)

print(dekripte())