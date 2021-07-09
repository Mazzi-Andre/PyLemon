from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from Gestione_Ascolto.Ascolto.Controller.ControlloreAscolto import ControlloreAscolto
from Gestione_Ascolto.Ascolto.Model.Ascolto import Ascolto


'''-----------Classe relativa alla vista grafica del Player, quindi dei dati presenti nella piattaforma----------'''
class Ui_Player(object):
    def setupUi(self, Player):
        self.listen = Ascolto()
        self.controller = ControlloreAscolto()
        self.search = False
        '''-------------Creazione della finestra-----------'''
        Player.setObjectName("Player")
        Player.resize(501, 475)
        Player.setAutoFillBackground(False)
        Player.setStyleSheet("background-color: rgb(40, 39, 39);\n""\n""")


        '''----------------Tabella canzoni riproducibili---------------'''
        self.table = QtWidgets.QTableWidget(Player)
        self.table.setGeometry(QtCore.QRect(0, 0, 501, 351))
        self.table.setMinimumSize(QtCore.QSize(3, 0))
        self.table.setMouseTracking(False)
        self.table.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                 "background-color: rgb(51, 51, 51);"
                                 "border-radius: 5px;\n"
                                 "font: 10pt \"Arial\";"
                                 "color: 'white';}")
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

        item = QtWidgets.QTableWidgetItem();item.setTextAlignment(QtCore.Qt.AlignCenter)
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
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setHighlightSections(True)


        '''-----------------Tasto play-------------------'''

        self.play = QtWidgets.QPushButton(Player)
        self.play.setGeometry(QtCore.QRect(10, 365, 85, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.play.setFont(font)
        self.play.setStyleSheet("border-radius: 10px;\n"
                                "color: 'white';}" +
                                "*:hover{background: rgb(18, 110, 60);\n}")
        self.play.setIconSize(QtCore.QSize(65, 65))
        self.play.setText("")
        self.play.setObjectName("play")
        self.play.setIcon(QIcon('play.png'))


        '''----------------Tasto pausa---------------'''

        self.pause = QtWidgets.QPushButton(Player)
        self.pause.setGeometry(QtCore.QRect(110, 365, 85, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pause.setFont(font)
        self.pause.setStyleSheet("border-radius: 10px;\n"
                                "color: 'white';}" +
                                "*:hover{background: rgb(18, 110, 60);\n}")
        self.pause.setIconSize(QtCore.QSize(40, 40))
        self.pause.setText("")
        self.pause.setObjectName("pause")
        self.pause.setIcon(QIcon('pause.png'))



        '''----------------Tasto stop---------------'''

        self.stop = QtWidgets.QPushButton(Player)
        self.stop.setGeometry(QtCore.QRect(210, 365, 85, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.stop.setFont(font)
        self.stop.setStyleSheet("border-radius: 10px;\n"
                                "color: 'white';}" +
                                "*:hover{background: rgb(18, 110, 60);\n}")
        self.stop.setIconSize(QtCore.QSize(85, 85))
        self.stop.setText("")
        self.stop.setObjectName("stop")
        self.stop.setIcon(QIcon('stop.png'))


        '''----------------Tasto canzone precedente---------------'''

        self.prev = QtWidgets.QPushButton(Player)
        self.prev.setGeometry(QtCore.QRect(310, 365, 85, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.prev.setFont(font)
        self.prev.setStyleSheet("border-radius: 10px;\n"
                                "color: 'white';}" +
                                "*:hover{background: rgb(18, 110, 60);\n}")
        self.prev.setIconSize(QtCore.QSize(52, 52))
        self.prev.setText("")
        self.prev.setObjectName("prev")


        '''-----------------Tasto canzone successiva---------------'''

        self.next = QtWidgets.QPushButton(Player)
        self.next.setGeometry(QtCore.QRect(410, 365, 85, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.prev.setIcon(QIcon('prev.png'))
        self.next.setFont(font)
        self.next.setStyleSheet("border-radius: 10px;\n"
                                "color: 'white';}" +
                                "*:hover{background: rgb(18, 110, 60);\n}")
        self.next.setIconSize(QtCore.QSize(52, 52))
        self.next.setText("")
        self.next.setObjectName("next")
        self.next.setIcon(QIcon('next.png'))


        '''----------------Slider del volume---------------'''

        self.horizontalSlider = QtWidgets.QSlider(Player)
        self.horizontalSlider.setGeometry(QtCore.QRect(80, 443, 90, 25))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setRange(0,10)
        self.horizontalSlider.setValue(2)


        '''--------------Icona volume-------------'''

        self.icon_volume = QtWidgets.QPushButton(Player)
        self.icon_volume.setGeometry(QtCore.QRect(13, 440, 65, 26))
        font = QtGui.QFont()
        self.icon_volume.setFont(font)
        self.icon_volume.setStyleSheet("*{border: 0.5px solid rgb(40, 39, 39);"  # border per i bordi
                                      "border-radius: 25px;\n"
                                      "color: 'white';}")
        self.icon_volume.setText("")
        self.icon_volume.setObjectName("icon_volume")
        self.icon_volume.setIcon(QIcon('volume.png'))
        self.icon_volume.setIconSize(QtCore.QSize(25, 25))



        self.retranslateUi(Player)
        QtCore.QMetaObject.connectSlotsByName(Player)

    def retranslateUi(self, Player):
        _translate = QtCore.QCoreApplication.translate
        Player.setWindowTitle(_translate("Player", ""))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Player", "Titolo"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Player", "Album"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Player", "Artista"))
        self.table.setColumnWidth(0, 167);
        self.table.setColumnWidth(1, 167) ;
        self.table.setColumnWidth(2, 167)
        self.icon_volume.setText(_translate("Player", ""))


