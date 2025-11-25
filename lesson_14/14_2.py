"""
Zadanie 2. Najdroższy produkt
Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji
MAX().

"""

import sqlite3

conn = sqlite3.connect("lesson14.db")
c = conn.cursor()

querry = '''
SELECT nazwa_produktu, cena
FROM Produkty
WHERE cena = (SELECT MAX(cena) FROM Produkty)
'''

c.execute(querry)
max = c.fetchall()

print(f"Najdroższy produkt to: {max[0][0]} i kosztuje {max[0][1]:.2f} zł")

conn.close()
