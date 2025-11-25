"""
Zadanie 8. Kategorie z liczbą produktów
Napisz zapytanie, które wyświetli nazwę każdej kategorii oraz liczbę produktów należących
do tej kategorii. Użyj JOIN, COUNT() oraz GROUP BY.

"""

import sqlite3

conn = sqlite3.connect('lesson14.db')
c = conn.cursor()

querry = '''
SELECT nazwa_kategorii, COUNT(Produkty.id_kategorii)
FROM Kategorie
JOIN Produkty ON Kategorie.id_kategorii = Produkty.id_kategorii
GROUP BY (Produkty.id_kategorii)
'''

c.execute(querry)
result = c.fetchall()

for row in result:
    print(f"Kategoria: {row[0]}, ilość sztuk: {row[1]}")