"""
Zadanie 7. Zamówienia Anny Nowak
Napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych przez klienta o
imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel: Klienci,
Zamowienia, Zamowienia_Produkty i Produkty.

"""

import sqlite3

conn = sqlite3.connect("lesson14.db")
c = conn.cursor()

klient = "Anna Nowak"

querry = '''
SELECT nazwa_produktu
FROM Produkty
JOIN Zamowienia_Produkty ON Produkty.id_produktu = Zamowienia_Produkty.id_produktu
JOIN Zamowienia ON Zamowienia_Produkty.id_zamowienia = Zamowienia.id_zamowienia
JOIN Klienci ON Zamowienia.id_klienta = Klienci.id_klienta
WHERE Klienci.imie = ?
'''
parameter = (klient,)
c.execute(querry, parameter)
result = c.fetchall()

print(f"Wszystkie produkty {klient}:")
for row in result:
    print(f"* {row[0]}")