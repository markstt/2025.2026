""""3. uzdevums — Datu apstrāde (10 p)

Izveido failu dati_ieskaite.csv ar šādu saturu:

vards,vecums

Anna,16

Jānis,18

Laura,20

Marta,15


3.1. Uzraksti programmu, kas izvada tikai pilngadīgos. (5 p)

3.2. Aprēķini vidējo vecumu. (5 p)


Kodus ievieto atbilžu laukā"""

with open("dati_ieskaite.csv", encoding="utf-8") as f:
    next(f)
    for line in f:
        vards,vecums = line.strip().split(",")
        if int(vecums) >= 18:
            print(vecums)
with open("dati_ieskaite.csv", encoding="utf-8") as f:
    next(f)
    summa = 0
    skaits = 0
    for line in f:
        vards,vecums = line.strip().split(",")
        summa += int(vecums)
        skaits += 1
videjais = summa / skaits
print("Vidējais vecums:", videjais)
