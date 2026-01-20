def paaohjelma():
    TiedostonNimi = input("Anna tallennettavan tiedoston nimi: ")
    TiedostoKirjoita(TiedostonNimi)
    TiedostoLue(TiedostonNimi)
    print("Kiitos ohjelman käytöstä.")
    return None
    

def TiedostoKirjoita(TiedostonNimiP):
    tiedosto = open(TiedostonNimiP, "w", encoding="utf-8")
    while True:
        Nimi = input("Anna tiedostoon tallennettava nimi (enter lopettaa): ")
        if (Nimi == str("")):
            break
        else:
            tiedosto.write(Nimi + '\n')
    tiedosto.close()
    return None
        
def TiedostoLue(TiedostonNimiP):
    tiedosto = open(TiedostonNimiP, "r", encoding="utf-8")
    print("Tiedostoon", "'" + TiedostonNimiP + "'", "on tallennettu seuraavat nimet:")
    while True:
        rivi = tiedosto.readline()
        if (len(rivi) == 0):
            break
        else:
            print(rivi, end = "")
    tiedosto.close()
    return None

paaohjelma()
    
