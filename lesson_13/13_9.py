"""
Zadanie 9. Dokonaj przypisań
Napisz skrypt, który dokona przypisań. Dla każdego studenta z tabeli studenci dodaj wpis
do tabeli przypisania, łącząc go z jednym z audytoriów.

"""

import sqlite3

conn = sqlite3.connect("uczelnia.db")
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS przypisania (
          id_przypisania INTEGER PRIMARY KEY,
          id_studenta INTEGER,
          id_audytorium INTEGER,
          FOREIGN KEY (id_studenta) REFERENCES studenci(id_studenta),
          FOREIGN KEY (id_audytorium) REFERENCES audytoria(id_audytorium))          
''')

c.execute("INSERT INTO przypisania (id_studenta, id_audytorium) VALUES (?, ?)", (1, 3))
c.execute("INSERT INTO przypisania (id_studenta, id_audytorium) VALUES (?, ?)", (2, 2))
c.execute("INSERT INTO przypisania (id_studenta, id_audytorium) VALUES (?, ?)", (3, 1))
c.execute("INSERT INTO przypisania (id_studenta, id_audytorium) VALUES (?, ?)", (4, 3))

conn.commit()
conn.close()