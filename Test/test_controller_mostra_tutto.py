from unittest import TestCase

from Gestione_Ascolto.Ascolto.Model.Ascolto import Ascolto
from Pubblicazione.Controller.Gestione_json import Gestione_json


class Testcontroller_mostra_tutto(TestCase):
    def test_mostra_tutto(self):
        self.gestione_json = Gestione_json()
        self.assertIsNotNone(self.gestione_json.get_jsonobject())


    def test_go_play(self):
        self.ascolto = Ascolto()
        self.ascolto.play("Data/mp3/5.mp3", 0.5)


    def test_go_pause(self):
        self.ascolto = Ascolto()
        self.ascolto.pause()

    def test_go_stop(self):
        self.ascolto = Ascolto()
        self.ascolto.stop()



    def test_change_value(self):
        self.ascolto = Ascolto()
        self.ascolto.vol_adjust(0.5)
