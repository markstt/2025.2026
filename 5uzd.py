""""5.1. Uzraksti programmu, kas pārbauda, vai “Laura” ir sarakstā. (3 p)

names = ["Anna", "Laura", "Marta"]

5.2. Paskaidro, kāpēc programmām ar miljoniem datu nepieciešami efektīvi algoritmi. (2 p)

5.3. Uzraksti programmu, kas CSV failā atrod cilvēku ar vecumu 20. (3 p)

Lūdzu ievieto kodus atbilžu laukā."""
#5.1
names = ["Anna", "Laura", "Marta"]
if "Laura" in names:
    print("ir")
else:
    print("nav atarast")

#5.2 lai vieglak butu apstradat tos datus

#5.3
with open("dati_ieskaite.csv", encoding="utf-8") as f:
    next(f)
    for line in f:
        vards,vecums = line.strip().split(",")
        if int(vecums) >= 20:
            print(vards)