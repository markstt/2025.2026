#27/01/2026

"""📌 Tēmas
Numbers & Strings

Lists


📝 Uzdevumi
🔢 1. Numbers & Strings (≈5 min)
Definē divus skaitļu mainīgos:

vienu int

vienu float

Aprēķini šo skaitļu summu.

Izvadi rezultātu divos veidos:

vienkārši ar print()

izmantojot teksta paskaidrojumu (string + skaitļi)

Definē teksta mainīgo (string).

Izvadi:

teksta garumu

pirmo simbolu

tekstu apgrieztā secībā

📋 2. Lists (≈5 min)
Izveido sarakstu (list) ar vismaz 5 elementiem
(drīkst būt dažādi datu tipi).

Izvadi:

visu sarakstu

pirmo elementu

pēdējo elementu

Pievieno sarakstam vienu jaunu elementu.

Nomaini vienu esošu elementu sarakstā.

Izvadi saraksta elementu skaitu.

📚 3. Dictionary (≈5 min)
Izveido vārdnīcu (dictionary) ar informāciju par sevi, piemēram:

vārds

vecums

pilsēta

Izvadi katru vērtību atsevišķi, izmantojot atslēgas.

Pievieno vārdnīcai jaunu atslēgu.

Izmanto un izvada:

.keys()

.values()

⭐ Papildu prasības (svarīgi)
Kods ir saprotams un kārtīgs

Izmanto komentārus (#), lai paskaidrotu, ko dara katra koda daļa

Programmai jāpalaižas bez kļūdām"""

#📝 Uzdevumi
#🔢 1. Numbers & Strings (≈5 min)
#Definē divus skaitļu mainīgos:
#vienu int
#vienu float
#Aprēķini šo skaitļu summu.
#Izvadi rezultātu divos veidos:
#vienkārši ar print()
#
# izmantojot teksta paskaidrojumu (string + skaitļi)
#Definē teksta mainīgo (string).
#Izvadi:
#teksta garumu
#pirmo simbolu
#tekstu apgrieztā secībā


#skaitlis1 ir vesels skaitlis
#skaitlis2 ir decimālskaitlis

skaitlis1 = 5
skaitlis2 = 4.3
summa = skaitlis1 + skaitlis2
print(skaitlis1)
print(skaitlis2)
print("Divu skaitļu summa ir " + str(summa))

teksts ="Hi world"
print(teksts)
print(len(teksts))
print(teksts[0])
print(teksts[::-1])

#Izveido sarakstu (list) ar vismaz 5 elementiem
#drīkst būt dažādi datu tipi).
#Izvadi:
#isu sarakstu
#prmo elementu

#pedejo elementu

#pievieno sarakstam vienu jaunu elementu.

#nomaini vienu esošu elementu sarakstā.

#Izvadi saraksta elementu skaitu.
saraksts = [1, "teksts", 3.14, "BMW", 1, 2, 3]
print(saraksts)
print(saraksts[0])