from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Login.Model_.Data_control import DataPick
from Gestione_del_profilo.View.Impostazioni import impostazioni

class controller_impostazioni(QtWidgets.QWidget,impostazioni):
    switch_window = QtCore.pyqtSignal()
    switch_window_1 = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pick = DataPick()
        self.btn_EliminaAccount.clicked.connect(self.btn_elimina_profilo_handler)
        self.btn_EditProfilo.clicked.connect(self.btn_edit_profilo_handler)
        self.btn_rimuovi_brano.clicked.connect(self.btn_rimuovi_brano_handler)



    """POP UP FINESTRA"""

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()


    """SWITCH FINESTRE"""

    def btn_elimina_profilo_handler(self):
        self.switch_window.emit()

    def btn_edit_profilo_handler(self):
        self.switch_window_1.emit()

    def btn_rimuovi_brano_handler(self):
        tipo = self.pick.controlla_login()
        if tipo == 2:
            self.switch_window_2.emit()
        else:
            self.pop_message(text="Disponibile a breve ")
