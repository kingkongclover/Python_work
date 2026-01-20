print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
while (True):
    print("Valitse haluamasi toiminto:")
    print("1) Tulosta merkkijono etuperin")
    print("2) Tulosta merkkijono takaperin")
    print("3) Tulosta merkkijonon pituus")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))

    if (Valinta == 1):
        merkkijono = input("Anna merkkijono: ")
        print("Merkkijono on etuperin", "'" + merkkijono + "'.")
        break
    elif (Valinta == 2):
        merkkijono = input("Anna merkkijono: ")
        print("Merkkijono on takaperin", "'" + merkkijono[::-1] + "'.")
        break
    elif (Valinta == 3):
        merkkijono = input("Anna merkkijono: ")
        print("Merkkijonon pituus on", str(len(merkkijono)) + ".")
        break
    elif (Valinta == 0):
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta.")

print("Kiitos ohjelman käytöstä.")
