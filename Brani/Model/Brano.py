class Brano():
    def __init__(self, nome, artista, album, genere, contatore, id):
        super(Brano, self).__init__()
        self.nome = nome
        self.artista = artista
        self.album = album
        self.genere = genere
        self.contatore = contatore
        self.id = id