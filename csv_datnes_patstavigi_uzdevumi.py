#29.04.2026
import csv

"""csv_datnes_patstavigi_uzdevumi.py
 
📝 Uzdevums 1
Izveido programmu, kas izvada tikai skolēnus no Jelgavas.

📝 Uzdevums 2
Izvada tikai tos skolēnus, kuri jaunāki par 17 gadiem.

📝 Uzdevums 3 (Cietā rieksta līmenis)
Saskaiti, cik ierakstu ir datnē.

⭐ PAPILDUS UZDEVUMS
Aprēķini vidējo vecumu."""


"""📝 Uzdevums 1
Izveido programmu, kas izvada tikai skolēnus no Jelgavas."""

# csv_datnes_patstavigi_uzdevumi.py

with open("skoleni.csv", encoding="utf-8") as fails:
    next(fails)   # izlaiž virsrakstu

    skaits = 0
    summa_vecums = 0

    print("📝 Uzdevums 1 - Skolēni no Jelgavas:")
    for rinda in open("skoleni.csv", encoding="utf-8"):
        pass

with open("skoleni.csv", encoding="utf-8") as fails:
    next(fails)

    for rinda in fails:
        vards, vecums, pilseta = rinda.strip().split(",")

        if pilseta == "Jelgava":
            print(vards, vecums, pilseta)

print()

print("📝 Uzdevums 2 - Jaunāki par 17 gadiem:")
with open("skoleni.csv", encoding="utf-8") as fails:
    next(fails)

    for rinda in fails:
        vards, vecums, pilseta = rinda.strip().split(",")

        if int(vecums) < 17:
            print(vards, vecums, pilseta)

print()

print("📝 Uzdevums 3 - Ierakstu skaits:")
with open("skoleni.csv", encoding="utf-8") as fails:
    next(fails)

    skaits = 0

    for rinda in fails:
        skaits += 1

print("Ierakstu skaits:", skaits)

print()

print("⭐ PAPILDUS UZDEVUMS - Vidējais vecums:")
with open("skoleni.csv", encoding="utf-8") as fails:
    next(fails)

    summa = 0
    skaits = 0

    for rinda in fails:
        vards, vecums, pilseta = rinda.strip().split(",")
        summa += int(vecums)
        skaits += 1

videjais = summa / skaits
print("Vidējais vecums:", round(videjais, 2))
