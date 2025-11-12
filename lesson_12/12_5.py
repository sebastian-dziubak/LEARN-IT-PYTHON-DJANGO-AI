"""
Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. Użyj bloku
try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat
użytkownikowi.

"""

try:
    plik = open("nieistniejacy.txt", "r", encoding="utf-8")
    text = plik.read()
except FileNotFoundError:
    print(f"Plik o podanej nazwie nie istnieje")