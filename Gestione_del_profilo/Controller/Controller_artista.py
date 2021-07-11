import pickle

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Data_Utente.control.Data_control import DataPick
from Gestione_del_profilo.View.Home_artista import home_artista


class controller_artista(QtWidgets.QWidget,home_artista):
    switch_window_1 = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()
    switch_window_3 = QtCore.pyqtSignal()
    switch_window_4 = QtCore.pyqtSignal()
    switch_window_5 = QtCore.pyqtSignal()
    switch_window_k = QtCore.pyqtSignal()

    def __init__(self, list5, list_brani):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.list_top5 = list5
        self.list_miei_brani = list_brani

        self.btn_Impostazioni.clicked.connect(self.btn_Impostazioni_handler)
        self.btn_mostraTutte.clicked.connect(self.btn_MostraTutte_handler)
        self.btn_Logout.clicked.connect(self.btn_LogOut_handler)
        self.btn_Pubblica.clicked.connect(self.btn_Pubblicazione_handler)
        self.btn_search.clicked.connect(self.put_data)
        self.btn_search.clicked.connect(self.btn_MostraSearch_handler)
        self.btn_limone.clicked.connect(self.btn_limone_handler)

        self.top5()
        self.brani_artista()


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

    def btn_Pubblicazione_handler(self):
        self.switch_window_3.emit()

    def btn_MostraSearch_handler(self):
        self.switch_window_4.emit()

    def btn_limone_handler(self):
        self.switch_window_5.emit()

    def btn_LogOut_handler(self):
        self.switch_window_k.emit()

    def put_data(self):
        self.nome = self.txt_nome.text()
        self.lista = []
        self.lista.append(self.nome)
        with open('Canzone.pkl', 'wb') as Dpi:
            pickle.dump(self.lista, Dpi)

    def top5(self):
        self.table_top.setRowCount(5)
        j=0
        for i in self.list_top5:
            self.table_top.setItem(j, 0, QtWidgets.QTableWidgetItem(i))
            j = j+1
            if j==5:
                break


    def brani_artista(self):
        if self.list_miei_brani:
            self.table_brani.setRowCount(len(self.list_miei_brani))
            j = 0
            for i in self.list_miei_brani:
                self.table_brani.setItem(j, 0, QtWidgets.QTableWidgetItem(i))
                j = j + 1
        else :
            self.table_brani.setRowCount(4)
            self.table_brani.setItem(1, 0, QtWidgets.QTableWidgetItem("Ancora nessun brano"))
            self.table_brani.item(1, 0).setTextAlignment(5)
