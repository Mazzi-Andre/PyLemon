from PyQt5 import QtWidgets
from PyQt5 import QtCore

from Gestione_del_profilo.Model.Gestione_profilo import DataPick
from Gestione_del_profilo.View.Rimozione_brani import rimozione_brani
from Pubblicazione.Model.pubblicazione_gestione import Gestione_json


'''------------Classe controller per la rimozione dei brani-----------'''

class controller_rimozioni_brani(QtWidgets.QWidget,rimozione_brani):
    switch_window_1 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.brani_artista()
        self.btn_eliminazione.clicked.connect(self.elimina_brano)
        self.btn_eliminazione.clicked.connect(self.btn_back_handler)
        self.btn_Back.clicked.connect(self.btn_back_handler)


    '''---------Pop up message----------'''

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()



    '''-------------Metodo per settare nella table la lista dei brani da poter eliminare-----------'''

    def brani_artista(self):
        data = DataPick()
        g = Gestione_json()
        json_data = g.get_jsonobject()
        brani_artista = []
        self.nome_artista = data.return_credenziali()[1].title() + " " + data.return_credenziali()[2].title()
        for i in json_data:
            if self.nome_artista == i["Artista"]:
                brani_artista.append(i["Titolo"])
        if brani_artista:
            self.table.setRowCount(len(brani_artista))
            j = 0
            for i in brani_artista:
                self.table.setItem(j, 0, QtWidgets.QTableWidgetItem(i))
                j = j + 1
        else:
            self.table.setRowCount(4)
            self.table.setItem(1, 0, QtWidgets.QTableWidgetItem("Ancora nessun brano"))


    '''----------Metodo per la rimozione del brano--------'''

    def elimina_brano(self):
        if self.table.selectedItems():
            g = Gestione_json()
            g.elimina_object(self.nome_artista, self.table.currentItem().text())


    '''--------Switch finestre--------'''

    def btn_back_handler(self):
        self.switch_window_1.emit()


