def valikko():
    print("\nValitse haluamasi toiminto:")
    print("1) Anna merkkijono")
    print("2) Määritä askel")
    print("3) Tulosta merkkijono")
    print("0) Lopeta")
    valinta = input("Anna valintasi: ")
    return int(valinta)
    



def kysyMerkkijono():
    merkkijono = input("Anna merkkijono: ")
    return merkkijono



def kysyAskel():
    askel = input("Anna tulostuksessa käytettävä askel: ")
    return askel



def tulostaMerkkijono(mjono, askel):
    if askel == str(0):
        for i in mjono:
            print(mjono)
            mjono = mjono[:-1]
        print()
    else:
        print(mjono[::int(askel)])



def paaohjelma():
    print("Tällä ohjelmalla voi tulostaa merkkijonoja eri tavoin.",end="")
    while True:
        valinta = valikko()
        if valinta == 1:
            merkkijono = kysyMerkkijono()
        elif valinta == 2:
            askel = kysyAskel()
        elif valinta == 3:
            tulostaMerkkijono(merkkijono, askel)
        elif valinta == 0:
            print("Lopetetaan.")
            print()
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
    print("Kiitos ohjelman käytöstä.")






paaohjelma()
