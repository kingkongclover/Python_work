import math

print("Tämä ohjelma tekee painolle ja pituudelle yksikkömuunnoksia.")
PainoK = float(input("Anna paino kiloina: "))
print("Paino on", PainoK, "kg eli", round(PainoK * 2.205, 2), "naulaa.")
print()
PituusCm = float(input("Anna pituus sentteinä: "))

PituusM = round(PituusCm/100,2)

PituusTuuma = round(PituusCm / 2.54,1)
PituusJalka = round(PituusTuuma // 12,1)

TuumaLaskettu = round(PituusTuuma - PituusJalka * 12,1)

print("Pituus on",PituusM ,"metriä", end=" ")
print("eli amerikkalaisittain",PituusJalka, end=" ")
print("jalkaa ja",TuumaLaskettu, "tuumaa.")


print("Kiitos ohjelman käytöstä.")
