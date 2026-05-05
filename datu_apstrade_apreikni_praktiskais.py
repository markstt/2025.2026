#05/05/2026
#praktiskie uzd
"""Izveido failu datu_apstrade_aprekini_prakt_darbs.py
 
📝 Uzdevums 1
Izvada tikai skolēnus ar atzīmi < 7

📝 Uzdevums 2
Aprēķini augstāko atzīmi

📝 Uzdevums 3
Saskaiti, cik skolēniem atzīme ≥ 8

📝 Uzdevums 4
Izveido programmu, kas:

izvada skolēnus virs vidējās atzīmes
💡 Padoms
aprēķini vidējo
vēlreiz pārbaudi datus
Aizsūti izdarīto uz GitHub."""
#1.uzd
with open("klase.csv", encoding="utf-8") as f:
    next(f)
    for line in f:
        vards,atzime = line.strip().split(",")
        if int(atzime) >= 7:
            print(vards)
#2.uzd
lielakatzime = 0
with open("klase.csv", encoding="utf-8") as f:
    next(f)
    for line in f:
        vards,atzime = line.strip().split(",")
        if int(atzime) > lielakatzime:
            lielakatzime = int(atzime)