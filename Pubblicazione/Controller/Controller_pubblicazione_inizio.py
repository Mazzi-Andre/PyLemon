from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Pubblicazione.View.pubblicazione_inizio import pubblicazione_inizio

'''Classe che controlla la view Pubblicazione_inizio che appare quando l'utente decide di voler pubblicare un brano o un album'''
class controller_pubblicazione_inizio(QtWidgets.QWidget, pubblicazione_inizio):
    switch_window_1 = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()

    '''Nel Costruttore andiamo a collegare i pulsanti alle funzioni fatte in seguito'''
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pubb_brano = False

        self.btn_brano.clicked.connect(self.btn_brano_handler)
        self.btn_album.clicked.connect(self.btn_album_handler)



    '''Pop Up Finesta'''
    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    '''Funzione collegata al pulsante btn_brano e permette di far visualizzare un'altra finestra'''
    def btn_brano_handler(self):
        self.switch_window_1.emit()

    '''Funzione collegata al pulsante btn_album e permette di far visualizzare un'altra finestra'''
    def btn_album_handler(self):
        self.switch_window_2.emit()





