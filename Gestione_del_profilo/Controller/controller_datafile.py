from Login.controller.controller_login import Login


class controller_utente():

    def __init__(self):
        self.log = Login()
        self.account = self.log.return_credenziali()


