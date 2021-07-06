import json
import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout
from Pubblicazione.View.Caricamento_brano_etichetta import Caricamento_brano_etichetta
from Data_Utente.control.Data_control import DataPick
from Pubblicazione.Controller.Gestione_json import Gestione_json
from Pubblicazione.Controller.Gestione_mp3 import Gestione_mp3


class Controller_Caricamento_Brano_Etichetta(QtWidgets.QWidget, Caricamento_brano_etichetta):
    switch_window = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()

    def __init__(self,verifica_album,nome_album):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pick = DataPick()
        self.myData = self.pick.return_credenziali()

        self.verifica_album = verifica_album
        self.nome_album = nome_album

        self.btn_Scegli_file.clicked.connect(self.btn_scegli_file_handler)
        self.btn_Pubblica.clicked.connect(self.btn_pubblica_handler)
        self.btn_Back.clicked.connect(self.btn_back_handler)

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()


    def btn_pubblica_handler(self):
        path = str(self.path)
        ciao = path.split(", ")
        newfile1 = ciao[0].replace("(", "")
        newfile2 = newfile1.replace("'", "")
        G = Gestione_mp3()
        J = Gestione_json()
        G.Carica_mp3(newfile2)
        nome = self.lineEdit.text()
        artista = self.lineEdit_2.text()
        if self.verifica_album == False:
            album = nome
        else:
            album = self.nome_album
        contatore = 0
        id = G.json_contatore["contatore_id"]
        J.carica_brano_su_JSON(nome, artista, album, id, contatore)
        self.pop_message(text="Brano caricato con successo.")
        if self.verifica_album == True:
            self.switch_window.emit()

    def btn_scegli_file_handler(self):
        self.path = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter='Data File (*.mp3)',
            # initialFilter='Data File (*.mp3)'
        )

    def btn_back_handler(self):
        self.switch_window_2.emit()