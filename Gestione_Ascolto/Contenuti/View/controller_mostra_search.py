import pickle

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Data_Utente.control.Data_control import DataPick
from Gestione_Ascolto.Contenuti.View.VistaContenuti_e_player import Ui_Player
from Gestione_del_profilo.View.Home_artist import home_artista
from Gestione_del_profilo.View.Home_label import home_etichetta
from Gestione_del_profilo.View.Home_listener import home_ascoltatore


class controller_mostra_search(QtWidgets.QWidget, Ui_Player, DataPick, home_ascoltatore, home_etichetta, home_artista):
    switch_window_1 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pick = DataPick()
        self.Mysong = self.get_canzone()

        self.mostra_search()

        self.play.clicked.connect(self.go_play)
        self.pause.clicked.connect(self.go_pause)
        self.stop.clicked.connect(self.go_stop)
        self.prev.clicked.connect(self.go_prev)
        self.next.clicked.connect(self.go_next)
        self.horizontalSlider.valueChanged.connect(self.changeValue)



    def mostra_search(self):
        self.var_search = self.Mysong[0]
        self.check_prev = False
        self.check_next = False
        self.riga_locale = ''
        self.primo_play = False
        self.lib = self.controller.getObject()
        riga = 0
        self.table.setRowCount(len(self.lib))
        var_title = self.var_search.title()
        for i in self.lib:
            check_riga = False
            if i["Titolo"] == var_title:
                self.table.setItem(riga, 0, QtWidgets.QTableWidgetItem(i["Titolo"]))
                self.table.setItem(riga, 1, QtWidgets.QTableWidgetItem(i["Album"]))
                self.table.setItem(riga, 2, QtWidgets.QTableWidgetItem(i["Artista"]))
                check_riga = True

            if i["Album"] == var_title:
                self.table.setItem(riga, 0, QtWidgets.QTableWidgetItem(i["Titolo"]))
                self.table.setItem(riga, 1, QtWidgets.QTableWidgetItem(i["Album"]))
                self.table.setItem(riga, 2, QtWidgets.QTableWidgetItem(i["Artista"]))
                check_riga = True

            if i["Artista"] == var_title:
                self.table.setItem(riga, 0, QtWidgets.QTableWidgetItem(i["Titolo"]))
                self.table.setItem(riga, 1, QtWidgets.QTableWidgetItem(i["Album"]))
                self.table.setItem(riga, 2, QtWidgets.QTableWidgetItem(i["Artista"]))
                check_riga = True

            if check_riga:
                riga = riga+1

        self.search = True
        self.righe_search = riga-1

    def go_play(self):
        if self.check_prev and self.riga_locale == self.table.currentRow():
            titolo_prev = self.table.item(self.riga, 0).text()
            album_prev = self.table.item(self.riga, 1).text()
            path = self.controller.getPath(titolo_prev, album_prev)
            self.listen.path_riproduzione = path
            self.listen.play(path, float(self.horizontalSlider.value() / 10))

        elif self.check_next and self.riga_locale == self.table.currentRow():
            titolo_next = self.table.item(self.riga, 0).text()
            album_next = self.table.item(self.riga, 1).text()
            path = self.controller.getPath(titolo_next, album_next)
            self.listen.path_riproduzione = path
            self.listen.play(path, float(self.horizontalSlider.value() / 10))

        elif self.table.selectedItems():
            self.primo_play = True
            self.riga_locale = self.riga = self.table.currentRow()
            selezione_titolo = self.table.currentItem().text()
            for i in self.lib:
                if selezione_titolo == i["Titolo"]:
                    album_corrispondente = self.table.item(self.riga, 1).text()
                    path = self.controller.getPath(selezione_titolo, album_corrispondente)
                    self.listen.path_riproduzione = path
                    self.listen.play(path, float(self.horizontalSlider.value() / 10))
                    break

    def go_pause(self):
        self.listen.pause()

    def go_stop(self):
        self.listen.stop()

    def go_prev(self):
        if self.primo_play:
            if self.search:
                self.riga = self.riga - 1

                if self.riga < 0:
                    self.riga = self.righe_search

                self.check_prev = True
                self.go_play()
            else:
                self.riga = self.riga - 1
                if self.riga < 0:
                    self.riga = len(self.lib) - 1
                self.check_prev = True
                self.go_play()

    def go_next(self):
        if self.primo_play:
            if self.search:
                self.riga = self.riga + 1
                if self.riga > self.righe_search:
                    self.riga = 0
                self.check_prev = True
                self.go_play()
            else:
                self.riga = self.riga + 1
                if self.riga > len(self.lib) - 1:
                    self.riga = 0
                self.check_next = True
                self.go_play()

    def changeValue(self, value):
        self.listen.vol_adjust(value)


    def get_canzone(self):
        with open('Canzone.pkl', 'rb') as Dpi:
            MyData = pickle.load(Dpi)
        return MyData



