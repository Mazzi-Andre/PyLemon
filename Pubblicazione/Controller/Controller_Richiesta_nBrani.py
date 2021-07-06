from PyQt5 import QtCore
from PyQt5 import QtWidgets
from Pubblicazione.View.Richiesta_nBrani_e_nomeAlbum import Ui_Form

class Controller_Richiesta_nBrani(QtWidgets.QWidget, Ui_Form):
    switch_window = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.btn_ok.clicked.connect(self.btn_ok_handler)
        self.btn_Back.clicked.connect(self.btn_back_handler)


    def btn_ok_handler(self):
        self.inizializzazione()
        self.switch_window.emit()

    def inizializzazione(self):
        self.nome_album =  self.txt_nome_album.text()
        self.nBrani = self.txt_nBrani.text()

    def btn_back_handler(self):
        self.switch_window_2.emit()


    #def get_nBrani(self):
        #return self.nBrani

    #def get_nome_album(self):
        #return self.nome_album







