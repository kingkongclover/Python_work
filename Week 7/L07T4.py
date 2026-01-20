# Tehtävä L07T4.py

class TULOS:
    pienin = ""
    suurin = ""
    summa = ""
    keskiarvo = ""

def paaohjelma():
    tulos = TULOS()
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    while True:
        valinta = valikko()
        if valinta == str(1):
            nimet = tiedostonimet()
        elif valinta == str(2):
            luettu = lukeminen(nimet)
        elif valinta == str(3):
            tuls = analyysi(luettu, tulos)
        elif valinta == str(4):
            kirjoittaminen(nimet, tulos)
        elif valinta == str(0):
            print("Lopetetaan")
            print()
            break
    print("Kiitos ohjelman käytöstä.")

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna tiedostonimet")
    print("2) Lue tiedosto")
    print("3) Analysoi")
    print("4) Kirjoita tiedosto")
    print("0) Lopeta")
    valinta = input("Anna valintasi: ")
    return valinta

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
    print("Tiedosto", "'" + nimet[0] + "'", "luettu.")
    print()
    return lista

def analyysi(luettu, tulos):
    luettu.sort()
    tulos.pienin = luettu[0]
    tulos.suurin = luettu[-1]
    tulos.summa = sum(luettu)
    tulos.keskiarvo = round(sum(luettu)/len(luettu),0)
    print("Analyysi suoritettu.")
    print()
    return tulos

def kirjoittaminen(nimet, tulos):
    tiedosto = open(nimet[1], "w", encoding="utf-8")
    tiedosto.write("Analyysin tulokset ovat seuraavat:\n")
    tiedosto.write("Datan pienin arvo on " + str(tulos.pienin) + '.\n')
    tiedosto.write("Datan suurin arvo on " + str(tulos.suurin) + '.\n')
    tiedosto.write("Datan summa on " + str(tulos.summa) + '.\n')
    tiedosto.write("Datan keskiarvo on " + str(tulos.keskiarvo) + '.\n')
    tiedosto.close()
    print("Tulokset kirjoitettu tiedostoon.")
    print()


paaohjelma()
