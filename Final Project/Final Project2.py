import sys

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
    try:
        lista = []
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
        sys.exit(0)
    return lista

def analyysi(tiedot):
    try:
        analysoitu = []
        vastaus = 0
        while True:
            if (tiedot[0] == "stop"):
                break
            tieto = tiedot[0].split(";")
            tiedot.append(tiedot[0])
            tiedot.pop(0)
            testi = tiedot[0].split(";")
            #splitillä erotetaan pvm ja kellonaika toisistaan ja alla testataan onko pvm sama, jos on WH lisätään yhteen.
            if (tieto[0].split(" ")[0] == testi[0].split(" ")[0]):
                vastaus = vastaus + int(tieto[1]) + int(tieto[2])
            else:
                vastaus = vastaus + int(tieto[1]) + int(tieto[2])
                analysoitu.append(tieto[0].split(" ")[0] + ";" + str(vastaus))
                vastaus = 0


        tiedot.pop(0)
        tiedot.append("stop")
                                  
            
        print("Päivittäiset summat laskettu.")
        analysoitu.append("stop")
        print()
        
    except Exception:
        print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
        print()
    
    return analysoitu

def tiedostonkirjoitus(nimi, tiedot):
    try:
        tiedosto = open(nimi, 'w', encoding="utf-8")
        tiedosto.write("Pvm;Kulutus (Wh)\n")
        while True:
            if (tiedot[0] == "stop"):
                tiedot.append("stop")
                tiedot.pop(0)
                break
            tiedosto.write(tiedot[0] + "\n")
            tiedot.append(tiedot[0])
            tiedot.pop(0)
        tiedosto.close()
        print("Tiedosto", "'" + nimi + "'", "kirjoitettu.")
        print()
        
    except Exception:
        print("Tiedoston", "'" + nimi + "'", "käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
        
    return None

def paaohjelma():
    anal = None
    tiedot = None
    while True:
        valinta = valikko()
        if (valinta == 1):
            nimi = tiedostonimet(1)
            tiedot = tiedostonluku(nimi)
        elif (valinta == 2):
            anal = analyysi(tiedot)
        elif (valinta == 3):
            if (anal == None):
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
                print()
            else:
                nimi = tiedostonimet(2)
                tiedostonkirjoitus(nimi, anal)
        elif (valinta == 0):
            print("Lopetetaan.")
            print()
            print("Kiitos ohjelman käytöstä.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()
            
    return None


paaohjelma()









#eoc
