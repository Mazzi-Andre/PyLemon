from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Data_Utente.control.Data_control import DataPick
from Gestione_del_profilo.View.Home_label import home_etichetta



class controller_loading(QtWidgets.QWidget, DataPick):
    switch_window_1 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.pick = DataPick()

    """SWITCH FINESTRE"""

    def btn_Ascoltatore_handler(self):
        self.pick.controlla_login()
        self.switch_window_1.emit()

    def btn_Artista_handler(self):
        self.pick.controlla_login()
        self.switch_window_2.emit()

    def btn_Etichetta_handler(self):
        self.pick.controlla_login()
        self.switch_window_3.emit()

