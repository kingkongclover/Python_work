def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue sähkönkulutustiedot")
    print("2) Analysoi päiväkulutus")
    print("3) Tallenna päiväkulutus")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def tiedostonimet(kumpi):
    if (kumpi == 1):
        nimi = input("Anna luettavan tiedoston nimi: ")
    elif (kumpi == 2):
        nimi = input("Anna kirjoitettavan tiedoston nimi: ")
    return nimi
    

def tiedostonluku(tiedNimi):
    lista = []
    try:
        tiedosto = open(tiedNimi, 'r', encoding="utf-8")
        while True:
            rivi = tiedosto.readline()
            if len(rivi) == 0:
                tiedosto.close()
                break
            lista.append(rivi[:-1])
        print("Tiedosto", "'" + tiedNimi + "'", "luettu.")
        print()
        lista.pop(0)
        lista.append("stop")
    except Exception:
        print("Tiedoston", "'" + tiedNimi + "'", "käsittelyssä virhe, lopetetaan.")
        exit(0)
    return lista

def analyysi(tiedot):
    analysoitu = []
    vastaus = 0
    while True:
        if (tiedot[0] == "stop"):
            break
        tieto = tiedot[0].split(";")
        tiedot.pop(0)
        testi = tiedot[0].split(";")
        if (tieto[0].split(" ")[0] == testi[0].split(" ")[0]):
            vastaus = vastaus + int(tieto[1]) + int(tieto[2])
        else:
            vastaus = vastaus + int(tieto[1]) + int(tieto[2])
            analysoitu.append(tieto[0].split(" ")[0] + ";" + str(vastaus))
            vastaus = 0
                              
        
    print("Päivittäiset summat laskettu.")
    analysoitu.append("stop")
    print()
    return analysoitu

def tiedostonkirjoitus(nimi, tiedot):
    tiedosto = open(nimi, 'w', encoding="utf-8")
    tiedosto.write("Pvm;Kulutus (Wh)\n")
    while True:
        if (tiedot[0] == "stop"):
            break
        tiedosto.write(tiedot[0] + "\n")
        tiedot.pop(0)
        
    print("Tiedosto", "'" + nimi + "'", "kirjoitettu.")
    print()
    return None

def paaohjelma():
    while True:
        valinta = valikko()
        if (valinta == 1):
            nimi = tiedostonimet(1)
            tiedot = tiedostonluku(nimi)
        elif (valinta == 2):
            try:
                anal = analyysi(tiedot)
            except Exception:
                print("Ei tietoja analysoitavaksi, lue tiedosto ennen analyysiä.")
                print()
        elif (valinta == 3):
            if (anal == None):
                print("Ei tietoja tallennetavaksi, analysoi tiedot ennen tallennusta.")
                print()
            else:
                nimi = tiedostonimet(2)
                tiedostonkirjoitus(nimi, anal)
        elif (valinta == 0):
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
    print()
    print("Kiitos ohjelman käytöstä.")
            



paaohjelma()









#eoc
