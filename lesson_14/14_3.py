"""
Zadanie 3. Suma wartości
Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". Użyj funkcji
SUM() oraz klauzuli WHERE z JOIN.

"""

import sqlite3

conn = sqlite3.connect("lesson14.db")
c = conn.cursor()

kategoria = 'Elektronika'

querry = '''
SELECT SUM(cena)
FROM Produkty
JOIN Kategorie ON Produkty.id_kategorii = Kategorie.id_kategorii
WHERE Kategorie.nazwa_kategorii = ?
'''

parameter = (kategoria,)
c.execute(querry, parameter)

suma = c.fetchall()

print(f'Suma cen produktów z kategorii Elektronika wynosi {suma[0][0]:.2f} zł')

conn.close()