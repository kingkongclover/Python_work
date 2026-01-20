def Paaohjelma():
    Luettava_Nimi = input("Anna luettavan tiedoston nimi: ")
    Kirjoitettava_Nimi = input("Anna tallennettavan tiedoston nimi: ")
    Kulutus = Luettava(Luettava_Nimi, "Kulutus")
    Pvm = Luettava(Luettava_Nimi, "Pvm")
    x = 2
    Paiva_Kulutus = 0
    Kulutukset = []
    if Kulutukset[0] == "00":
        Kulutus.remove("00")
        Kulutus.insert(0, "01")
    for i in Kulutus:
        x += 1
        if x % 3 == 0:
            if i == "00":
                Kulutukset.append(int(round(Paiva_Kulutus, 0)))
                Paiva_Kulutus = 0
        elif x % 3 != 0:
            Paiva_Kulutus += float(i)
    if Kulutus[len(Kulutus) - 2] != "00":
        Kulutukset.append(int(round(Paiva_Kulutus, 0)))
    Kirjoitettava(Kirjoitettava_Nimi, Pvm, Kulutukset)
    print("Kiitos ohjelman käytöstä.")



def Luettava(Luettava_Nimi, Valinta):
    Tiedosto = open(f"{Luettava_Nimi}", "r")
    Turha = Tiedosto.readline()
    Rivi = Tiedosto.readline()
    Pvm = []
    Pv_Kulutus = []
    while len(Rivi) > 0:
        Sana =""
        for i in Rivi:
            if i == " ":
                Pvm.append(Sana)
                Sana =""
            elif i == ";" or i == "\n":
                Pv_Kulutus.append(Sana)
                Sana = ""
            else:
                Sana += i
        Rivi = Tiedosto.readline()
    Pvm = list(dict.fromkeys(Pvm))

    if Valinta == "Kulutus":
        return Pv_Kulutus
    elif Valinta == "Pvm":
        return Pvm


    
def Kirjoitettava(Kirjoitettava, Pvm, Kulutus):
    Tiedosto = open(f,"{Kirjoitettava}", "w")
    Tiedosto.write("       Pvm:  kWh\n")
    for i in range(len(Pvm)):
        if len(str(Kulutus[i])) == 1:
            Rivi = (f,"{Pvm[i]}:    {Kulutus[i}}\n")
        elif len(str(Kulutus[i])) == 2:
            Rivi = (f,"{Pvm[i]}:    {Kulutus[i}}\n")
        elif len(str(Kulutus[i])) == 3:
            Rivi = (f,"{Pvm[i]}:    {Kulutus[i}}\n")
        else:
            break
        Tiedosto.write(Rivi)
    Tiedosto.close()


        
Paaohjelma()
