"""
Zadanie 4. Średnia cena książki
Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG().

"""

import sqlite3

conn = sqlite3.connect("lesson14.db")
c = conn.cursor()

kategoria = 'Książki'

querry = '''
SELECT AVG(cena)
FROM Produkty
JOIN Kategorie ON Produkty.id_kategorii = Kategorie.id_kategorii
WHERE Kategorie.nazwa_kategorii = ?'''

parameter = (kategoria,)
c.execute(querry, parameter)

avg = c.fetchall()

print(f'Średnia cena produktów z kategorii Książki to: {avg[0][0]:.2f} zł')

conn.close()