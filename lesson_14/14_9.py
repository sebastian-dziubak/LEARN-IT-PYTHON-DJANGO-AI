"""
Zadanie 9. Funkcja do wyszukiwania produktów
Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje
jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich
produktów w tej kategorii.

"""

def znajdz_produkty_w_kategorii(nazwa_kategorii):
    import sqlite3

    conn = sqlite3.connect("lesson14.db")
    c = conn.cursor()

    querry = '''
    SELECT nazwa_produktu, cena
    FROM Produkty
    JOIN Kategorie ON Produkty.id_kategorii = Kategorie.id_kategorii
    WHERE nazwa_kategorii = ?
    '''
    c.execute(querry,(nazwa_kategorii,))
    return c.fetchall()

print(znajdz_produkty_w_kategorii("Książki"))