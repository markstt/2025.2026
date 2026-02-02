"""Izveido Python programmu, kas:

Pieprasa lietotājam ievadīt:

vārdu

vecumu

iecienītāko programmēšanas valodu

Programma:

pārbauda, vai lietotājs ir pilngadīgs

pārbauda, vai ievadītā programmēšanas valoda ir sarakstā

izvada atbilstošu ziņojumu"""

vards = (input("Ievadi savu vardu:"))#vardu ievadišana
vecums = int(input("Ievadi savu vecumu:"))#vecuma izvadišana
programmesanas_valodas = ["Python", "Java", "C++", "JavaScript"]#programešanas valodas izvele
izvele = input("Izvelies miļako programešanas valodu:")#prog valodas ievade
print("Sveiki,", vards)#izvada Iesveicinašanu un cilveka ievadito vardu

if vecums >= 18:#vecuma parbaude
    print("Tu esi pilngadīgs")#ja ir pilngadīgs
else:
    print("Tu ne esi pilngadīgs")#ja nav pilngadīgs

if izvele in programmesanas_valodas:#parbaude vai prog valoda ir saraksta
    print("Ši ir laba programešanas valoda")
else:
    print("Diemžel šis valodas nav saraksta.")