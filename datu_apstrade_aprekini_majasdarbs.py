#12.05.2026
#Majas darbs

"""Izveido CSV failu ar:

5 produktiem
cenu
Uzraksti programmu, kas:

aprēķina kopējo summu
izvada dārgāko produktu
Paveikto aizsūti uz GitHub."""
#csv faila izveide ar 5 produktiem
with open("produkti.csv", "w", encoding="utf-8") as f:
    f.write("Maize,2\n")
    f.write("Siers,5\n")
    f.write("Kūka,15.5\n")
    f.write("Saldejums,0.68\n")
    f.write("Piens,1.2\n")

#apreikna kopeja suma
#izvada dargako produktu
with open("produkti.csv", encoding="utf-8") as f:


    summa = 0
    lielakacena = 0

    for rinda in f:
        produkts, cena = rinda.strip().split(",")
        summa += float(cena)
        if float(cena) > lielakacena:
            lielakacena = float(cena)
print("kopeja summa: ",summa)
print("Lielaka produkta cena", lielakacena)
