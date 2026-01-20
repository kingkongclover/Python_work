print("Selvitetään tuotteen alennusprosentti ja myyntihinta.")
hinta = int(input("Mikä on tuotteen listahinta: "))
alennusprosentti = 0
print("Lasketaanko hinta")
print("1) yhdellä monihaaraisella valintarakenteella")
print("2) useilla erillisillä valintarakenteilla?")
valinta = int(input("Anna valintasi: "))
if (valinta == 1):
    print("Yhdellä monihaaraisella valintarakenteella tulokset ovat seuraavat:")
    if (hinta >= 300):
        alennusprosentti = 30
        hinta = round(hinta * 0.70, 2)
    elif (hinta >= 200):
        alennusprosentti = 20
        hinta = round(hinta * 0.80, 2)
    elif (hinta >= 100):
        alennusprosentti = 10
        hinta = round(hinta * 0.90, 2)
    print("Tuotteen alennus on", str(alennusprosentti) + "%", "ja hinnaksi jää", str(hinta) + "e.")
elif (valinta == 2):
    print("Monella erillisellä valintarakenteella tulokset ovat seuraavat:")
    if (hinta >= 300):
        alennusprosentti = 30
        hinta = round(hinta * 0.70, 2)
    if (hinta >= 200):
        alennusprosentti = 20
        hinta = round(hinta * 0.80, 2)
    if (hinta >= 100):
        alennusprosentti = 10
        hinta = round(hinta * 0.90, 2)
    print("Tuotteen alennus on", str(alennusprosentti) + "%", "ja hinnaksi jää", str(hinta) + "e.")
else:
    hinta = round(hinta, 2)
    print("Tuntematon valinta.")
    print("Tuotteen alennus on", str(alennusprosentti) + "%", "ja hinnaksi jää", str(hinta) + ".0e." )

print("Kiitos ohjelman käytöstä.")
