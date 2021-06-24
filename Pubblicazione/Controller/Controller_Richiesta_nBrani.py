from PyQt5 import QtCore
from PyQt5 import QtWidgets
from Pubblicazione.View.Richiesta_nBrani_e_nomeAlbum import Ui_Form

class Controller_Richiesta_nBrani(QtWidgets.QWidget, Ui_Form):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.btn_ok.clicked.connect(self.btn_ok_handler)

        self.nBrani = self.txt_nBrani.text()
        self.nome_album = self.txt_nome_album.text()


    def btn_ok_handler(self):

        self.switch_window.emit()

