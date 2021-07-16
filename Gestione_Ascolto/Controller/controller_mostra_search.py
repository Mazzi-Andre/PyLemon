from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Gestione_Ascolto.View.VistaContenuti_e_player import Ui_Player
from Pubblicazione.Controller.Gestione_json import Gestione_json

''' Classe di controllo attività: MOSTRA SEARCH.
    L'utente dopo essersi interfacciato con la barra di ricerca, vedrà mostrati i risultati associati'''
class controller_mostra_search(QtWidgets.QWidget, Ui_Player):
    switch_window_1 = QtCore.pyqtSignal()

    def __init__(self,canzone_ricercata):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.Mysong = canzone_ricercata
        self.chiusura_win = False

        self.mostra_search()

        self.play.clicked.connect(self.go_play)
        self.pause.clicked.connect(self.go_pause)
        self.stop.clicked.connect(self.go_stop)
        self.prev.clicked.connect(self.go_prev)
        self.next.clicked.connect(self.go_next)
        self.horizontalSlider.valueChanged.connect(self.changeValue)


    '''Overriding del metodo di QtWidgets.QWidget associato alla finestra di visualizzazione risultati.
       Alla sua chiusura viene stoppata la riproduzione musicale qualora fosse attiva'''
    def closeEvent(self, event):
        self.chiusura_win = True
        self.go_stop()


    '''Metodo che verifica se la ricerca da parte dell'utente produrrà risultati.
       In tal caso, andrà a riempire gli elementi della tabella utilizzata per la visualizzaione delle voci.
       Si avranno informazioni relative a titoli di brani, titoli di album e a nomi di artisti.'''
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


    '''Metodo che controlla la riproduzione musicale a seguito dell'interfacciamento dell'utente (pulsante PLAY)'''
    def go_play(self):
        if self.check_prev and self.riga_locale == self.table.currentRow():
            titolo_prev = self.table.item(self.riga, 0).text()
            album_prev = self.table.item(self.riga, 1).text()
            path = self.controller.getPath(titolo_prev, album_prev)
            g = Gestione_json()
            g.incremento_conta(titolo_prev, album_prev)
            self.listen.path_riproduzione = path
            self.listen.play(path, float(self.horizontalSlider.value() / 10))

        elif self.check_next and self.riga_locale == self.table.currentRow():
            titolo_next = self.table.item(self.riga, 0).text()
            album_next = self.table.item(self.riga, 1).text()
            path = self.controller.getPath(titolo_next, album_next)
            g = Gestione_json()
            g.incremento_conta(titolo_next, album_next)
            self.listen.path_riproduzione = path
            self.listen.play(path, float(self.horizontalSlider.value() / 10))

        elif self.table.selectedItems():
            self.riga_locale = self.riga = self.table.currentRow()
            selezione_titolo = self.table.currentItem().text()
            for i in self.lib:
                if selezione_titolo == i["Titolo"]:
                    album_corrispondente = self.table.item(self.riga, 1).text()
                    path = self.controller.getPath(selezione_titolo, album_corrispondente)
                    g = Gestione_json()
                    g.incremento_conta(selezione_titolo, album_corrispondente)
                    self.listen.path_riproduzione = path
                    self.primo_play = True
                    self.listen.play(path, float(self.horizontalSlider.value() / 10))
                    break

    '''Metodo che controlla la pausa del flusso musicale a seguito dell'interfacciamento dell'utente (pulsante PAUSA)'''
    def go_pause(self):
        self.listen.pause()

    '''Metodo che controlla lo stop del flusso musicale a seguito dell'interfacciamento dell'utente (pulsante STOP)'''
    def go_stop(self):
        self.listen.stop(self.chiusura_win)

    '''Metodo che controlla la riproduzione musicale a seguito dell'interfacciamento dell'utente (pulsante PREV)'''
    def go_prev(self):
        if self.primo_play:
            if self.search:
                if self.righe_search > 0:
                    self.riga = self.riga - 1

                    if self.riga < 0:
                        self.riga = self.righe_search

                    self.check_prev = True
                    self.search = False
                    self.go_play()
            else:
                self.riga = self.riga - 1
                if self.riga < 0:
                    self.riga = self.righe_search
                self.check_prev = True
                self.go_play()

    '''Metodo che controlla la riproduzione musicale a seguito dell'interfacciamento dell'utente (pulsante NEXT)'''
    def go_next(self):
        if self.primo_play:
            if self.search:
                if self.righe_search > 0:
                    self.riga = self.riga + 1
                    if self.riga > self.righe_search:
                        self.riga = 0
                    self.check_prev = True
                    self.search = False
                    self.go_play()
            else:
                self.riga = self.riga + 1
                if self.riga > self.righe_search:
                    self.riga = 0
                self.check_next = True
                self.go_play()

    '''Metodo che controlla la riproduzione musicale a seguito dell'interfacciamento dell'utente (slider del volume)'''
    def changeValue(self, value):
        self.listen.vol_adjust(value)