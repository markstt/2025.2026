#27.10.2026

class Kontakts:
    def __init__(self, vards, uzvards, talrunis,epasts):
        self.vards = vards
        self.uzvards = uzvards
        self.talruins = talrunis
        self.epasts = epasts
    def mainit_numuru(self):
        self.talruins == ""
        #Jāmaina vienas kontaktpersonas tālruņa numurs, piešķirot jaunu vērtību īpašībai talrunis, piemēram, kontakts1.talrunis = "26999999".
    def paradit_informaciju(self):
        print("Vards: ",  self.vards)       
        print("Uzvards: ",  self.uzvards)  
        print("Talrunis: ",  self.talruins)  
        print("Epasts: ",  self.epasts)  
"""Izveido Python programmu “Telefona grāmatiņa”, kas izmanto objektorientēto programmēšanu, lai modelētu kontaktpersonu ierakstus kā objektus. Uzdevuma mērķis ir apgūt klases izveidi, konstruktora __init__ un self lietošanu, objektu izveidi, kā arī īpašību nolasīšanu un mainīšanu, vienlaikus pārbaudot objektu neatkarību.

Tev jāizveido programma, kurā katra kontaktpersona tiek aprakstīta ar klasi Kontakts. Programma demonstrē vismaz divu kontaktu izveidi un to datu apstrādi.

Programmai jāveic šādas darbības.

Jāizveido Python fails ar nosaukumu telefona_gramatina.py.
Jāizveido klase Kontakts, kurai ir konstruktors __init__, un tajā jādefinē 3 īpašības:
vards;
uzvards;
talrunis.
Konstruktorā obligāti jāizmanto self, lai īpašības piesaistītu objektam, piemēram, self.vards = vards.
Jāizveido vismaz 2 objekti (kontaktpersonas) no klases Kontakts, piemēram,
kontakts1 = Kontakts("Jānis", "Bērziņš", "26123456");
kontakts2 = Kontakts("Anna", "Kalniņa", "29876543").
Jānolasa un jāizvada kontakpersonu īpašības, izmantojot punktu (.) notāciju: katrai kontakpersonai jāizvada vārds, uzvārds un tālrunis.
Jāmaina vienas kontaktpersonas tālruņa numurs, piešķirot jaunu vērtību īpašībai talrunis, piemēram, kontakts1.talrunis = "26999999".
Pēc izmaiņām atkārtoti jāizvada informācija par šo kontaktpersonu, lai redzētu, ka numurs ir mainījies.
Jāpārbauda objektu neatkarība: jāizvada otras kontaktpersonas dati un jāparāda, ka tie nav mainījušies pēc pirmās kontaktpersonas tālruņa numura maiņas.
Programmas beigās jābūt vismaz 3 izvadēm (pirms izmaiņām, pēc izmaiņām, neatkarības pārbaude), lai skolotājs var redzēt darbību secību un rezultātu.

Programmas piemērs līdz šim punktam pieejams augstāk.

Izveidot metodi mainit_numuru()
Izveidot metodi paradit_informaciju()
Pārbaudīt abu metožu darbību
Rezultāts jāaizsūta uz GitHub, faila nosaukums (telefona_gramatina.py) ar pilnu, izpildāmu pirmkodu, kas darbojas bez kļūdām. """
#Jānolasa un jāizvada kontakpersonu īpašības, izmantojot punktu (.) notāciju: katrai kontakpersonai jāizvada vārds, uzvārds un tālrunis.
kontakts1 = Kontakts("Jānis", "Bērziņš", "26123456", "janiisberzins@gmail.com")
print( kontakts1.vards)
print(kontakts1.uzvards)
print(kontakts1.talruins)
kontakts1.talruins = 26999999
print(kontakts1.talruins)
kontakts1.epasts = "janiskalnins@gmail.com"
kontakts2 = Kontakts("Anna", "Kalniņa", "29876543", "anna.kalnina@gmail.com")
print(kontakts2.vards)
print(kontakts2.uzvards)
print(kontakts2.talruins)
print("Jaunks konta numurs", kontakts1.mainit_numuru())
print("Pirma konta info")
kontakts1.paradit_informaciju()
print("Otra konta info")
kontakts2.paradit_informaciju()

