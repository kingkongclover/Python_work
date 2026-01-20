print("Tämä ohjelma etsii luvuilla 5 ja 7 jaollista lukua annetulta lukualueelta.")
Alaraja = int(input("Anna lukualueen alaraja: "))
Ylaraja = int(input("Anna lukualueen yläraja: "))
Luku = Alaraja - 1
Loyto = False
for i in range(Alaraja, Ylaraja + 1, 1):
    Luku = Luku + 1
    if (Luku % 5 == 0):
        if (Luku % 7 == 0):
            Loyto = True
            print("Luku", Luku, "on jaollinen 5:llä ja 7:llä.")
            break
        else:
            print(Luku, "ei ole jaollinen seitsemällä, hylätään.")
    else:
        print(Luku, "ei ole jaollinen viidellä, hylätään.")
if (Loyto == False):
    print("Alueelta ei löytynyt sopivaa lukua.")   
else:
    print("Lopetetaan etsintä.")
    
print("Kiitos ohjelman käytöstä.")
