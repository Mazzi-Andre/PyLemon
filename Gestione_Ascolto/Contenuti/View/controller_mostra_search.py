from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Gestione_Ascolto.Contenuti.View.VistaContenuti_e_player import Ui_Player, controller_player


class controller_mostra_search(QtWidgets.QWidget, Ui_Player, controller_player):
    switch_window_1 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.mostra_search()

        self.play.clicked.connect(self.go_play)
        self.pause.clicked.connect(self.go_pause)
        self.stop.clicked.connect(self.go_stop)
        self.prev.clicked.connect(self.go_prev)
        self.next.clicked.connect(self.go_next)
        self.horizontalSlider.valueChanged.connect(self.changeValue)