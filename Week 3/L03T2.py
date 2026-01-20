print("Selvitetään sanojen aakkosjärjestys.")
Sana1 = input("Anna sana 1: ")
Sana2 = input("Anna sana 2: ")

if (Sana1 < Sana2):
    print("'" + Sana1 + "'", "on aakkosissa aiemmin kuin", "'" + Sana2 + "'.")
elif (Sana2 < Sana1):
    print("'" + Sana2 + "'", "on aakkosissa aiemmin kuin", "'" + Sana1 + "'.")
elif (Sana1 == Sana2):
    print("Sanat ovat samoja,", "'" + Sana1 + "'." )
print()

print("Selvitetään merkin sisältyminen merkkijonoon.")
merkkijono = input("Anna merkkijono: ")
merkki = input("Anna etsittävä merkki: ")

if (merkki in merkkijono):
    print("Merkki", "'" + merkki + "'", "sisältyy merkkijonoon", "'" + merkkijono + "'.")
else:
    print("Merkki", "'" + merkki + "'", "ei sisälly merkkijonoon", "'" + merkkijono + "'.")
print()

print("Selvitetään, onko sana palindromi.")
Sana3 = input("Anna testattava sana: ")

if (Sana3 == Sana3[::-1]):
    print("Sana", "'" + Sana3 + "'", "on palindromi.")
    print("Kiitos ohjelman käytöstä.")
elif (Sana3 != Sana3[::-1]):
    print("Sana ei ole palindromi.")
    print("Sana on etuperin", "'" + Sana3 + "'", "ja takaperin", "'" + Sana3[::-1] + "'.")
    print("Kiitos ohjelman käytöstä.")
