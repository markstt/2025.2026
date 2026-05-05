#05.05.2026

#datu apstrade un apreikni

#nolasit un izvadit

with open("klase.csv", encoding="utf-8") as f:
    next(f)
    for line in f:
        vards,atzime = line.strip().split(",")
        print(vards,atzime)
with open("klase.csv", encoding="utf-8") as f:
    next(f)
    for line in f:
        vards,atzime = line.strip().split(",")
        if int(atzime) >= 8:
            print(vards,atzime)
summa = 0
with open("klase.csv", encoding="utf-8") as f:
    next(f)
    for line in f:
        vards,atzime = line.strip().split(",")
        summa += int(atzime)
        print(vards,atzime)
summa = 0
skaits = 0
with open("klase.csv", encoding="utf-8") as f:
    next(f)
    for line in f:
        vards,atzime = line.strip().split(",")
        summa += int(atzime)
        skaits += 1 
        print(summa/skaits)