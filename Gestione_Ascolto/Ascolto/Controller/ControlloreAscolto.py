import pathlib

from Gestione_Ascolto.Ascolto.Model.Ascolto import Ascolto
from Pubblicazione.Controller.Gestione_json import Gestione_json

class ControlloreAscolto():

    def __init__(self):
        #self.controller = Ascolto()
        self.g = Gestione_json()


    def getPath(self, lst_titolo, lst_album): # che saranno item
        id = self.g.ricerca_id(lst_titolo, lst_album)
        path = f"{pathlib.Path().parent.absolute()}\Data\mp3\{id}.mp3"
        return path