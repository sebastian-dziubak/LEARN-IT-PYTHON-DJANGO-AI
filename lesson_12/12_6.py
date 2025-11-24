"""
Stwórz własny wyjątek InvalidPasswordError. Następnie napisz funkcję ustaw_haslo(haslo),
która sprawdza, czy hasło ma co najmniej 8 znaków. Jeśli nie, funkcja powinna podnieść
(raise) wyjątek InvalidPasswordError z odpowiednim komunikatem. Napisz kod, który
testuje tę funkcję w bloku try...except.

"""

class InvalidPasswordError(Exception):
    pass


def ustaw_haslo(haslo):
    if len(haslo) >= 8:
        print("Hasło spełnia wymagania bezpieczeństwa")
    else:
        raise InvalidPasswordError ("wpisane hasło jest za którkie. \
Podaj conajmniej 8 znaków")


password = input("Podaj hasło: ")
try:
    ustaw_haslo(password)
except InvalidPasswordError as e:
    print(e)
