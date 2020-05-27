# import smtplib do wysylania mejli oraz klas z pliku obiekty
# TODO testy dla app,py i obiekty.py
import smtplib
from newsletter import obiekty

# global zmienne, uzywane przez funkcje
menu = ["1. Add", "2. Show", "3. Send", "4. Exit"]
menu_selection = 0
user = None
game = True

# wyswietlanie menu i pobieranie inputu od uzytkownika
#TODO lepsze try/except zeby informowac uzytkownia jak zle wybierze
def show_menu(a):
    choice = None
    global game
    global menu_selection
    for i in a:
        print(i)
    try:
        choice = int(input("Select option "))
    except:
        print("incorrect selction")
    if choice == 1:
        menu_selection = 1
    elif choice == 2:
        menu_selection = 2
    elif choice == 3:
        menu_selection = 3
    elif choice == 4:
        game = False
    return menu_selection
# dodac try/except jakby user wpisal glupoty
#TODO lepsze try/except zeby informowac uzytkownia jak zle wybierze
#TODO REGEX zeby sprawdzic czy na pewno user wpisuje swojego mejla
def add_user_func():
    global user
    user_imie = input("podaj imie: ")
    user_nazwisko = input("podaj nazwisko: ")
    user_email = input("podaj email:  ")
    user = obiekty.User(user_imie,user_nazwisko,user_email)
    return user
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
# TODO try/except jakby usera nie bylo, albo nie mial dobrego mejla i cos poszlo nie tak.
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
            smtp.sendmail("mike.python.testing@gmail.com", item, msg) # faktycznie wysylanie mejla - pierszy parametr - mejl z jakiego wysylamy, koleny
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

