import pickle

from PyQt5 import QtCore
from PyQt5 import QtWidgets


from Gestione_del_profilo.View.Home_ascoltatore import home_ascoltatore


class controller_ascoltatore(QtWidgets.QWidget, home_ascoltatore):
    switch_window_1 = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()
    switch_window_4 = QtCore.pyqtSignal()
    switch_window_5 = QtCore.pyqtSignal()
    switch_window_k = QtCore.pyqtSignal()

    def __init__(self, list):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.list_top5 = list
        self.btn_Impostazioni.clicked.connect(self.btn_Impostazioni_handler)
        self.btn_mostraTutte.clicked.connect(self.btn_MostraTutte_handler)
        self.btn_Logout.clicked.connect(self.btn_LogOut_handler)
        self.btn_search.clicked.connect(self.put_data)
        self.btn_search.clicked.connect(self.btn_MostraSearch_handler)
        self.btn_limone.clicked.connect(self.btn_limone_handler)

        self.top5()



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

    def btn_MostraSearch_handler(self):
        self.switch_window_4.emit()

    def btn_limone_handler(self):
        self.switch_window_5.emit()

    def btn_LogOut_handler(self):
        self.switch_window_k.emit()

    def put_data(self):
        nome = self.txt_nome.text()
        lista = []
        lista.append(nome)
        with open('C:\Progetti_Python\PySound\Data\pkl\Canzone.pkl', 'wb') as Dpi:
            pickle.dump(lista, Dpi)


    def top5(self):
        self.table.setRowCount(5)
        j = 0
        for i in self.list_top5:
            self.table.setItem(j, 0, QtWidgets.QTableWidgetItem(i))
            j = j + 1
            if j == 5:
                break

    """DA FINIRE"""

    """def bool_search_check(self):
        if len(self.lineEdit.text()) <= 1:
            self.pop_message(text='Inserire un titolo valido')
        else:
            if classeManu.funz is False
                self.pop_message(text='Canzone non trovata')"""





