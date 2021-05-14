
import Gestione_json

class ControlloreContenuti():

    def __init__(self):
        self.contenuti = {}
        self.Gestione_contenuti = Gestione_json()
        self.contenuti = self.Gestione_contenuti.getLettura()
        
    def getLista(self):
        return self.contenuti