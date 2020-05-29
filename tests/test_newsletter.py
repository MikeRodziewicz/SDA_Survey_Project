import unittest

from newsletter import obiekty
from newsletter import app

class Test_User(unittest.TestCase):
    def setUp(self):
        self.user = obiekty.User("Michal", "Rodziewicz", "m.rodziew@gmail.com")


    def test_tworzenie(self):
        self.assertEqual("Michal", self.user.first_name)
        self.assertEqual("Rodziewicz", self.user.last_name)
        self.assertEqual("m.rodziew@gmail.com", self.user.email)

    def test_repr(self):
        self.assertEqual("Imie: Michal, Nazwisko: Rodziewicz, e-mail: m.rodziew@gmail.com", self.user.__repr__())


class Test_Lista(unittest.TestCase):
    def setUp(self):
        self.test_lista = obiekty.Lista()

    def test_add_user(self):
        self.user = obiekty.User("Michal", "Rodziewicz", "m.rodziew@gmail.com")
        self.test_lista.add_user(self.user)
        self.assertNotEqual(len(self.test_lista.lista),0)

    def test_remove_user(self):
        self.user = obiekty.User("Michal", "Rodziewicz", "m.rodziew@gmail.com")
        self.test_lista.add_user(self.user)
        self.assertNotEqual(len(self.test_lista.lista), 0)
        self.test_lista.remove_user(self.user)
        self.assertEqual(len(self.test_lista.lista), 0)

class Test_app(unittest.TestCase):
    def setUp(self):
        self.test_name = None
        self.test_surname = None
        self.test_email = None

    def test_email_valid(self):
        pass

    def test_show_menu(self):
        pass

    def test_add_user(self):
        pass

    def test_show_all(self):
        pass

    def test_send_email(self):
        pass

if __name__ == "__main__":
    unittest.main()