class Brano():
    def __init__(self, nome, artista, album, contatore, id):
        super(Brano, self).__init__()
        self.nome = nome
        self.artista = artista
        self.album = album
        self.contatore = contatore
        self.id = id