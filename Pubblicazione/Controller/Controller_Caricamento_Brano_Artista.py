import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout

from Pubblicazione.View.Caricamento_brano_Artista import Caricamento_brano
from Data_Utente.control.Data_control import DataPick

from Pubblicazione.Controller.Gestione_json import Gestione_json
from Pubblicazione.Controller.Gestione_mp3 import Gestione_mp3

class Controller_Caricamento_Brano_Artista(QtWidgets.QWidget, Caricamento_brano):
    switch_window = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()

    def __init__(self,verifica_album, nome_album):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        pick = DataPick()
        myData = pick.return_credenziali()
        self.nomeartista = myData[1]
        self.cognomeartista = myData[2]

        self.verifica_album = verifica_album
        self.nome_album = nome_album
        self.path=""
        self.btn_scegli_file.clicked.connect(self.btn_scegli_file_handler)
        self.btn_pubblica.clicked.connect(self.btn_pubblica_handler)
        self.btn_Back.clicked.connect(self.btn_back_handler)

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()



    def btn_pubblica_handler(self):
        if not self.path == '':
            path= str(self.path)
            stringa_split = path.split(", ")
            newfile1 = stringa_split[0].replace("(", "")
            newfile2 = newfile1.replace("'","")
            G = Gestione_mp3()
            J = Gestione_json()
            G.Carica_mp3(newfile2)
            nome = self.txt_nome_brano.text()
            if nome:
                artista = self.nomeartista + " " + self.cognomeartista
                if self.verifica_album == False:
                    album = nome
                else: album = self.nome_album
                contatore = 0
                id = G.json_contatore["contatore_id"]
                J.carica_brano_su_JSON(nome,artista,album,id,contatore)
                self.pop_message(text="Brano caricato con successo.\n"
                                      "Per vedere gli aggiornamenti ne I TUOI BRANI rieffettuare l'accesso")
                if self.verifica_album == True:
                    self.switch_window.emit()
            else: self.pop_message(text="Immetti un titolo")
        else: self.pop_message(text="Indicare il file mp3 da caricare")




    def btn_scegli_file_handler(self):
        self.path = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter='Data File (*.mp3)',
        )

    def btn_back_handler(self):
        self.switch_window_2.emit()