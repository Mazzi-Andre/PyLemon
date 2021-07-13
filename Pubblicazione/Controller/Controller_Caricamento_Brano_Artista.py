import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from Pubblicazione.View.Caricamento_brano_Artista import Caricamento_brano
from Data_Utente.control.Data_control import DataPick

from Pubblicazione.Controller.Gestione_json import Gestione_json
from Pubblicazione.Controller.Gestione_mp3 import Gestione_mp3

''' Classe di controllo per le funzionalità dell caricamento di un brano per un'artista. '''
class Controller_Caricamento_Brano_Artista(QtWidgets.QWidget, Caricamento_brano):
    switch_window = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()
    switch_window_3 = QtCore.pyqtSignal()

    ''' Nel costruttore andiamo a definire delle variabili utili a seguire e collegare i pulsanti della view con delle fuzioni definite sotto'''
    def __init__(self,verifica_album, nome_album):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        pick = DataPick()
        myData = pick.return_credenziali()
        self.nomeartista = myData[1]
        self.cognomeartista = myData[2]

        self.Gestione_mp3 = Gestione_mp3()
        self.Gestione_Json = Gestione_json()

        self.verifica_album = verifica_album
        self.nome_album = nome_album
        self.path=""

        self.btn_scegli_file.clicked.connect(self.btn_scegli_file_handler)
        self.btn_pubblica.clicked.connect(self.btn_pubblica_handler)
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
                path= str(self.path)
                stringa_split = path.split(", ")
                nomefile = stringa_split[0].replace("(", "")
                nomefile2 = nomefile.replace("'","")
                verifica_pubb_mp3 = self.Gestione_mp3.Carica_mp3(nomefile2)
                if verifica_pubb_mp3:
                    nome = self.txt_nome_brano.text()
                    if nome:
                        artista = self.nomeartista + " " + self.cognomeartista
                        if self.verifica_album == False:
                            album = nome
                        else: album = self.nome_album
                        contatore = 0
                        id = self.Gestione_mp3.json_contatore["contatore_id"]
                        self.Gestione_Json.carica_brano_su_JSON(nome,artista,album,id,contatore)
                        self.pop_message(text="Brano caricato con successo.\n"
                                            "Per vedere gli aggiornamenti ne I TUOI BRANI rieffettuare l'accesso")
                        if self.verifica_album == True:
                            self.switch_window.emit()
                    else: self.pop_message(text="Immetti un titolo")
                else : self.pop_message(
                text="Errore sul nome del file.\n"
                     "TIP: Prova a rinominare il file non utilizzando parentesi tonde, quadrate e graffe, gli slash e le virgolette.")
            else: self.pop_message(text="Indicare il file mp3 da caricare")
        except:
            self.pop_message(text="Il file non esiste")



    '''Funzione che permette di visualizzare un File Dialog e prende il path del file, collegata al pulsante btn_scegli_file'''
    def btn_scegli_file_handler(self):
        self.path = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter='Data File (*.mp3)'
        )

    '''Funzione collegata al pulsante btn_back e permette di far visualizzare un'altra finestra'''
    def btn_back_handler(self):
        self.switch_window_2.emit()

    '''Funzione secondaria collegata al pulsante btn_pubblica e permette di far visualizzare un'altra finestra'''
    def btn_back_pubblica(self):
        self.switch_window_3.emit()











