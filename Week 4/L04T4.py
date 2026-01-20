print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
while (True):
    print("Valitse haluamasi toiminto:")
    print("1) Syötä tiedot")
    print("2) Laske")
    print("3) Tulosta tulokset")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))

    if (Valinta == 1):
        print("Syötä tiedot")
        Luku1 = int(input("Anna luku 1: "))
        Luku2 = int(input("Anna luku 2: "))
        print()
    elif (Valinta == 2):
        Lasku = Luku1 + Luku2
        print("Laske")
        print()
    elif (Valinta == 3):
        print("Tulosta tulokset")
        print("Lukujen summa on", str(Lasku) + ".")
        print()
    elif (Valinta == 0):
        print("Lopetetaan.")
        print()
        break
    else:
        print("Tuntematon valinta, yritä uudestaan.")
        print()

print("Kiitos ohjelman käytöstä.")
