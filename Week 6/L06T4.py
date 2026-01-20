def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna tiedostonimet")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return str(Valinta)

def tiedostonimet():
    luku = ""
    kirjotus = ""
    print("Anna tiedostonimet")
    print("Luettavan tiedoston nimi on", "'" + luku + "'.")
    luku = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    print("Kirjoitettavan tiedoston nimi on", "'" + kirjotus + "'.")
    kirjotus = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    print()
    nimet = []
    nimet.append(luku)
    nimet.append(kirjotus)
    return(nimet)

def lukeminen(nimet):
    lista = []
    tiedosto = open(nimet[0], 'r', encoding="utf-8")
    while True:
        rivi = tiedosto.readline()
        if len(rivi) == 0:
            tiedosto.close()
            break
        lista.append(int(rivi[:-1]))
    return lista


def analyysi(luettu):
    tulos = []
    luettu.sort()
    tulos.append(luettu[0]) #pienin
    tulos.append(luettu[-1]) #suurin
    print()
    return tulos


def kirjoittaminen(nimet, tulos):
    tiedosto = open(nimet[1], "w", encoding="utf-8")
    tiedosto.write("Analyysin tulokset ovat seuraavat:\n")
    tiedosto.write("Datan pienin arvo on " + str(tulos[0]) + '.\n')
    tiedosto.write("Datan suurin arvo on " + str(tulos[1]) + '.\n')
    tiedosto.close()
    print()


def paaohjelma():
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    while True:
        valinta = valikko()
        if valinta == str(1):
            nimet = tiedostonimet()
        elif valinta == str(2):
            print("Suoritetaan analyysi")
            luettu = lukeminen(nimet)
            tulos = analyysi(luettu)
        elif valinta == str(3):
            print("Kirjoitetaan tulokset tiedostoon")
            kirjoittaminen(nimet, tulos)
        elif valinta == str(0):
            print("Lopetetaan")
            print()
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()

    print("Kiitos ohjelman käytöstä.")
    
    



paaohjelma()
