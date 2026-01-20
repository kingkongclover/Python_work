print("Tämä ohjelma laskee neljän tenttiarvosanan keskiarvon.")
Num1 = int(input("Anna 1. tenttiarvosana väliltä 0-5: "))
Num2 = int(input("Anna 2. tenttiarvosana väliltä 0-5: "))
Num3 = int(input("Anna 3. tenttiarvosana väliltä 0-5: "))
Num4 = int(input("Anna 4. tenttiarvosana väliltä 0-5: "))

Summa = Num1 + Num2 + Num3 + Num4
KeskiArvo = round(Summa/4,1)
KeskiKok = int(Summa/4)

print()

print("Antamiesi arvosanojen summa on", str(Summa) + '.')
print("Antamiesi arvosanojen keskiarvo on", str(KeskiArvo) + '.')
print("Keskiarvo on kokonaislukuna", str(KeskiKok) + '.')
print("Kiitos ohjelman käytöstä.")
