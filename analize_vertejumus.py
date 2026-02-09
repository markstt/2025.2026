""""""
"""📁 Darba noformējums (OBLIGĀTI)

Izveido vienu Python failu ar nosaukumu: treninuzdevums_funkcijas.py

Darbu nosūti uz savu GitHub repository un pēc darba iesniegšanas, uzraksti - iesniegts GitHub un nodot uzdevumu vērtēšanai.

Repository jābūt pieejamam skolotājam

📝 Uzdevuma apraksts
Izveido Python funkciju analize_vertejumus, kas:

Funkcijas prasības:
saņem sarakstu ar skolēnu vērtējumiem (skaitļi);

aprēķina:

vērtējumu skaitu,

vidējo vērtējumu,

augstāko vērtējumu;

nosaka teksta novērtējumu:

ja vidējais ≥ 7 → "labi"

ja vidējais ≥ 4 → "vidēji"

citādi → "jāuzlabo"

atgriež vārdnīcu (dictionary) ar rezultātiem.

Pārbaudi izveidotās funkcijas darbību!"""
""

def analize_vertejumus(vertejumi):# Funkcija, kas analizē skolēnu vērtējumus
    skaits = 0
    summa = 0
    augstakais = vertejumi[0]

    for v in vertejumi:# Cikls, kas skstas cauri vērtējumiem
        skaits += 1
        summa += v
        if v > augstakais:
            augstakais = v

    videjais = summa / skaits

    if videjais >= 7:# Nosaka teksta novērtējumu
        vertejums = "labi"
    elif videjais >= 4:# Nosaka teksta novērtējumu
        vertejums = "vidēji"
    else:# Nosaka teksta novērtējumu
        vertejums = "jāuzlabo"

    rezultats = {
        "skaits": skaits,
        "videjais": videjais,
        "augstakais": augstakais,
        "vertejums": vertejums
    }# Sagatavo rezultātu vārdnīcu

    return rezultats# Atgriež rezultātu vārdnīcu


dati = [6, 8, 7, 9]
rez = analize_vertejumus(dati)
print(rez)
