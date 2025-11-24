"""
Zadanie 4. Wyszukaj książki autora
Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, które zostały
napisane przez Twojego ulubionego autora.

"""

import sqlite3

conn = sqlite3.connect("biblioteka.db")
c = conn.cursor()

c.execute("SELECT tytul, autor, rok_wydania FROM ksiazki WHERE autor = ?", ("Andrzej Sapkowski",))
sapkowski = c.fetchall()

print(sapkowski)

conn.close()