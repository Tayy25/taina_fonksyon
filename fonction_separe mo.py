def separe_mo():
    word = input("Antre on mo: ")
    new_word = []
    for i in word:
        new_word.append(i)
    return ",".join(new_word)
print("Mo separe a se :", separe_mo())
