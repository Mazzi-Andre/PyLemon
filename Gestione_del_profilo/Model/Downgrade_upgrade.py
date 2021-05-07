import Verifica_credenziali

class Downgrade_upgrade:

    def __init__(self, username, password):
        super(Downgrade_upgrade, self).__init__()
        self.username = username
        self.password = password

    verifica = Verifica_credenziali.verifica_credenziali
    def upgrade_artista(self, verifica, username, password): #scelta la prendo dalla view quindi dal tipo di tasto cliccato
        if verifica is True:
