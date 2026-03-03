"""
Kreklu apdruka
Problēma
Draugiem jāaprēķina, cik izmaksās apdrukātu T-kreklu pasūtīšana un piegāde, ņemot vērā, ka cena ir
atkarīga no apdrukas veida un kreklu skaita, bet piegādes maksa ir atkarīga no pasūtījuma summas.


Specifikācija
● Funkcijai pasuti_tkreklus ir trīs parametri saskaņā ar formātu pasuti_tkreklus(skaits, apdruka,
piegade). Parametrs skaits ir vesels skaitlis (pasūtamo kreklu skaits), parametri apdruka un piegade
ir simbolu virknes.
● Parametrs apdruka var būt simbolu virkne, kam atļautas trīs vērtības: TEKSTS, ZIME vai FOTO.
Cena attiecīgi ir 5 EUR, 7 EUR un 20 EUR.
● Parametrs piegade ir Būla tipa mainīgais (True vai False). Ja piegade ir True un kopējā pasūtījuma
summa ir mazāka nekā 50 EUR, par piegādi papildus jāmaksā 15 EUR, ja summa ir 50 EUR vai
vairāk, tad piegāde ir par brīvu.
● Pasūtījumiem, kas pārsniedz 100 EUR, tiek piemērota 5 % atlaide no pasūtījuma summas"""
#Funkcijas definēšana ar parametriem skaits ir vesels skaitlis (pasūtamo kreklu skaits)

