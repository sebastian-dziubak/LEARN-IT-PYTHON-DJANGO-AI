"""
Zadanie 2. Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki.
Użyj metody executemany do dodania wszystkich książek za jednym razem.

"""

import sqlite3

conn = sqlite3.connect("biblioteka.db")
c = conn.cursor()

books_to_add = [
    ("Wiedźmin", "Andrzej Sapkowski", 2010),
    ("Pan Tadeusz", "Adam Mickiewicz", 1860),
    ("W pustyni i w puszczy", "Henryk Sieniewicz", 1850)
]

c.executemany("INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?, ?, ?)", books_to_add)

conn.commit()
conn.close()