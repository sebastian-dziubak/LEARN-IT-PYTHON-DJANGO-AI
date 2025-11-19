"""
Zadanie 7. Wypełnij dane uczelni
Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. Dodaj co
najmniej 4 studentów i 3 audytoria.

"""

import sqlite3

conn = sqlite3.connect("uczelnia.db")
c = conn.cursor()

students = [
    ("Sebastian", "Dziubak"),
    ("Adam", "Rutkowski"),
    ("Tomasz", "Kowalski"),
    ("Marcin", "Chmielewski")
]

auditories = [
    ("Wydział Inżynierii Mechanicznej", 62),
    ("Instytut Pojazdów i Transportu", 23),
    ("Zakład Silników i Inżynierii Eksploatacji", 68)
]

c.executemany("INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)", students)
c.executemany("INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?, ?)", auditories)

conn.commit()
conn.close()