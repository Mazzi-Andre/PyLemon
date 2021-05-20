class ControllerBrano():
    def __init__(self, brano):
        super(ControllerBrano, self).__init__()
        self.model = brano()

    def get_nome_brano(self):
        return self.model.nome

    def get_artista_brano(self):
        return self.model.artista

    def get_album_brano(self):
        return self.model.btn_album

    def get_contatore_brano(self):
        return self.model.contatore

    def get_id_brano(self):
        return self.model.id


