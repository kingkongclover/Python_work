def paaohjelma():
    tulostaOhjeet()
    nimi = kysyNimi()
    tulostaTulokset(nimi)


    print("Kiitos ohjelman käytöstä.")
    return None
    

def tulostaOhjeet():
    print("Tämä ohjelma kysyy ja tulostaa tietoja.")
    print("Tämä aliohjelma tulostaa ohjeita käyttäjälle.")
    print("Anna nimesi kahdessa osassa.")
    return None

def kysyNimi():
    print("Tämä aliohjelma kysyy nimen.")
    etunimi = input("Anna etunimi: ")
    print("Tämä aliohjelma kysyy nimen.")
    sukunimi = input("Anna Sukunimi: ")
    return etunimi, sukunimi

def tulostaTulokset(nimi):
    print("Tämä aliohjelma tulostaa nimesi.")
    print("Hei", nimi[0], nimi[1])

paaohjelma()
