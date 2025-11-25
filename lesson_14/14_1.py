"""
Zadanie 1. Liczba produktów
Napisz skrypt, który połączy się z bazą sklep.db i policzy, ile jest wszystkich produktów w
tabeli Produkty. Użyj funkcji COUNT().

"""

import sqlite3

conn = sqlite3.connect("lesson14.db")
c = conn.cursor()

querry = '''
SELECT COUNT(id_produktu) FROM PRODUKTY
'''
c.execute(querry)
produkty = c.fetchall()
print(f"Wszystkich produktów w tabeli Produkty jest {produkty[0][0]}")

conn.close()