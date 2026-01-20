Alku = int(input("Anna aloitusarvo: "))
Loppu = int(input("Anna lopetusarvo: "))
print()
Numero = Alku - 1
print("Toteutus for-lauseella:")
for i in range(Alku, Loppu + 1, 1):
    Numero = Numero + 1
    print(Numero, end=' ')
print()
print()
Numero = Alku - 1
print("Toteutus while-lauseella:")
while (Numero < Loppu ):
    Numero = Numero + 1
    print(Numero, end=' ')
print()
print()
print("Kiitos ohjelman käytöstä.")
    
