"""
Zadanie 6. Produkty droższe od średniej
Napisz skrypt, który wyświetli nazwy i ceny wszystkich produktów, których cena jest wyższa
niż średnia cena wszystkich produktów w sklepie. Wykorzystaj podzapytanie.

"""

import sqlite3

conn = sqlite3.connect("lesson14.db")
c = conn.cursor()

querry = '''
SELECT nazwa_produktu, cena
FROM Produkty
WHERE cena > (SELECT AVG(cena) FROM Produkty)
'''

c.execute(querry)
produkty = c.fetchall()

print('Produkty, których cena jest wyższa niż średnia cena wszystkich produktów w sklepie:')
for row in produkty:
    print(f'* {row[0]} - {row[1]} zł')