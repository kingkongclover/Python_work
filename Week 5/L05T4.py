def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Syötä tiedot")
    print("2) Laske")
    print("3) Tulosta tulokset")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def kysyLuku():
    print("Syötä tiedot")
    Luku1 = int(input("Anna kokonaisluku 1: "))
    Luku2 = int(input("Anna kokonaisluku 2: "))
    return Luku1, Luku2

def summa(luvut):
    vastaus = sum(luvut)
    return vastaus


def erotus(luvut):
    vastaus = luvut[0] - luvut[1]
    return vastaus


def tulostaTulokset(summa, erotus, luvut):
    print("Luvut ovat", luvut[0],"ja",str(luvut[1])+".")
    print("Lukujen summa on", summa, "ja erotus on", str(erotus) +".")


def paaohjelma():
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    while (True):
        Valinta = valikko()

        if (Valinta == 1):
            luvut = kysyLuku()
            print()
        elif (Valinta == 2):
            print("Laske")
            sSumma = summa(luvut)
            eErotus = erotus(luvut)
            print()
        elif (Valinta == 3):
            print("Tulosta tulokset")
            tulostaTulokset(sSumma, eErotus, luvut)
            print()
        elif (Valinta == 0):
            print("Lopetetaan.")
            print()
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()

    print("Kiitos ohjelman käytöstä.")
    
    



paaohjelma()
