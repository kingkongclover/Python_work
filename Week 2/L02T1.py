Nimi = input("Mikä nimesi on: ")
Kanta = int(input("Anna kolmion kanta kokonaislukuna: "))
Korkeus = round(float(input("Anna kolmion korkeus desimaalilukuna: ")),2)
PintaAla = Kanta * Korkeus / 2

print(Nimi, "annoit kannaksi", Kanta, "ja korkeudeksi", Korkeus)
print("Kolmion pinta-ala on tällöin", PintaAla)
print("Kiitos ohjelman käytöstä.")
