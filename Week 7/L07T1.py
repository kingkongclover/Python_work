# Tehtävä L07T1.py



def lisays(ostoslista):
    tuote = input("Anna lisättävä tuote: ",)
    ostoslista.append(tuote)
    return ostoslista

def poisto(ostoslista):
    poistettava = input("Anna poistettavan tuotteen järjestysnumero: ",)
    if ostoslista.index(ostoslista[-1]) < int(poistettava) - 1 or poistettava == str(0):
        print("Indeksiä", poistettava, "ei löydy.")
        print("Tuotteiden järjestysnumerot alkavat numerosta 1.")
    else:    
        del ostoslista[int(poistettava) - 1]
    return ostoslista

        
        


def valikko():
    ostoslista = []
    while True:
        print("Ostoslistasi sisältää seuraavat tuotteet:")
        for i in ostoslista:
            print(i, end=" ")
        print("\nValitse haluamasi toiminto:")
        print("1) Lisää tuote listaan")
        print("2) Poista tuote listasta")
        print("0) Lopeta")
        valinta = input("Valintasi: ",)
        if (valinta == str(1)):
            lisays(ostoslista)
            print()
                        
        elif (valinta == str(2)):
            print("Ostoslistassasi on", len(ostoslista), "tuotetta.")
            poisto(ostoslista)
            print()
        elif (valinta == str(0)):
            print("Lopetetaan")
            print("Sinulta jäi ostamatta seuraavat tuotteet:")
            if len(ostoslista) == int(0):
                print()
                print()
            else:
                for i in ostoslista:
                    print(i, end=" ")
                print("\n")
            print("Kiitos ohjelman käytöstä.")
            break
        else:
            print("Tunnistamaton valinta, yritä uudestaan.")
            print()
    return None

def paaohjelma():
    valikko()
    return None

paaohjelma()
# eof
