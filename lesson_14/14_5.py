"""
Zadanie 5. Lista klientów
Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci.

"""

import sqlite3

conn = sqlite3.connect("lesson14.db")
c = conn.cursor()

querry = '''
SELECT imie, email
FROM Klienci
'''

c.execute(querry)
dane = c.fetchall()

for row in dane:
    print(f"Imię i nazwisko: {row[0]}, adres email: {row[1]}")

conn.close()