"""
Stwórz klasę RejestracjaUzytkownika. W konstruktorze init przyjmuj email i haslo.
Wewnątrz konstruktora dodaj walidację:
Sprawdź, czy email zawiera znak @ . Jeśli nie, podnieś wyjątek ValueError z
odpowiednim komunikatem.
Sprawdź, czy haslo ma co najmniej 8 znaków. Jeśli nie, podnieś ValueError. Użyj bloku
try...except, aby przetestować tworzenie obiektów z poprawnymi i niepoprawnymi
danymi. (challenge)

"""

class RejestracjaUzytkownika:
    def __init__(self, email, haslo):
        if "@" in email:
            self.email = email
        else:
            raise ValueError("email musi zaierać znak @")
        if len(haslo) >= 8:
            self.haslo = haslo
        else:
            raise ValueError("hasło musi zawierać coanjmniej 8 znakó")

try:
    user1 = RejestracjaUzytkownika("email.pl", "haslo")
    print(user1.email)
    print(user1.haslo)
except:
    user1 = RejestracjaUzytkownika("email@.pl", "haslohaslo")
    print(user1.email)
    print(user1.haslo)
