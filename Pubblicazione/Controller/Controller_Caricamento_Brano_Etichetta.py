import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from Pubblicazione.View.Caricamento_brano_etichetta import Caricamento_brano_etichetta
from Pubblicazione.Model.pubblicazione_gestione import Gestione_mp3, Gestione_json

''' Classe di controllo per le funzionalità dell caricamento di un brano per un'etichetta discografica'''
class Controller_Caricamento_Brano_Etichetta(QtWidgets.QWidget, Caricamento_brano_etichetta):
    switch_window = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()

    ''' Nel costruttore andiamo a definire delle variabili utili a seguire e collegare i pulsanti della view con delle fuzioni definite sotto'''
    def __init__(self,verifica_album,nome_album):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.verifica_album = verifica_album
        self.nome_album = nome_album
        self.path = ""
        self.btn_Scegli_file.clicked.connect(self.btn_scegli_file_handler)
        self.btn_Pubblica.clicked.connect(self.btn_pubblica_handler)
        self.btn_Back.clicked.connect(self.btn_back_handler)

    '''Pop Up Pinestra'''
    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    '''Funzione per pubblicare un brano collegato al pulsante btn_pubblica'''
    def btn_pubblica_handler(self):
        try:
            if not self.path == '':
                path = str(self.path)
                str_split = path.split(", ")
                newfile1 = str_split[0].replace("(", "")
                newfile2 = newfile1.replace("'", "")
                G = Gestione_mp3()
                J = Gestione_json()
                G.Carica_mp3(newfile2)
                nome = self.lineEdit.text()
                artista = self.lineEdit_2.text()
                if nome and artista:
                    if self.verifica_album == False:
                        album = nome
                    else:
                        album = self.nome_album
                    contatore = 0
                    id = G.json_contatore["contatore_id"]
                    J.carica_brano_su_JSON(nome, artista, album, id, contatore)
                    self.pop_message(text="Brano caricato con successo")
                    if self.verifica_album == True:
                        self.switch_window.emit()
                else: self.pop_message(text="Inserisci i campi mancanti")
            else: self.pop_message(text="Indicare il file mp3 da caricare")
        except:
            self.pop_message(
                text="Il file non esiste o errore sul nome del file.\n TIP: Prova a non utilizzare parentesi tonde, quadrate e graffe, gli slash e le virgolette")

    '''Funzione che permette di visualizzare un File Dialog e prende il path del file, collegata al pulsante btn_scegli_file'''
    def btn_scegli_file_handler(self):
        self.path = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter='Data File (*.mp3)',
        )

    '''Funzione collegata al pulsante btn_back e permette di far visualizzare un'altra finestra'''
    def btn_back_handler(self):
        self.switch_window_2.emit()