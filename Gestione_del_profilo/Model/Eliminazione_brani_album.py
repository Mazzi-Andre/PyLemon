import os
import pickle
import shutil


class eliminazione_brani_album:

    def __init__(self, nome_brano, nome_album):
        super(eliminazione_brani_album, self).__init__()
        self.nome_brano = nome_brano
        self.nome_album = nome_album

    def eliminazione_brano(self, nome_brano):
        def selected_brano(brani):
            if brani.nome_brano == nome_brano:
                return True
            return False
        self.lista_brani.remove(list(filter(selected_brano, self.lista_brani))[0]) #lista_brani sarebbe il pickle load cioè la lettura del pickle con dentro i brani
        file_song = '/dove si trova/{}.mp3'.format(nome_brano)
        try:
            os.remove(file_song)
        except OSError as e:
            print("Attenzione file .mp3 non trovato!: {}, {}".format(file_song, e.strerror))



    def eliminazione_album(self, nome_album):
        def selected_album(album):
            if album.nome_album == nome_album:
                return True
            return False
        self.lista_album.remove(list(filter(selected_album, self.lista_album))[0]) #lista_album sarebbe il pickle load cioè la lettura del pickle con dentro gli album
        dir_album = '/dove si trova/nome cartella'
        try:
            shutil.rmtree(dir_album)
        except OSError as e:
            print("La directory non esiste!: {} {}".format(dir_album, e.strerror))
