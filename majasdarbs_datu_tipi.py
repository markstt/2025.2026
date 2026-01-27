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
saraksts = [1, "teksts", 3.14, "BMW", 1, 2, 3]#saraksts
print(saraksts)
print(saraksts[0])#pirmas elements
print(saraksts[-1])#izvadu pedejo elementu
saraksts.append(input("Pieveino jaunu elementu:"))#pievieno sarakstam vienu jaunu elementu.
print(saraksts)
saraksts[2] = "Audi"  #nomaini vienu esošu elementu sarakstā.
print(saraksts)
print(len(saraksts))#Izvadi saraksta elementu skaitu.

#📚 3. Dictionary (≈5 min)
#zveido vārdnīcu (dictionary) ar informāciju par sevi, piemēram:
#vārds
#vecums
#pilsēta
#Izvadi katru vērtību atsevišķi, izmantojot atslēgas.
#Pievieno vārdnīcai jaunu atslēgu.
#Izmanto un izvada:
#.keys()
#.values()

informacija = {"vards": "Marks", "vecums": 16 , "pilseta":"Viļani" }
print(informacija)
print(informacija["vards"])#Izvadi katru vērtību atsevišķi, izmantojot atslēgas.
print(informacija["vecums"])#Izvadi katru vērtību atsevišķi, izmantojot atslēgas.
print(informacija["pilseta"])#Izvadi katru vērtību atsevišķi, izmantojot atslēgas.

informacija["hobijs"] = "sports"#Pievieno vārdnīcai jaunu atslēgu.
print(informacija)
print("Atslegas:", informacija.keys())#Izmanto un izvada: keys
print("Vertibas:", informacija.values())#Izmanto un izvada: values


"""⭐ Izaicinājums: Datu tipu apvienošana
Izveido sarakstu (list), kurā atrodas:

vismaz viens skaitlis

viens teksts

viena vārdnīca (dictionary)

Piemērs (drīkst veidot arī citādi):

 
dati = [5, "Python", {"kurss": "Programmēšana"}]
Izvadi:

visu sarakstu

katru elementu atsevišķi

🔄 Darbs ar datiem
No vārdnīcas, kas atrodas sarakstā:

izvada vienu vērtību, izmantojot atslēgu

Pievieno vārdnīcai jaunu atslēgu–vērtību pāri.

🧠 Teksta apstrāde
Izmantojot tekstu no saraksta:

nosaki teksta garumu

izvada tekstu ar lielajiem burtiem

izvada tekstu apgrieztā secībā
"""

saraksts1 = [16 , "Māja", {"pilseta": "Vilani"}] #Izveido sarakstu (list), kurā atrodas:
print(saraksts1) # izvads
print(saraksts1[0])#katru elementu atsevišķi
print(saraksts1[1])#katru elementu atsevišķi
print(saraksts1[2])#katru elementu atsevišķi
print(saraksts1[2]["pilseta"])#izvada vienu vērtību, izmantojot atslēgu
saraksts1[2]["atrasana"] = "Latvija" #Pievieno vārdnīcai jaunu atslēgu–vērtību pāri.
print(saraksts1)
"""🧠 Teksta apstrāde
Izmantojot tekstu no saraksta:

nosaki teksta garumu

izvada tekstu ar lielajiem burtiem

izvada tekstu apgrieztā secībā
"""
teksts = saraksts1[1]#izvada tekstu apgrieztā secībā
print("Teksta garums:", len(teksts))#nosaki teksta garumu
print("Lielie burti;", teksts.upper())#izvada tekstu ar lielajiem burtiem
print("Apgrieztais:", teksts[::-1])#izvada tekstu apgrieztā secībā