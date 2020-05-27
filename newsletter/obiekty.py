# pewnie mozna to zrobic z jedna klasa ale chcialem pocwiczyc
# najpierw tworzymy usera zgodnie z tymi wymaganiami, oraz dajemy mu __repr__
# po to, zeby moc wyswietlac dane w naszej funkcji show_all

class User:

    def __init__(self, first_name, last_name, email, active = True):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.active = active

    def __repr__(self):
        return f"Imie: {self.first_name}, Nazwisko: {self.last_name}, e-mail: {self.email}"

# tutaj mamy liste userow, oraz opcje manipulowania nimi, czyli jak przywolujemy funkcje w app.py to
# tak serio uzywamy metod, ktore sa juz wewnatrz klas
class Lista:

    def __init__(self):
        self.lista = []
        self.lista_mejli = []

    def add_user(self, user):
        self.lista.append(user)
        self.lista_mejli.append(user.email)

    def remove_user(self,user):
        self.lista.remove(user)

    def show_users(self):
        for item in self.lista:
            print(item.__repr__())


