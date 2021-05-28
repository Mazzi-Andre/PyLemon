from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Data_Utente.control.Data_control import DataPick

from Gestione_del_profilo.View.Home_listener import home_ascoltatore


class controller_ascoltatore(QtWidgets.QWidget, DataPick, home_ascoltatore):
    switch_window_1 = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pick = DataPick()

        self.btn_Impostazioni.clicked.connect(self.btn_Impostazioni_handler)
        self.btn_mostraTutte.clicked.connect(self.btn_MostraTutte_handler)
        self.btn_Logout.clicked.connect(self.btn_LogOut_handler)


    """POP UP FINESTRA"""
    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    """SWITCH FINESTRE"""

    def btn_Impostazioni_handler(self):
        self.switch_window_1.emit()

    def btn_MostraTutte_handler(self):
        self.switch_window_2.emit()

    def btn_LogOut_handler(self):
        self.pop_message(text="Arrivederci ! ")
        self.controller_ascoltatore.close()

    """DA FINIRE"""

    """def bool_search_check(self):
        if len(self.lineEdit.text()) <= 1:
            self.pop_message(text='Inserire un titolo valido')
        else:
            if classeManu.funz is False
                self.pop_message(text='Canzone non trovata')"""





