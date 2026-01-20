def paaohjelma():
    TiedostonNimi = input("Anna luettavan tiedoston nimi: ")
    tiedosto = open(TiedostonNimi, "r", encoding="utf-8")
    Pituus = 0
    Maara = 0
    
    while True:
        rivi = tiedosto.readline()
        if (len(rivi) == 0):
            break
        else:
            Maara = Maara + 1
            Pituus = Pituus + len(rivi)
    print("Tiedostossa oli", Maara, "nimeä ja", Pituus, "merkkiä.")
    print("Keskimäärin nimen pituus oli", round((Pituus - Maara) / Maara), "merkkiä.")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
