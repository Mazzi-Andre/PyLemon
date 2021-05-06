import os
import pickle

class EliminazioneAccount():

    def __init__(self, username, password):
        super(EliminazioneAccount, self).__init__()
        self.username = username
        self.password = password


    def verifica(self, username, password):
        if username == controller_andre.username #controllore_andre.username me lo passerà andre dal pickle
                if password == controller_andre.password #controllore_andre.password me lo passerà andre da pickle
                    verifica = True
                    return verifica
        verifica = False
        return verifica

    """def rimozione_accont(self, verifica):
        def selected_profilo(self, registrazione, username):
            if verifica is True:
                if  registrazione.username == username:
                    return True
                return False
            self.registrazione.lista_profili.remove(list(filter(selected_profilo, self)))"""""

    def rimozione_accont(self, verifica):
        if verifica is True:
            def selected_profilo(self, registrazione, username):
                if registrazione.username == username:
                    return True
                return False
            self.registrazione.lista_profili.remove(list(filter(selected_profilo, self)))
