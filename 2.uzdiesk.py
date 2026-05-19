""""2. uzdevums — Datu validācija (8 p)

2.1. Uzraksti programmu, kas pārbauda, vai ievadītais vārds sākas ar lielo burtu. (5 p)

Pievieno kodu atbilžu laukā"""

vards = input("Ievadi savu vardu:")
len_vards = len(vards)
if len_vards == 0:
    print("Nepareiza izvade")
elif vards[0].isupper():
    print("OK")
else:
    print("Nepareiza izvade")