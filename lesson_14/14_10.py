"""
Zadanie 10. Prosta symulacja ORM
Stwórz klasę Produkt w Pythonie z atrybutami id_produktu, nazwa_produktu i cena.
Następnie napisz funkcję pobierz_wszystkie_produkty(), która połączy się z bazą danych,
pobierze wszystkie produkty i zwróci listę obiektów klasy Produkt. To ćwiczenie pokaże Ci,
jak ORM automatyzuje mapowanie wierszy na obiekty.

"""

class Produkt():
    def __init__(self, id_produktu, nazwa_produktu, cena):
        self.id_produktu = id_produktu
        self.nazwa_produktu = nazwa_produktu
        self.cena = cena
    
    def pobierz_wszystkie_produkty():
        import sqlite3

        conn = sqlite3.connect("lesson14.db")
        c = conn.cursor()
        produkty = []

        c.execute('SELECT id_produktu, nazwa_produktu, cena FROM Produkty')
        rows = c.fetchall()

        for row in rows:
            produkt = Produkt(id_produktu=row[0], nazwa_produktu=row[1], cena=row[2])
            produkty.append(produkt)
        
        conn.close()
        return produkty


produkty = Produkt.pobierz_wszystkie_produkty()
for p in produkty:
    print(p)