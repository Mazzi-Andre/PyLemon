import json
import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout

from Pubblicazione.View.Caricamento_brano_Artista import Caricamento_brano
from Data_Utente.control.Data_control import DataPick
from Brani.Model.Brano import Brano
from Pubblicazione.Controller.Gestione_json import Gestione_json
from Pubblicazione.Controller.Gestione_mp3 import Gestione_mp3
from Pubblicazione.Controller.Controller_Richiesta_nBrani import Controller_Richiesta_nBrani

class Controller_Caricamento_Brano_Artista(QtWidgets.QWidget, Caricamento_brano):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pick = DataPick()
        self.myData = self.pick.return_credenziali()
        self.brano= Brano()

        self.btn_scegli_file.clicked.connect(self.btn_scegli_file_handler)
        self.btn_pubblica.clicked.connect(self.btn_pubblica_handler)

        self.nome = self.myData[1]
        self.cognome = self.myData[2]

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def btn_pubblica_handler(self):
        if not self.path == "":
            Gestione_mp3.Carica_mp3(self.path)
            self.brano.nome = self.txt_nome_brano.text()
            if self.brano.artista == "":
                self.brano.artista = self.nome + " " + self.cognome
            else: self.brano.artista #da inserire il nome dell'artista presa dalla schermata prima, nel caso in cui a caricare il brano o album sia un etichetta
            if self.brano.album == "":
                self.brano.album = self.brano.nome
            else: self.brano.album #da inserire il nome dell'album preso dalla schermata fatta da tass
            self.brano.contatore = 0
            with open('ContatoreBrani.json', 'r') as j:
                Json = json.load(j)
            U = Json['contatore']
            contatoreid = U.get["valore"]
            self.brano.id = contatoreid
            Gestione_json.carica_brano_su_JSON(self.brano)
            self.pop_message(text="Brano caricato con successo.")
        else: self.pop_message(text="Indicare il file mp3 da caricare")
        #da chiudere poi la finestra



    def btn_scegli_file_handler(self):
        file_filter = 'Data File (*.mp3)'
        self.path = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Data File (*.mp3)'
        )
        return self.path









