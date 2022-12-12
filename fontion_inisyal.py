def inisyal():
    full_name = input("Antre nonw: ")
    add = []
    ini = ""
    for i in full_name:
        full_name =full_name.replace(" ", "-")
    for word in full_name.split("-"):
        add.append(word)
    for a in add:
        ini += a[0].upper()
    print("Men inisyal ou :", ini)
inisyal()