from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Gestione_del_profilo.Model.Gestione_profilo import DataPick
from Gestione_del_profilo.View.Edit_ascoltatore import edit_ascoltatore


'''------------Classe controller view edit ascoltatore------------'''

class controller_edit_ascoltatore(QtWidgets.QWidget,edit_ascoltatore):
    switch_window_1 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pick = DataPick()
        self.myData = self.pick.return_credenziali()

        self.btn_Artista.clicked.connect(self.btn_artista_handler)
        self.btn_Etichetta.clicked.connect(self.btn_etichetta_handler)
        self.btn_Back.clicked.connect(self.btn_back_handler)



    """-----------POP UP FINESTRA----------"""

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()


    """------------SWITCH FINESTRE----------"""

    def btn_artista_handler(self):
        tipo = 'Artista'
        self.pick.update_account(tipo)
        self.pop_message(text="Cambiamento effettuato. \nIl programma si chiuderà per la modifica.")

    def btn_etichetta_handler(self):
        tipo = 'Etichetta'
        self.pick.update_account(tipo)
        self.pop_message(text="Cambiamento effettuato. \nIl programma si chiuderà per la modifica.")

    def btn_back_handler(self):
        self.switch_window_1.emit()