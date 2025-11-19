"""
Zadanie 3. Wyświetl całą bibliotekę
Napisz skrypt, który pobierze i wyświetli w konsoli wszystkie książki (wszystkie kolumny) z
tabeli ksiazki.

"""

import sqlite3

conn = sqlite3.connect("biblioteka.db")
c = conn.cursor()

c.execute("SELECT * FROM ksiazki")

all_books = c.fetchall()
for book in all_books:
    print(book)

conn.close()
