
import Pubblicazione
from Pubblicazione.Controller.Gestione_JSON import Gestione_JSON


class ControlloreContenuti():

    def __init__(self):
        self.contenuti = {}
        self.Gestione_contenuti = Gestione_JSON()
        self.contenuti = self.Gestione_contenuti.get_jsonobject()
        
    def getLista(self):
        return self.contenuti