class User:

    def __init__(self, first_name, last_name, email, active = True):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.active = active

    def __repr__(self):
        return f"Imie: {self.first_name}, Nazwisko: {self.last_name}, e-mail: {self.email}"


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


