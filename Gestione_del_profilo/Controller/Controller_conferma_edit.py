from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Gestione_del_profilo.Model.Gestione_profilo import DataPick
from Gestione_del_profilo.View.Conferma_credenziali_eliminazione import conferma_credenziali


'''----------Classe controller view conferma edit--------'''

class controller_conferma_edit(QtWidgets.QWidget,conferma_credenziali):
    switch_window_1 = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()
    switch_window_3 = QtCore.pyqtSignal()
    switch_window_4 = QtCore.pyqtSignal()
    switch_window_5 = QtCore.pyqtSignal()


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pick = DataPick()

        myData = self.pick.return_credenziali()

        self.username = myData[5]
        self.password = myData[6]

        self.btn_Back.clicked.connect(self.btn_back_handler)
        self.btn_Ok.clicked.connect(self.btn_confirm_handler)



    """POP UP FINESTRA"""

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    """SWITCH FINESTRE"""

    def confronto_credenziali(self):
        username = self.txt_username.text()
        password = self.txt_password.text()

        if username == self.username and password == self.password:
            return True
        else:
            return False




    def btn_confirm_handler(self):
        val = self.confronto_credenziali()
        if (val):

            costante= self.pick.controlla_login()
            if costante == 1:
                self.switch_window_4.emit()
            if costante == 2:
                self.switch_window_5.emit()
            if costante == 3:
                pass


        else:
            self.pop_message("Username o password invalidi ")





    def btn_back_handler(self):

        if self.pick.controlla_login() == 1:
            self.switch_window_1.emit()

        if self.pick.controlla_login() == 2:
            self.switch_window_2.emit()

        if self.pick.controlla_login() == 3:
            self.switch_window_3.emit()