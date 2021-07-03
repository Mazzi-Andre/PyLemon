from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Pubblicazione.View.pubblicazione_inizio import pubblicazione_inizio


class controller_pubblicazione_inizio(QtWidgets.QWidget, pubblicazione_inizio):
    switch_window_1 = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.btn_brano.clicked.connect(self.btn_brano_handler)
        self.btn_album.clicked.connect(self.btn_album_handler)


    """POP UP FINESTRA"""

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    """SWITCH FINESTRE"""

    def btn_brano_handler(self):
        self.switch_window_1.emit()

    def btn_album_handler(self):
        self.switch_window_2.emit()

    def closeEvent(self, event):
        self.pop_message(text="Per vedere gli aggiornamenti ne I TUOI BRANI riaccedere.")



