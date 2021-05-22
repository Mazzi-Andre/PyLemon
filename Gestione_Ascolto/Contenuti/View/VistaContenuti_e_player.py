from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QSizePolicy

from Gestione_Ascolto.Contenuti.Controller.ControlloreContenuti import ControlloreContenuti
from Pubblicazione.Controller.Gestione_JSON import Gestione_JSON


class Ui_Player(object):
    def setupUi(self, Player):
        Player.setObjectName("Player")
        Player.resize(501, 471)
        Player.setAutoFillBackground(False)
        Player.setStyleSheet("background-color: rgb(40, 39, 39);\n"
                                "\n"
                                "")
        self.table = QtWidgets.QTableWidget(Player)

        self.table.setGeometry(QtCore.QRect(0, 0, 501, 351))

        self.table.setMinimumSize(QtCore.QSize(3, 0))
        self.table.setMouseTracking(False)
        self.table.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                        "")
        self.table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table.setLineWidth(0)
        self.table.setMidLineWidth(0)
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table.setAutoScroll(False)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.table.setDragDropOverwriteMode(False)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table.setShowGrid(False)
        self.table.setGridStyle(QtCore.Qt.NoPen)
        self.table.setObjectName("table")
        self.table.setColumnCount(3)
        #self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.table.setHorizontalHeaderItem(2, item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.verticalHeader().setVisible(True)
        self.table.verticalHeader().setHighlightSections(True)
        self.play = QtWidgets.QPushButton(Player)

        self.play.setGeometry(QtCore.QRect(10, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.play.setFont(font)
        self.play.setStyleSheet("font color : rgb (255, 255, 0)\n"
"border-radius: 10px;")
        self.play.setText("")
        self.play.setObjectName("play")
        self.play.setIcon(QIcon('play.png'))
        self.pause = QtWidgets.QPushButton(Player)

        self.pause.setGeometry(QtCore.QRect(110, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pause.setFont(font)
        self.pause.setStyleSheet("font color:rgb (255,255,0)\n"
"border-radius: 10px;")
        self.pause.setText("")
        self.pause.setObjectName("pause")
        self.pause.setIcon(QIcon('pause.png'))
        self.stop = QtWidgets.QPushButton(Player)

        self.stop.setGeometry(QtCore.QRect(210, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.stop.setFont(font)
        self.stop.setStyleSheet("font color:rgb (255,255,0)\n"
"border-radius: 10px;")
        self.stop.setText("")
        self.stop.setObjectName("stop")
        self.stop.setIcon(QIcon('stop.png'))
        self.prev = QtWidgets.QPushButton(Player)

        self.prev.setGeometry(QtCore.QRect(310, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.prev.setFont(font)
        self.prev.setStyleSheet("font color:rgb (255,255,0)\n"
"border-radius: 10px;")
        self.prev.setText("")
        self.prev.setObjectName("prev")
        self.next = QtWidgets.QPushButton(Player)

        self.next.setGeometry(QtCore.QRect(410, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.prev.setIcon(QIcon('prev.png'))
        self.next.setFont(font)
        self.next.setStyleSheet("font color:rgb (255,255,0)\n"
"border-radius: 10px;")
        self.next.setText("")
        self.next.setObjectName("next")
        self.next.setIcon(QIcon('next.png'))
        self.horizontalSlider = QtWidgets.QSlider(Player)
        self.horizontalSlider.setGeometry(QtCore.QRect(70, 440, 80, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(Player)
        self.label.setGeometry(QtCore.QRect(13, 438, 55, 16))
        self.label.setStyleSheet("QLabel { color : white; }");
        self.label.setObjectName("label")

        self.retranslateUi(Player)
        QtCore.QMetaObject.connectSlotsByName(Player)


    def retranslateUi(self, Player):
        _translate = QtCore.QCoreApplication.translate
        Player.setWindowTitle(_translate("Player", "Player"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Player", "Titolo"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Player", "Album"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Player", "Artista"))
        self.table.setColumnWidth(0, 167); self.table.setColumnWidth(1, 167) ;self.table.setColumnWidth(2, 167)
        self.label.setText(_translate("Player", "Volume"))
        """self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.horizontalSlider.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.next.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.prev.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.stop.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pause.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.play.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)"""

    def mostra_tutto(self):
        Libreria = Gestione_JSON()
        lib = Libreria.get_jsonobject()
        riga = 0
        self.table.setRowCount(len(lib))
        for i in lib:
            self.table.setItem(riga, 0, QtWidgets.QTableWidgetItem(lib["Titolo"]))
            self.table.setItem(riga, 1, QtWidgets.QTableWidgetItem(lib["Album"]))
            self.table.setItem(riga, 2, QtWidgets.QTableWidgetItem(lib["Artista"]))
            riga = riga+1

    def prova(self):
        #_translate = QtCore.QCoreApplication.translate
        #self.table.setItem(0, 0, self.table.QTableWidgetItem("ciao"))
        #self.table.item
        '''item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Player", "rrrrrr"))'''
        self.table.setRowCount(45)
        self.table.setItem(0,0, QtWidgets.QTableWidgetItem('ciao'))
        #self.table.setItem(0, 2, self.table.QTableWidgetItem("d"))

    def mostra_search(self, var_search):
        Libreria = ControlloreContenuti()
        lib = Libreria.getLista()
        riga = 0
        self.table.setRowCount(len(lib))
        for i in lib:
            check_riga = False
            if i["Titolo"] == var_search:
                self.table.setItem(riga, 0, QWidget.QTableWidgetItem(lib["Titolo"]))
                self.table.setItem(riga, 1, QWidget.QTableWidgetItem(lib["Album"]))
                self.table.setItem(riga, 2, QWidget.QTableWidgetItem(lib["Artista"]))
                check_riga = True

            if i["Album"] == var_search:
                self.table.setItem(riga, 0, QWidget.QTableWidgetItem(lib["Titolo"]))
                self.table.setItem(riga, 1, QWidget.QTableWidgetItem(lib["Album"]))
                self.table.setItem(riga, 2, QWidget.QTableWidgetItem(lib["Artista"]))
                check_riga = True
            if i["Artista"] == var_search:
                self.table.setItem(riga, 0, QWidget.QTableWidgetItem(lib["Titolo"]))
                self.table.setItem(riga, 1, QWidget.QTableWidgetItem(lib["Album"]))
                self.table.setItem(riga, 2, QWidget.QTableWidgetItem(lib["Artista"]))
                check_riga = True

            if check_riga:
                riga = riga+1







app = QApplication([])
window = QWidget()
form = Ui_Player()
form.setupUi(window)
#form.mostra_tutto()
#form.prova()
window.show()
app.exec()