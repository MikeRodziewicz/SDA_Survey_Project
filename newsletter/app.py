# import smtplib do wysylania mejli oraz klas z pliku obiekty
# TODO testy dla app,py i obiekty.py
# TODO naprawic breaklook i exit func, bo wykonuja program jeszcze jeden raz niepotrzebnie
import smtplib
from newsletter import obiekty
import re

# global zmienne, uzywane przez funkcje
menu = ["1. Add", "2. Show", "3. Send", "4. Exit"]
menu_selection = 0
user = None
game = True
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


# funkcja sprawdzajaca z pomoca regex czy user na pewno podaje poprawnego mejla
def email_validator(a):
    if (re.search(regex, a)):
        return True
    else:
        return False

    # wyswietlanie menu i pobieranie inputu od uzytkownika
def show_menu(a):
    choice = None
    global game
    global menu_selection
    for i in a:
        print(i)
    choice = int(input("Select option "))
    if choice == 1:
        menu_selection = 1
    elif choice == 2:
        menu_selection = 2
    elif choice == 3:
        menu_selection = 3
    elif choice == 4:
        menu_selection = 4
        game = False
    else:
        print("incorrect selection")
    return menu_selection


# uzycie func isalpha - sprawdza czy podane zostaly imiona a nie jakies buble
def add_user_func():
    global user
    while True:
        try:
            user_imie = input("podaj imie: ")
            user_nazwisko = input("podaj nazwisko: ")
            user_email = input("podaj email:  ")
            if email_validator(user_email) == True and user_imie.isalpha() and user_nazwisko.isalpha():
                user = obiekty.User(user_imie, user_nazwisko, user_email)
                return user
                break
            else:
                raise TypeError
        except TypeError:
                print("niepoprawne dane ")
                continue

#TODO dodac opcje uzuwania usera, do tego potrzeba jakis numer ID generowac dla kazdego usera
def remove_user_func():
    pass

# zaciaga z klasy Lista wszystkich dodanych uzytkownikow, jak nie ma zadnych to printuje info
def show_all_users(dist_list):
    if len(dist_list.lista) != 0:
        dist_list.show_users()
    else:
        print("no users in the list")

# iterator for jest po to, zeby pobrac z klasy List, e-mail kazdego dodanego uzytkownika.
# nastepnie z "with" uzywamy metod z tego modulu smtp, ktory importowalismy i w moim przypadku danych gmail.
# monza tez uzyc pewnie innej poczty, albo w ogole mocka ale tego nie ogarnalem.
def send_newsletter(a):
    for item in a.lista_mejli:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo() # to jest jakas metoda na zabezpiecznie polaczenia i szyfrowanie danych
            smtp.starttls() # to jest jakas metoda na zabezpiecznie polaczenia i szyfrowanie danych
            smtp.ehlo() # to jest jakas metoda na zabezpiecznie polaczenia i szyfrowanie danych
            smtp.login("yyy", "xxx") # zamiast y - adres e-mail, zamiast x swoje haslo do tego adresu mejlowego
            subject = "testing 2 mejling" # tytul - mozemy dac dowolny, albo wykorzystac jakas funkcje zeby go dynamicznie generowac
            body = "testujemy mejlowanie z pythona" # tekst - mozemy dac dowolny, albo wykorzystac jakas funkcje zeby go dynamicznie generowac
            msg = f'Subject: {subject}\n\n{body}' # tu tworzymy samego mejla, z subjectu i body, ktore zdefiniowalismy wyzej
            # smtp.sendmail("mike.python.testing@gmail.com", item, msg) # faktycznie wysylanie mejla - pierszy parametr - mejl z jakiego wysylamy, koleny
            # kolejny to adres na ktory wysylamy mejla (dalem item, bo dzieki iteratorowi on bedzie pobieral po jednym adresie z naszej listy
            # a potem jest nasza wiadomos jak ostatni parametr


if __name__ == "__main__":
    newletter_list = obiekty.Lista()
    while game:
        show_menu(menu)
        if menu_selection == 1:
            add_user_func()
            newletter_list.add_user(user)
        elif menu_selection == 2:
            show_all_users(newletter_list)
        elif menu_selection == 3:
            send_newsletter(newletter_list)
        elif menu_selection == 4:
            break
    #
