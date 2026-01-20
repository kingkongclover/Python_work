def tarkistaRivi(Luettava, Kirjo):
    Ltiedosto = open(Luettava, "r", encoding="utf-8")
    while True:
        rivi = Ltiedosto.readline()[:-1]
        rivioikea = "".join(i for i in rivi.lower() if i.isalnum())
        
        if len(rivi) == 0:
            break
        elif rivioikea.isalpha() == False:
            print("Ei OK:", "'" + rivi + "'")
        else:
            if (rivioikea == rivioikea[::-1]) and len(rivioikea) > 2:
                kirjoitaRivi(Kirjo, rivi, rivioikea)
                print("OK:", "'" + rivi + "'")
            else:
                print("Ei OK:", "'" + rivi + "'")
    Ltiedosto.close()
    return None
        
    



def kirjoitaRivi(nimi, rivi, kaannetty):
    Ktiedosto = open (nimi, "a", encoding="utf-8")
    Ktiedosto.write(rivi + '\n')
    Ktiedosto.write("----> " + kaannetty + '\n')
    Ktiedosto.close()
    return None




def paaohjelma():
    LuettavaTiedosto = input("Anna luettavan tiedoston nimi: ")
    KirjoitettavaTiedosto = input("Anna kirjoitettavan tiedoston nimi: ")
    tarkistaRivi(LuettavaTiedosto, KirjoitettavaTiedosto)
    print("Kiitos ohjelman käytöstä.")
    



paaohjelma()
