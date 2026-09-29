def aprekinat_piegades_cenu(svars):
    if svars <= 0:
        return "Nepareizs svars"
    elif svars <= 1:
        return 3
    elif svars <= 5:
        return 5
    elif svars <= 10:
        return 8
    else:
        return 12

ievade = input("Ievadi sūtījuma svaru kg: ")
try:
    svars = float(ievade)
    cena = aprekinat_piegades_cenu(svars)
    if isinstance(cena, (int, float)):
        print("Piegādes cena:", cena, "€")
    else:
        print(cena)
except ValueError:
    print("Nepareizs svars")

"""Programmas specifikācija
•	Svars jāievada kilogramos.
•	0 kg vai mazāk → “Nepareizs svars”.
•	Vairāk par 0 un līdz 1 kg → 3 €.
•	Vairāk par 1 un līdz 5 kg → 5 €.
•	Vairāk par 5 un līdz 10 kg → 8 €.
•	Vairāk par 10 kg → 12 €.
•	Ja ievade nav skaitlis → “Nepareizs svars”.
"""