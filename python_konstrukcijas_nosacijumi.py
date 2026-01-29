#29/01/2026
#Nosacijumi if, elif ,else

vecums = int(input("Ievadi savu vecumu: "))#Datu ievade
#nosacijms
if vecums >= 18:
    print("Tu esi pilngadīgs.")#izpildas ja nosacijums ir patiess
else:
    print("Tu vēl neesi pilngadīgs.")#izpildas ja nosacjiums nav patiess

vards = input("Ievadi savu vārdu: ")
#nosacijums
if vards == "Anna":#salidzinot vertibas jalieto ==
    print("Sveika, Anna!")
else:
    print("Sveiki, lietotāj!")
#piemers ar elif stukturu
atzime = int(input("Ievadi atzīmi (1–10): "))   #Ievade

if atzime >= 9:
    print("Izcili!")
elif atzime >= 6:
    print("Ieskaite")
else:
    print("Nepietiekami")
#ar list
augli = ["ābols", "banāns", "bumbieris"]

izvele = input("Ievadi augļa nosaukumu: ")
#salidzinašana ar katru saraksta elemenetu, izmantojot iebuvetu funkcija

if izvele in augli:
    print("Šis auglis ir sarakstā.")
else:
    print("Šī augļa sarakstā nav.")
#piemers ar vardnicu
skolens = {
    "vards": "Jānis",
    "vecums": 16,
    "klase": "10.A"
}

if skolens["vecums"] >= 18:
    print("Skolēns ir pilngadīgs.")
else:
    print("Skolēns nav pilngadīgs.")

#nosacijumi ar vairakam parbaudem
#1. variants ar logisko operta
lietotajvards = input("Ievadi lietotājvārdu: ")
parole = input("Ievadi paroli: ")

if lietotajvards == "admins" and parole == "1234":
    print("Piekļuve atļauta.")
else:
    print("Nepareizs lietotājvārds vai parole.")
#2. variants ar nosacijumu (nesting)
if lietotajvards == "admins":
    if parole == "1234":
        print("Piekļuve atļauta.")
else:
    print("Nepareizs lietotājvārds vai parole.")
    