import smtplib
from newsletter import obiekty


menu = ["1. Add", "2. Show", "3. Send", "4. Exit"]
menu_selection = 0
user = None
game = True

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

def add_user_func():
    global user
    user_imie = input("podaj imie: ")
    user_nazwisko = input("podaj nazwisko: ")
    user_email = input("podaj email:  ")
    user = obiekty.User(user_imie,user_nazwisko,user_email)
    return user

def remove_user_func():
    pass

def show_all_users(dist_list):
    if len(dist_list.lista) != 0:
        dist_list.show_users()
    else:
        print("no users in the list")

def send_newsletter(a):
    for item in a.lista_mejli:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login("mike.python.testing@gmail.com", "Sosnowiec!12")
            subject = "testing 2 mejling"
            body = "testujemy mejlowanie z pythona"
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail("mike.python.testing@gmail.com", item, msg)


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

