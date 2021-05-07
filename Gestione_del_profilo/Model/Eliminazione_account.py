import os
import pickle
import Verifica_credenziali

class EliminazioneAccount():

    def __init__(self, username, password):
        super(EliminazioneAccount, self).__init__()
        self.username = username
        self.password = password


    """def rimozione_accont(self, verifica):
        def selected_profilo(self, registrazione, username):
            if verifica is True:
                if  registrazione.username == username:
                    return True
                return False
            self.registrazione.lista_profili.remove(list(filter(selected_profilo, self)))"""""

    verifica = Verifica_credenziali.verifica_credenziali
    def rimozione_accont(self, verifica):
        if verifica is True:
            def selected_profilo(registrazione, username):
                if registrazione.username == username:
                    return True
                return False
            self.registrazione.lista_profili.remove(list(filter(selected_profilo, self))[0])
        print("Username o password errati.")