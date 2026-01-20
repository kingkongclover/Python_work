# Tehtävä L07T5.py

class AUTOT:
    merkki = ""
    hinta = ""


def tiedot(lista):
    autot = AUTOT()
    merkki = input("Anna auton merkki: ")
    hinta = input("Anna auton hinta: ")
    print()
    autot.merkki = merkki
    autot.hinta = hinta
    lista.append(autot.merkki + " " + autot.hinta)
    return lista
    


def tulosta(tietoja):
    print("Listalta löytyy seuraavat autot ja hinnat:")
    for x in range(len(tietoja)):
        print(tietoja[x])
    print()
    return None


def kirjoitus(tallennettava, tietoja):
    tiedosto = open(tallennettava, "w", encoding="utf-8")
    tiedosto.write("Auton merkki;Auton hinta\n")
    for x in range(len(tietoja)):
        tiedosto.write(tietoja[x].replace(" ", ";") + '\n')
    tiedosto.close()
    print("Tapahtumat kirjoitettu tiedostoon", "'" + tallennettava + "'.")
    print()



def paaohjelma():
    autolista = []
    tallennettava = input("Anna tallennettavan tiedoston nimi: ")
    print("Tämä ohjelma hallitsee autojen tietoja listalla.")
    while True:
        valinta = valikko()
        if valinta == str(1):
            tietoja = tiedot(autolista)
        elif valinta == str(2):
            tulosta(tietoja)
        elif valinta == str(3):
            kirjoitus(tallennettava, tietoja)
        elif valinta == str(0):
            print("Lopetetaan.")
            print()
            break
        else:
            print("Tuntematon valinta")
    print("Kiitos ohjelman käytöstä.")

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna auton tiedot")
    print("2) Tulosta autojen tiedot")
    print("3) Tallenna autojen tiedot tiedostoon")
    print("0) Lopeta")
    valinta = input("Anna valintasi: ")
    return valinta


paaohjelma()
