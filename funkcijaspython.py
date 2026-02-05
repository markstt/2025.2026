#05/02/2026

#funkcijas

#Funkcijas pamatstruktura
#def funkcijas_nosaukums(parametri):
    #darbibas
    #return rezultats
#def - atslegvards funkcijas izveidei
#parametri - dati ko funkcijas saņem
#return - vertiba ko funkcija atgriež(nav obliagti)

#piemers ar skaitliem
def summa(a, b):
    return a+b
rezulatats = summa(2, 7)
print(rezulatats)

#Pieamers ar tekstu
def sveiciens(vards):
    vards = input("Ievadi vardu")
    return "Sveiki, " + vards + "!"

print(sveiciens("Anna"))

#piemers ar list

def elementu_skaits(saraksts):
    skaits = 0
    for elements in saraksts:
        skaits += 1
    return skaits
print(elementu_skaits([3, 5, 7, 8]))

#piemers at dictionary
def vai_ir_atslegas(dati, atslegas):
    if atslegas in dati:
        return "Atslega ir atrasta"
    else:
        return "Atslega nav atrasta"
students = {
"vards": "Janis",
"vecums": 16

}
print(vai_ir_atslegas(students, "vecums"))