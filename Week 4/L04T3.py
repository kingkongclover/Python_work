Pisin = ""
Maara = 0

print("Ohjelma kysyy merkkijonoja ja etsii niistä pisimmän.")
Jonomaara = int(input("Kuinka monta merkkijonoa kysytään: "))
Minimi = int(input("Mikä on merkkijonon minimipituus: "))
Eisaaolla = input("Mitä merkkiä merkkijonossa ei saa olla: ")
for i in range(0, Jonomaara, 1):
    Jono = input("Anna merkkijono: ")
    Maara = Maara + 1
    if (len(Jono) > len(Pisin)):
        Pisin = Jono
    if (len(Jono) > Minimi):
        if (Eisaaolla in Jono):
            print("Ohjelma päättyi, koska merkkijonossa oli kielletty merkki.")
            break
    elif (len(Jono) < Minimi):
        print("Ohjelma päättyi, koska merkkijonon minimipituus ei täyttynyt.")
        break
if (Maara == Jonomaara):
    print("Ohjelma päättyi, koska maksimimäärä merkkijonoja tuli täyteen.")
print("Annoit", Maara, "merkkijonoa.")
print("Pisin merkkijono oli", "'" + Pisin + "',", "jossa oli", len(Pisin),  "merkkiä.")
print("Kiitos ohjelman käytöstä.")

            
            
        
