visszaszámlálás = int(input("Hány órás visszaszámlálásást tervezünk? "))

ido = visszaszámlálás

while visszaszámlálás > 0:
    print(visszaszámlálás)
    választás = input("Fel kell függeszteni a visszaszámlálásást(i/n)? ")
    if választás == "n":
        visszaszámlálás -=1
    elif választás == "i":
        ido +=1
        visszaszámlálás -=1

print(f"A rakéta a visszaszámlálásást követően ennyi órával indult: {ido}")