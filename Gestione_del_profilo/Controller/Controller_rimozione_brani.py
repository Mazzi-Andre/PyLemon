from PyQt5 import QtWidgets

from Data_Utente.control.Data_control import DataPick
from Pubblicazione.Controller.Gestione_json import Gestione_json
from Gestione_del_profilo.View.Rimozione_brani import rimozione_brani


class controller_rimozioni_brani(QtWidgets.QWidget,rimozione_brani):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.brani_artista()
        self.btn_eliminazione.clicked.connect(self.elimina_brano)
        #self.btn_Back.clicked.connect()



    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()


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
        else :
            self.table.setRowCount(4)
            self.table.setItem(1, 0, QtWidgets.QTableWidgetItem("Ancora nessun brano"))


    def elimina_brano(self):
        if self.table.selectedItems():
            g = Gestione_json()
            g.elimina_object(self.nome_artista, self.table.currentItem().text())

            self.pop_message(text="Eliminazione avvenuta con successo.")
            self.pop_message(text="Per vedere gli aggiornamenti rieffettuare l'accesso")



