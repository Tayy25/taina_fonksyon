import string

karacte = string.ascii_letters+string.digits+"-"
fraz = input("antre on fraz")
for i in fraz:
    if i not in karacte:
        fraz = fraz.replace(i, "-")
print("Slug lan se :", fraz)
