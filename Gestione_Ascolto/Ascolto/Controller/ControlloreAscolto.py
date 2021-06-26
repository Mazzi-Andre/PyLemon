import pathlib

from Gestione_Ascolto.Ascolto.Model.Ascolto import Ascolto
from Pubblicazione.Controller.Gestione_json import Gestione_json

class ControlloreAscolto():

    def __init__(self):
        #self.controller = Ascolto()
        self.G_json = Gestione_json()
        #self.path = ''


    def getPath(self, titolo, album): # che saranno item
        id = self.G_json.ricerca_id(titolo, album)
        path = "Data/mp3/"+str(id)+".mp3"
        return path

    def getObject(self):
        return self.G_json.get_jsonobject()
