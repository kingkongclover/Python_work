print("Tämä ohjelma laskee risteilyhintoja.")
Hytti = input("Minkälainen hytti on kyseessä - A, B vai C-hytti: ")
Sesonki = input("Onko sesonkiaika (k/e): ")
Kanta = input("Onko kanta-asiakas (k/e): ")

C = round(79 ,0)
B = round(79 * 1.1 ,0)
A = round(79 * 1.6 ,0)

if(Hytti == "A"):
    if (Sesonki == "k"):
        if (Kanta == "k"):
            A = A * 2.75 * 0.9
        elif (Kanta == "e"):
            A = A * 2.75
    elif (Sesonki == "e"):
        if (Kanta == "k"):
            A = A * 0.9
        elif (Kanta == "e"):
            A = A
    print("A-hytti maksaa", round(A ,2),"euroa.")
            
elif(Hytti == "B"):
    if (Sesonki == "k" or "K"):
        if (Kanta == "k"):
            B = B * 1.75 * 0.9
        elif (Kanta == "e"):
            B = B * 1.75
    elif (Sesonki == "e"):
        if (Kanta == "k"):
            B = B * 0.9
        elif (Kanta == "e"):
            B = B
    print("B-hytti maksaa", round(B ,2),"euroa.")
            
elif(Hytti == "C"):
    if (Sesonki == "k"):
        if (Kanta == "k"):
            C = C * 1.5 * 0.9
        elif (Kanta == "e"):
            C = C * 1.5
    elif (Sesonki == "e"):
        if (Kanta == "k"):
            C = C * 0.9
        elif (Kanta == "e"):
            C = C
    print("C-hytti maksaa", round(C ,2),"euroa.")



