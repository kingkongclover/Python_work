Maara = 0
Summa = 0

while True:
    Paino = float(input("Anna paino väliltä 30-130 kg (0 lopettaa): "))
    if (30 <= Paino <= 130):
        Maara = Maara + 1
        Summa = Summa + Paino
    elif (Paino == 0):
        Keskiarvo = round(Summa / Maara, 1)
        print("Painojen keskiarvo on", str(Keskiarvo) + ".")
        print("Kiitos ohjelman käytöstä.")
        break
    else:
        print("Väärä syöte. Painon tulee olla 30 ja 130 kg välillä (0 lopettaa).")
