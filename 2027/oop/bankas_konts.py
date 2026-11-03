"""Izveido Python programmu, kas, izmantojot objektorientēto programmēšanu, modelē bankas kontu kā objektu! Uzdevuma mērķis ir nostiprināt prasmes klases izveidē, konstruktora __init__ un self lietošanā, metožu izstrādē, kuras maina objekta stāvokli, kā arī vienkāršas loģikas izmantošanā, lai novērstu nekorektu darbību. Papildus tiek apgūta ideja par datu sagatavošanu saglabāšanai, pārvēršot objekta datus teksta rindā.

Tev jāizveido programma, kurā bankas konts tiek aprakstīts ar klasi BankasKonts. Programma demonstrē konta darbību: naudas iemaksu, naudas izņemšanu, informācijas attēlošanu un datu sagatavošanu saglabāšanai. Uzdevumā drīkst izmantot if pārbaudi metodē iznemt, bet nav nepieciešami cikli vai sarežģītas datu struktūras – fokuss ir uz OOP pamatiem un stāvokļa maiņu ar metodēm.

;

;

o    atlikums (sākumā vērtība var būt 0.0).

Konstruktorā obligāti jāizmanto self, lai īpašības piesaistītu objektam, piemēram, self.ipasnieks = ipasnieks.
Jāizveido metode paradit_info(), kas izvada konta informāciju saprotamā formā, piemēram, Konta īpašnieks: Anna, Atlikums: 120 EUR.
Jāizveido metode iemaksat(summa), kas palielina atlikums vērtību par norādīto summu.
Jāizveido metode iznemt(summa), kas samazina atlikums vērtību par norādīto summu.
Metodē iznemt(summa) jāiekļauj pārbaude ar if: ja atlikums ir mazāks nekā summa, jāizvada paziņojums “Nepietiek līdzekļu!” un atlikumu nedrīkst mainīt.
Jāizveido metode uz_failu(), kas atgriež teksta rindu formātā ipasnieks;numurs;atlikums.
Jāizveido vismaz 1 bankas konta objekts no klases BankasKonts, piemēram,
mans_konts = BankasKonts("Jānis Bērziņš", "LV123BANK0001", 0.0).
Programmas testēšanai jāizpilda šāds scenārijs (secīgi):
1)      parāda konta informāciju;

2)      iemaksā 100 EUR;

3)      izņem 30 EUR;

4)      mēģina izņemt summu, kas pārsniedz atlikumu (jāparādās paziņojumam);

5)      parāda konta informāciju pēc veiktajām darbībām;

6)      izvada uz_failu() rezultātu.

Programmas beigās jābūt redzamām izvadēm konsolē, lai skolotājs var pārbaudīt
·         sākuma stāvokli;

·         stāvokļa maiņu pēc naudas iemaksas/izņemšanas;

·         kļūdas situāciju;

·         sagatavošanu saglabāšanai.

Rezultāts jāiesniedz kā .py fails (bankas_konts.py) ar pilnu, izpildāmu pirmkodu, kas darbojas bez kļūdām.
 

 

Papildu uzdevumi (3–4 pēc izvēles)

1.       Formatēta izdruka
Pielāgo paradit_info() metodi tā, lai naudas summa tiktu izvadīta ar diviem cipariem aiz komata!

2.       Jauns konts
Izveido otru bankas kontu ar citu īpašnieku un sākuma atlikumu un izpildi ar to tās pašas darbības!

3.       Bonusa metode
Izveido metodi pievienot_bonus(), kas kontam pieskaita 5 EUR!

4.     Objektu neatkarība
Parādi, ka viena konta darbības neietekmē cita konta atlikumu!"""

class BankasKonts:
    def __init__(self, ipasnieks,konta_numurs, atlikums):
        self.ipasnieks = ipasnieks
        self.konta_numurs = konta_numurs
        self.atlikums = atlikums
        
    def paradit_info(self):
        print("Ipašnieks: ", self.ipasnieks)
        print("Konta Numurs: ", self.konta_numurs)
        print("Atlikums: ", self.atlikums)
    def iemaksat(self, summa):
        self.atlikums += summa
        print("Iemaksāta summa:", summa, "EUR")
    
    def iznemt(self, summa):
        if self.atlikums >= summa:
            self.atlikums -= summa
            print("Izņemta summa:", summa, "EUR")
        else:
            print("Nepietiek līdzekļu!")
    def uz_failu(self):
        with open("C:/Users/Marks/Documents/2025.2026/2027/oop/bankas_konts.csv" , "w", encoding="utf-8" ) as fails:
            fails.write(self.ipasnieks + "\n")
            fails.write(self.konta_numurs + "\n")
            fails.write(str(self.atlikums))
mans_konts = BankasKonts("Jānis Bērziņš", "LV123BANK0001", 0.0)
    
print("Konta info")
mans_konts.paradit_info()
print("Iemaksājam naudu")
mans_konts.iemaksat(55.9)
mans_konts.paradit_info()
print("Izmakasajam naudu")
mans_konts.iznemt(15)


mans_konts.iznemt(80)#Meigniam iznemt vairak neka ir konta
mans_konts.paradit_info()
mans_konts.uz_failu()
