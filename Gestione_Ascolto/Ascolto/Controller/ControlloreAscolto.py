import pathlib

from Gestione_Ascolto.Ascolto.Model.Ascolto import Ascolto
from Pubblicazione.Controller.Gestione_json import Gestione_json

class ControlloreAscolto():

    def __init__(self):
        #self.controller = Ascolto()
        self.g = Gestione_json()
        #self.path = ''


    def getPath(self, lst_titolo, lst_album): # che saranno item
        id = self.g.ricerca_id(lst_titolo, lst_album)
        path = "Data/mp3/"+str(id)+".mp3"
        return path

    def getObject(self):
        return self.g.get_jsonobject()