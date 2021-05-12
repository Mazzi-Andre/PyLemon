#import Brani

class ListaBraniPubblicazione():
    def __init__(self):
        super(ListaBraniPubblicazione, self).__init__()
        self.lista_brani = []

    def get_lista_brani_by_index(self,index):
        return self.lista_brani[index]

    def get_lista_brani(self):
        return self.lista_brani
