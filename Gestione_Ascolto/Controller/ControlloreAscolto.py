from Pubblicazione.Controller.Gestione_json import Gestione_json

'''classe di controllo delle funzionaità di ascolto'''
class ControlloreAscolto():

    ''' Nel costruttore si crea un oggetto della classe Gestione_json
        responsabile della lettura e della gestione del file info_brani.json. '''
    def __init__(self):
        self.g = Gestione_json()

    '''Metodo utlizzato per ricavare il percorso file dei brani contenuti in Data/mp3 da riprodurre.
       Come parametri del metodo si passano il titolo e l'album della traccia in considerazione.'''

    def getPath(self, lst_titolo, lst_album): # che saranno item
        id = self.g.ricerca_id(lst_titolo, lst_album)
        path = "Data/mp3/"+str(id)+".mp3"
        return path


    '''Metodo che ritorna la lista conseguente alla lettura del file info_brani.json'''
    def getObject(self):
        return self.g.get_jsonobject()