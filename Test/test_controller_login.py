from unittest import TestCase

from Login.Model.login import DataPick


class TestLogin(TestCase):
    def test_loading(self):
        self.utente_pikle = DataPick()
        self.utente_pikle.put_data("az", "az")
        self.assertIsNotNone(self.utente_pikle.lista)

    def test_btn_submit_handler(self):
        self.utente_pikle = DataPick()
        self.utente_pikle.put_data("az", "az")
        self.assertIsNotNone(self.utente_pikle.controlla_login())


