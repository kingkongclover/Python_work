def paaohjelma():
    tulostaOhjeet()
    luvut = kysyLuku()
    tulostaTiedot(luvut)


    print("Kiitos ohjelman käytöstä.")
    return None
    

def tulostaOhjeet():
    print("Tämä ohjelma etsii antamistasi luvuista pienimmän.")
    print("Ohjelman lopussa se kertoo pienimmän luvun lisäksi antamiesi")
    print("lukujen lukumäärän.")
    print()
    return None

def kysyLuku():
    lista = []
    luku1 = input("Anna positiivinen kokonaisluku: ")
    luku2 = input("Anna vertailtava positiivinen kokonaisluku (0 lopettaa): ")
    if luku2 == str(0):
        tulostaTiedot(luku1)
    lista.append(int(luku1))
    lista.append(int(luku2))
    pienempi = vertaileLukuja(lista)
    while True:
        print("Annetuista luvuista pienempi oli", pienempi+".")
        uusi = input("Anna uusi positiivinen kokonaisluku (0 lopettaa): ")
        if uusi == str(0):
            break
        lista.append(int(uusi))
        pienempi = vertaileLukuja(lista)
    print()
    return lista      
        


def vertaileLukuja(lista):
    pienin = min(lista)
    return str(pienin)
    
    
    
def tulostaTiedot(pienin):
    if len(pienin) == 1:
        print("Annoit yhden luvun, joka oli", str(min(pienin)) + ".")
    else:
        print("Annoit", len(pienin), "lukua.")
        print("Annetuista luvuista pienin oli", str(min(pienin)) + ".")
    return None
    

paaohjelma()
