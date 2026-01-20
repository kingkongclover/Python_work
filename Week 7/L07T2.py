# Tehtävä L07T2.py

class TILI:
    nimi = ""
    saldo = ""

def kysyja1(tilinimi):
    tilinimi = input("Anna pankkitilin nimi: ")
    return tilinimi

def kysyja2(tilisaldo):
    tilisaldo = input("Anna pankkitilin saldo: ")
    tilisaldo = round(float(tilisaldo) ,2)
    return tilisaldo

def tulostus(nimi, saldo):
    print("Pankkitilillä", "'" + nimi + "'","on nyt rahaa", str(saldo) + "e.")
    print("Kiitos ohjelman käytöstä.")
    return None

def paaohjelma():
    tili = TILI()
    tili.nimi = kysyja1(tili.nimi)
    tili.saldo = kysyja2(tili.saldo)
    tulostus(tili.nimi, tili.saldo)
    return None

paaohjelma()
