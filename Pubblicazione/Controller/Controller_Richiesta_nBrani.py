import pickle

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from Pubblicazione.View.Richiesta_nBrani_e_nomeAlbum import Ui_Form

'''Funzione che controlla la view per la richiesta dei brani e il nome dell'album'''
class Controller_Richiesta_nBrani(QtWidgets.QWidget, Ui_Form):
    switch_window = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()

    '''Nel Costruttore vado a collegare le funzioni ai rispettivi pulsanti'''
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.verifica_album = False
        self.controllo_btn_ok = False
        self.nBrani = 0

        self.btn_ok.clicked.connect(self.btn_ok_handler)
        self.btn_Back.clicked.connect(self.btn_back_handler)

    '''Pop Up Finestra'''
    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    '''Funzione che parte quando si va a chiudere la finestra senza l'utilizzo del stato Indietro'''
    def closeEvent(self, event):
        if not self.controllo_btn_ok:
            self.verifica_album = False

    '''Funzione collegata al pulsante btn_ok e permette di far visualizzare un'altra finestra'''
    def btn_ok_handler(self):
        if self.inizializzazione():
            self.switch_window.emit()

    '''Funzione che inizializza le variabili inserite dell'utente'''
    def inizializzazione(self):
        self.album_name = self.nome_album.text()
        self.nBrani = self.numero_brani.text()
        self.put_data_brani(self.nBrani,self.album_name)
        self.controllo_btn_ok = True
        self.verifica_album = True
        try:
            if not self.nBrani.find('.') == 0:
                    if int(self.nBrani) > 1:
                        if self.nome_album:
                            self.nBrani = int(self.nBrani)
                            return True
                        else:
                            raise
                    else: raise

            else : raise
        except:
            self.pop_message(text="Dati mancanti o incorretti")
            return False


    '''Funzione collegata al pulsante btn_back e permette di far visualizzare un'altra finestra'''
    def btn_back_handler(self):
        if self.verifica_album:
            self.verifica_album = False
        self.switch_window_2.emit()

    def put_data_brani(self, numero, album):
        lista = []
        lista.append(numero)
        lista.append(album)
        with open('Data\Database\Album.pkl', 'wb') as Dpi:
            pickle.dump(lista, Dpi)


