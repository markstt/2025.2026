#27/01/2026

#Dictionary - vārdnīcas
#Python datu tips: Dictionary - vardnica/ biblioteka
"""
✍️ Praktiskais uzdevums
Izveido vārdnīcu par sevi (iekļauj: vārds, vecums un iegūtā izglītība (pamatskolas, vidusskolas, augstākā un t.t.))
Izvadi izveidoto vārdnīcu

Izvadi vārdnīcas atslēgas
Izvadi vārdnīcas atslēgu vērtības

Izmanto .keys() un .values()

Iedomājies, ka jau esi nosvinējis dzimšanas dienu un maini vērtību atslēgā vecums
Izvadi visu vārdnīcu
Izvadi tikai atslēgas vecums vērtību
"""
#saraksts[]
#vardnica/biblioteka{}
#atslegas:vertibas
#datu pieiešana izmantojot atslēga
informacija = {"vards": "Marks" , "vecums": 16, "izglitiba": "vidusskola"}
print(informacija)
#Izvadi vārdnīcas atslēgas
#Izvadi vārdnīcas atslēgu vērtības

#Izmanto .keys() un .values()


print(informacija.keys())
print(informacija.values())
#Iedomājies, ka jau esi nosvinējis dzimšanas dienu un maini vērtību atslēgā vecums
#Izvadi visu vārdnīcu
informacija["vecums"] = 17
print(informacija)
#Izvadi tikai atslēgas vecums vērtību
print(informacija["vecums"])