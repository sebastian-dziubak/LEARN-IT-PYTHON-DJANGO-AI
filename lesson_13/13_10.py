"""
Zadanie 10. Funkcja wyszukująca z JOIN
Napisz funkcję w Pythonie znajdz_sale_studenta(nazwisko), która przyjmuje nazwisko
studenta jako argument. Funkcja powinna połączyć się z bazą, a następnie znaleźć i
wyświetlić informację, w którym budynku i w jakiej sali znajduje się dany student.

"""

def znajdz_sale_studenta(nazwisko):
    import sqlite3
    conn = sqlite3.connect("uczelnia.db")
    c = conn.cursor()

    querry = ('''
    SELECT s.imie, s.nazwisko, a.nazwa_budynku, a.numer_sali
    FROM studenci AS s
    JOIN przypisania AS p ON s.id_studenta = p.id_studenta
    JOIN audytoria AS a ON p.id_audytorium = a.id_audytorium
    WHERE s.nazwisko = ?''')

    c.execute(querry, (nazwisko,))
    dane_studenta = c.fetchall()
    print(f"Student {dane_studenta[0][0]} {dane_studenta[0][1]} ma egzamin w budynku {dane_studenta[0][2]} w sali numer {dane_studenta[0][3]}")

znajdz_sale_studenta("Rutkowski")