# Tehtävä L07T3.py


def paaohjelma():
        tiedostoNimi = input("Anna tiedoston nimi: ",)
        tiedosto = open(tiedostoNimi, 'r', encoding="utf-8")
        tiedosto.readline()
        print("Kalastuskilpailun tulokset ovat seuraavat:")
        while (True):
            rivi = tiedosto.readline()
            sarake = rivi.split(';')
            if len(rivi) == 0:
                break
            rivi = rivi[:-1]
            sarake = rivi.split(';')
            print("Joukkue", "'" + sarake[0] + "'", "sai kalan", sarake[1] + ",", "joka oli", sarake[2], "cm.")
        print("Kiitos ohjelman käytöstä.")
        return None
            

paaohjelma()
