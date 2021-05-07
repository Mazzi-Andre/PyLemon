class verifica_credenziali():

    def __init__(self, username, password):
        super(verifica_credenziali, self).__init__()
        self.username = username
        self.password = password


    def verifica(self, username, password):
        if username == controller_andre.username #controllor_andre.username me lo passerà andre dal pickle
                if password == controller_andre.password #controllor_andre.password me lo passerà andre da pickle
                    verifica = True
                    return verifica
        verifica = False
        return verifica