#1. uzdevums (2 punkti)
#Izskaidro:

##a) Kāpēc programmatūras izstrādē ir nepieciešama prasību specifikācija?

#b) Kas var notikt, ja kods tiek rakstīts bez skaidras specifikācijas?#

"""2. uzdevums (3 punkti)
Atzīmē pareizos apgalvojumus:

☐ Komentāri programmā ietekmē programmas izpildes ātrumu
☐ Koda pieraksta stils palīdz citiem saprast programmu
☐ Cikls palīdz izvairīties no koda dublēšanas
☐ Versiju vadības sistēma saglabā tikai gala versiju
☐ Sintakses kļūda neļauj programmai darboties
☑ Koda pieraksta stils palīdz citiem saprast programmu
☑ Cikls palīdz izvairīties no koda dublēšanas
☑ Sintakses kļūda neļauj programmai darboties
"""

"""3. uzdevums (3 punkti)
Sakārto programmatūras dzīves cikla posmus pareizā secībā:

Testēšana
Plānošana
Uzturēšana
Izstrāde
Analīze

Īsi paskaidro jebkurus divus no tiem.

Plānošana - Tu sac domat ko tu gribi no sava projetka
Izstrāde
Testēšana - tu parbaudi vai sanaca kaut kas
Analīze
Uzturēšana
"""

"""Dots apraksts:

Programmētājs saglabā katru koda versiju, var atgriezties pie iepriekšējās versijas un strādāt komandā ar citiem.

a) Kādu rīku viņš izmanto? git
b) Kādas ir 2 priekšrocības šim rīkam? var atgriezties ja kaut kas nesanaks"""

#6 uzd . a variants

vecums = int(input("Ievadi savu vecumu:"))#ievada skaitlu
print("Tev ir", vecums, "gadi")



skaitlis = int(input("Ievadi skaitli: "))
if skaitlis >= 10:#nebija int
    print("Lielāks par 10")#nav atstarpes
else: # nav divpunktes
  print("Mazāks vai vienāds ar 10")

def kvadrats(skaitlis):
   

   return skaitlis * skaitlis
# Lietotājs ievada skaitli
skaitlis = int(input("Ievadi skaitli: "))

# Funkcijas izsaukšana
rezultats = kvadrats(skaitlis)

# Rezultāta izdrukāšana
print("Kvadrāts ir:", rezultats)

atzime = int(input("Ievadi savu atzimi:"))#cilveks ievada skaitli
if atzime >= 90:#parbauda to
   print("Izcili")
elif atzime >= 70:
   print("Labi")
else:
   print("Jauzlabo")# ja nav 2 augseji varianti tad trešais