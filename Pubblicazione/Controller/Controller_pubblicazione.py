from PyQt5 import QtWidgets, QtCore
from Pubblicazione.View.pubblicazione_inizio import pubblicazione_inizio

class controller_pubblicazione(QtWidgets.QWidget,pubblicazione_inizio):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.btn_brano.clicked.connect(self.btn_caricamento_brano)
        self.btn_album.clicked.connect()

    def btn_caricamento_brano(self):
        self.switch_window.emit()




