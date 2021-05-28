from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Data_Utente.control.Data_control import DataPick
from Gestione_del_profilo.View.Conferma_credenziali_eliminazione import conferma_credenziali


class controller_conferma_credenziali(QtWidgets.QWidget, DataPick, conferma_credenziali):
    switch_window_1 = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()
    switch_window_3 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pick = DataPick()

        self.btn_Back.clicked.connect(self.btn_back_handler)
        self.btn_Ok.clicked.connect(self.btn_ok_handler)




    """POP UP FINESTRA"""

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    """SWITCH FINESTRE"""

    def btn_ok_handler(self):
        self.pop_message(text="Da fare")

    def btn_back_handler(self):

        if self.pick.controlla_login() == 1:
            self.switch_window_1.emit()

        if self.pick.controlla_login() == 2:
            self.switch_window_2.emit()

        if self.pick.controlla_login() == 3:
            self.switch_window_3.emit()