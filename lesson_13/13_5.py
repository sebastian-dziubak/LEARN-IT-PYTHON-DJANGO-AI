"""
Zadanie 5. Zaktualizuj rok wydania
Wybierz jedną z dodanych książek i napisz skrypt, który zaktualizuje jej rok_wydania na
inną wartość. Po aktualizacji wyświetl dane tej książki, aby potwierdzić, że zmiana się
powiodła.

"""

import sqlite3

conn = sqlite3.connect("biblioteka.db")
c = conn.cursor()

new_publish_year = 2099

c.execute("UPDATE ksiazki SET rok_wydania = ? WHERE tytul = ?", (new_publish_year, "Pan Tadeusz"))
conn.commit()

c.execute("SELECT * FROM ksiazki WHERE tytul = ?", ("Pan Tadeusz",))
updated_book = c.fetchone()

print(updated_book)

conn.close()

