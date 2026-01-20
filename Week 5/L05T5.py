PITUUS_MIN = 5
PITUUS_MAX = 15
EROTIN = ';'



def tulostaOhjeet():
    print("Tämä ohjelma kysyy merkkijonoja, tarkistaa ne ja tulostaa hyväksytyt merkkijonot.")
    print("Anna pyydetyn mittaisia merkkijonoja, joissa ei ole kiellettyjä merkkejä.")
    print("Merkkijonojen tulee olla vähintään 5 ja korkeintaan 15 merkkiä pitkiä.")
    print("Merkkijonoissa ei osaa olla merkkiä ';'.")
    print()


def kysyMerkkijono(apua):
    if apua == 0:
        merkkijono = input("Anna merkkijono 5-15 merkkiä (enter lopettaa): ")
    elif apua == 1:
        merkkijono = input("Anna seuraava merkkijono 5-15 merkkiä (enter lopettaa): ")
    elif apua == 2:
        merkkijono = input("Anna uusi merkkijono 5-15 merkkiä (enter lopettaa): ")
    return merkkijono


def tarkistaMerkkijono(mjono):
    if len(mjono)< PITUUS_MIN:
        print("Liian lyhyt,",len(mjono),"merkkiä.")
    elif len(mjono)> PITUUS_MAX:
        print("Liian pitkä,", len(mjono),"merkkiä.")
    elif EROTIN in mjono:
        print("Merkkijonossa on kielletty merkki ';'.")
        print()
    else:
        return str(mjono + ';')
        
            
    


def tulostaHyvaksytyt(tarkistetut):
    print("\nAnnoit seuraavat hyväksytyt merkkijonot:")
    erottelu = tarkistetut.replace(";", "\n")
    print(erottelu)


def paaohjelma():
    apua = 0
    tulostaOhjeet()
    tarkistetut = ""
    while True:
        merkkijono = kysyMerkkijono(apua)
        apua = 2
        if len(merkkijono) == 0:
            break
        mjono = tarkistaMerkkijono(merkkijono)
        if mjono != None:
            apua = 1
            tarkistetut = tarkistetut + mjono
    tulostaHyvaksytyt(tarkistetut[:-1])

    print("Kiitos ohjelman käytöstä.")

paaohjelma()
