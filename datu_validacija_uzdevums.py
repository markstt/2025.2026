#27.04.2026

"""nosacījumi
📝 Uzdevums
Izveido programmu, kas:

prasa lietotājam ievadīt vārdu
pārbauda:
vai ievade nav tukša
vai sākas ar lielo burtu
izvada:
“OK” vai
“Nepareiza ievade”
Faila nosaukums: datu_validacija_uzdevums.py
Pēc darba izpildes: Nosūtīt uz GitHub

💡 Padoms skolēniem
izmanto:
 
len(vards)
vards[0].isupper()

"""

vards = input("Ievadi vardu,tikai ar lielo burtu: ")#prasa lietotājam ievadīt vārdu 
len_vards = len(vards)#parbaudam vai ievade nav tukša
if len_vards ==0:#ja ievade ir tukša 
    print("Nepareiza Ievade")#izvada Nepareiza Ievade
elif vards[0].isupper():#parbaudam vai vards sakas ar lielo burtu
    print("OK")#ja sakas ar lielo burtu izvada OK
else:
    print("Nepareiza Ievade")#ja nesakas ar lielo burtu izvada Nepareiza Ievade
